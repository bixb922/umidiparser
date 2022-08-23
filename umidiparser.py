f"""
NAME
    umidiparser

AUTHOR
    Hermann Paul von Borries

LICENSE
    MIT, Copyright (c) Hermann Paul von Borries

INSTALLATION
    Copy umidiparser.py to your device.

DESCRIPTION
    This module allows to parse midi files.
    This module does not contain a sound synthesizer, only the capabilities to
    read and interpret a midi file.
    Example:

    import umidiparser
    Import utime
    for event in umidiplay.MidiFile("example.mid"):
        utime.sleep_us( event.delta_us )
        if event.status == umidiplay.NOTE_ON:
            ... start the note event.note on event.channel with event.velocity
        elif event.status == umidiplay.NOTE_OFF :
            ... stop the note event.note stop to sound ...
        elif event.status == umidiplay.PROGRAM_CHANGE:
            ... change midi program to event.program on event.channel ....
        else:
            print("other event", event )

    Memory and CPU usage is optimized for a microcontroller with Micropython. CPU usage can
    be lowered even more by reusing the same MidiEvent over and over
    during the process:
        for event in MidiFile("example.mid", reuse_event_object=True ):
            ... process event....

    Normally the complete midi file will be buffered in RAM when opening the
    file. If RAM is scarce or may be fragmented use:

        for event in MidiFile("example.mid", buffer_size=100 ):
            .... process event...

    This will allocate 100 bytes as a buffer for each track in the
    midi file, open one file descriptor for each track and then read the file
    piecemeal. This will use slightly (about 10%) more CPU, but RAM usage
    is limited to the buffer_size bytes per track, and you can process a files
    much larger than the available heap or RAM.

    MIDI FILE COMPATIBILITY
    The parser will parse midi files format type 0, 1 and 2. Running status events are
    recognized. All standard MIDI channel events (note on, note off,
    program change, control change, etc) and meta and sysex events (track name,
    key signature, time signature, etc) recognized.

    The set tempo meta events and the "pulses per beat"
    (aka "midi ticks per quarter note")
    field of the midi file header are used to calculate the time between events.
    The time is calculated as integer rounded to the nearest microsecond,
    because floating point processing may be slow on some microcontrollers.
    This way utime.sleep_us( event.delta_us ) can be used to sleep between events.
    Set tempo events may be present in any track.

    Multitrack file type 1 files are supported, and tracks are automatically
    merged during playback.

    MIDI file format errors such as running status event at the beginning of
    a track or incorrect file header fields are detected insofar they could
    lead to wrong results. Non standard data chunks are ignored. Missing
    end of track events are inserted on the fly.
    Running status events may have a meta or sysex event in between, as this
    is non standard but common in MIDI files.
    Non standard or custom meta messages are recognized. Values of fields out
    of range, such as note values between 128 and 255 are passed to the calling
    program.

    There are no capabilities to modify or create MIDI files.

    CPU AND RAM USAGE

    Parsing on a ESP32 WROOM with Micropython takes less than
    1 millisecond, and even less if you use the reuse_event_object
    of the MidiFile object.
    That should be enough for playback of music files,
    where there will be, in average, a time of several tens of
    milliseconds between events, and where a delay of a couple of
    milliseconds will not be noticed by the human ear.

    With the reuse_event_object parameter set to true, CPU overhead should be
    about 15% lower, and less heap is used.
    On the ESP32-WROOM, parsing a MIDI file with buffer_size=100 and
    reuse_event_object=True uses about 20kbytes of heap. Each event will
    allocate and free less than 100 bytes of heap, so garbage collections are not
    frequent if little RAM is available.
    Most of the processing such as parsing event data into individual fields
    is delayed until the information is really needed.

    PORTABILITY
    The code is optimized for Micropython, but
    also works with same functionality under regular Python (CPython).
    This allows to develop or test on Linux or Windows and then port to
    Micropython. Not tested on CircuitPython so far.

CLASSES
    The starting point is the MidiFile object, allowing to iterate through
    the events. Events are returned as MidiEvent objects, and the fields
    of the event are visible as attributes of the MidiEvent.
    The tracks of a MIDI file are also
    visible as MidiTrack objects, so each track can be played individually.

DEPENDENCIES
    Imports time/utime. Provides a wrapper to work with CPython "import time".
    Imports os to get the absolute path of the MIDI file.

"""


import time
import os

# Wrapper for python/micropython functions
try:
    # Test if this is Micropython or CircuitPython
    from micropython import const
    UPYTHON = True
    # It is, define wrapper for Micropython dependent functions
    time_sleep_us = lambda usec: time.sleep_us( usec )
    ticks_now_us = lambda: time.ticks_us()
    ticks_diff_us = lambda x, y: time.ticks_diff( x, y )
    os_path_abspath = lambda x : os.getcwd() + "/" + x
except ImportError:
    # Make this code work with cPython
    UPYTHON = False
    # Ignore const
    const = lambda x: x
    # These functions only are available in Micropython
    time_sleep_us = lambda usec: time.sleep( usec/1_000_000 )
    ticks_now_us = lambda : int(time.time()*1_000_000)
    ticks_diff_us = lambda x, y: x - y
    os_path_abspath = lambda x: os.path.abspath( x )

    # Make the @micropython.native decorator do nothing
    def micropython( function ):
        return function
    micropython.native = lambda function : function


# Midi name events
# These events are used by the MidiEvent.__str__() function in a reverse
# dictionary to decode event status byte to readable text
NOTE_OFF = const(0x80)
NOTE_ON = const(0x90)
POLYTOUCH = const(0xa0)
CONTROL_CHANGE = const(0xb0)
PROGRAM_CHANGE = const(0xc0)
AFTERTOUCH = const(0xd0)
PITCHWHEEL = const(0xe0)

# Midi channel events are the midi events that refer
# to a channel such as note on, note off, control change, etc
_FIRST_CHANNEL_EVENT = const(0x80)
_LAST_CHANNEL_EVENT = const(0xef)
# Most midi channel events have 2 bytes of data, except this range
# which consists of two event types:
_FIRST_1BYTE_EVENT = const(0xc0)
_LAST_1BYTE_EVENT = const(0xdf)

_META_PREFIX = const(0xff)
# Meta messages
SEQUENCE_NUMBER = const(0x00)

# Events from 0x01 to 0x1f are "text" events
_META_FIRST_TEXT_EVENT = const(0x01)
TEXT = const(0x01)
COPYRIGHT = const(0x02)
TRACK_NAME = const(0x03)
INSTRUMENT_NAME = const(0x04)
LYRICS = const(0x05)
MARKER = const(0x06)
CUE_MARKER = const(0x07)
PROGRAM_NAME = const(0x08)
DEVICE_NAME = const(0x09)
_META_LAST_TEXT_EVENT = const(0x09)
# No text events officialy defined between 0x09 and 0x1f

# Other Meta events
CHANNEL_PREFIX = const(0x20)
MIDI_PORT = const(0x21)
END_OF_TRACK = const(0x2f)
SET_TEMPO = const(0x51)
SMPTE_OFFSET = const(0x54)
TIME_SIGNATURE = const(0x58)
KEY_SIGNATURE = const(0x59)
SEQUENCER_SPECIFIC = const(0x7f)
_FIRST_META_EVENT = const(0x00)
_LAST_META_EVENT = const(0x7f)

# Sysex/escape event
SYSEX = const(0xf0)
ESCAPE = const(0xf7)

# Define a static buffer for MidiParser of this size in bytes.
# This buffer is used for the data of meta and sysex messages
# If there are larger messages in a file, this buffer will increase automatically
# to accomodate the larger data
_INITIAL_EVENT_BUFFER_SIZE = const(20)


# Parse midi variable length number format,
# used for time deltas and meta message lengths
@micropython.native
def _midi_number_to_int( midi_data ):
    # Converts a midi variable length number to integer. In midi files,
    # variable length numbers are used for delta times (time difference between
    #one midi event and the next) and for variable length fields in meta messages.
    data_byte = next( midi_data )
    if data_byte <= 0x7f:
        # This "if" is really only for an improvement in speed, because
        # most variable length numbers tend to be 1 byte long, so this
        # is the most probable execution path.
        return data_byte

    # The value spans more than one byte, parse until
    # a byte with most significant bit "on" is found, and gather
    # 7 bits of data for each byte found, according to Midi standard.
    value = data_byte & 0x7f
    while data_byte >= 0x80:
        data_byte = next( midi_data )
        value = (value<<7) | (data_byte & 0x7f )
    return value



def _process_events( event_iterator,
                    miditicks_per_quarter,
                    reuse_event_object ):
    # This function iterates through the provided event iterator,
    # getting one MidiEvent at a time, and processes MIDI meta set tempo
    # events to convert the time delta in MIDI ticks to time delta in microseconds,
    # rounded to the next microsecond.
    # The function also ensures that there will be a MIDI meta end of track event
    # at the end (as should be according to MIDI standard).
    # If the reuse_event_object parameter is set to False, a independent deep copy
    # of each event is returned. If the reuse_event_object is True, the same
    # object is returned over and over, to reduce CPU usage and RAM heap allocation.

    # Start with default "microseconds per quarter" according to midi standard
    tempo = 500_000

    for event in event_iterator:

        if not reuse_event_object:
            event = event.copy()

        # According to MIDI spec
        # time (in ms) = number_of_ticks * tempo / divisor * 1000
        # where tempo is expressed in microseconds per quarter note and
        # the divisor is expressed in MIDI ticks per quarter note
        # Do the math in microseconds.
        # Do not use floating point, in some microcontrollers
        # floating point is slow.
        # event.delta_us = ( event.delta_miditicks * tempo \
                          # + (miditicks_per_quarter//2) \
                         # ) // miditicks_per_quarter
        event.delta_us = ( event.delta_miditicks * tempo ) / miditicks_per_quarter


        # Process tempo meta event, get tempo to be used for
        # event.delta_us calculation for next events.
        status = event.status
        if status == SET_TEMPO:
            tempo = event.tempo

        # If end_of_track is seen, stop processing events
        elif status == END_OF_TRACK:
            yield event
            # Ignore events after end of track
            break

        yield event

    else:
        # Loop ended without end_of_track meta event, yield one
        # last event of type "end of track" to make caller happy.
        yield MidiEvent()._set_end_of_track()



class _MidiParser:
    # This class instantiates a MidiParser, the class constructor
    # accepts a iterable with MIDI events in MIDI file format, i.e.
    # it accepts a iterable for the content of a MIDI file track.
    def __init__( self, midi_data ):
        # Initialize a parser on the midi_data iterable. The parsing
        # is then done with the parse_events method.

        # Allocate data buffers for the sake of CPU and RAM efficiency,
        # to avoid allocating new objects for each event parsed.

        # Save midi data iterator
        self._midi_data = midi_data

        # The first event cannot be a "running status event"
        self._running_status = None

        # This buffer is for meta and sysex events.
        # This buffer can potentially grow
        # because it must contain the largest midi meta, sysex,
        # or escape  event in the file.
        self._buffer = bytearray(_INITIAL_EVENT_BUFFER_SIZE )

        # The most frequently used buffers are 1 and 2 bytes long
        # For CPU/RAM efficiency, preallocate these buffers.
        # These two buffers are used only for midi channel events
        self._buffer1 = memoryview(bytearray(1))
        self._buffer2 = memoryview(bytearray(2))


    def _parse_events( self ):
        # This generator will parse the midi_data iterable
        # and yield MidiEvent objects until end of data (i.e. this
        # function is in itself a generator for events)

        # For CPU and RAM efficiency, the midi event is always returned
        # in the same object, that is, the MidiEvent returned is allocated
        # once, and set before yielding to the new values. It is responsibility
        # of the caller to copy the event if needed. The data buffer in the
        # event is also reused from one call to the next (see __init__).

        # Exceptions:
        # ValueError if the midi event subtype is in the range 0x7f to 0xff.
        # RuntimeError if there is a running status event without a previous
        # midi channel event.
        # RuntimeError if a system common or real time event is detected (event
        # status byte 0xf1-0xf6 and 0xf7-0xfe. These type of events are not allowed
        # in MIDI files.

        event = MidiEvent()
        midi_data = self._midi_data
        try:
            while True:
                # Parse a delta time
                delta = _midi_number_to_int( midi_data )

                # Parse a message
                event_status, data = self._parse_message(  )

                # Set the event with new data
                event._set( event_status, data, delta )

                yield event

        except StopIteration:
            # No more input data, "next" in called function got end of data,
            # stop this generator
            return


    @micropython.native
    def _parse_non_channel_events( self, event_status ):
        # Parses meta, sysex and escape events

        # Precondition: the event status byte has already been read.
        # Postcondition: the event data has been parsed and the next
        # byte in midi_data is a new MIDI event.

        midi_data = self._midi_data

        if event_status == _META_PREFIX:
            # Midi messages event status has format
            # 0xff nn (nn from 0x00-0x7f)
            # discard 0xff, keep nn as event status
            event_status = next( midi_data )

            # The second event status byte might not be in range
            # defined by standard
            if not  _FIRST_META_EVENT \
                    <= event_status \
                    <= _LAST_META_EVENT:
                raise ValueError(\
                    f"Meta midi second event status byte (0x{event_status:x}) "
                    "not in range 0x00-0x7f")

        # All non-channel events have a variable length field
        data_length = _midi_number_to_int( midi_data )

        # Data might be longer than available buffer
        if data_length >= len(self._buffer):
            # Increase buffer size to fit the data.
            self._buffer = bytearray( data_length )

        # Use a memoryview for efficiency, this avoids copying the buffer
        # and allows to return a slice of the current size efficiently.
        data = memoryview(self._buffer)[0:data_length]

        # Now copy the data from the input midi_data to the buffer
        for idx in range(data_length):
            data[idx] = next( midi_data )

        return event_status, data

    @micropython.native
    def _parse_channel_event( self, event_status, data_byte ):
        # Parse midi channel events, i.e. events with event status
        # byte 0x80 to 0xef. Procesess both regular channel events and
        # running status events.
        # Precondition: the event status byte has already been read.
        # Postcondition: the event data has been parsed and the next
        # byte in midi_data is a new MIDI event.

        # Check if this event is 1 or 2 bytes long
        if _FIRST_1BYTE_EVENT <= event_status \
            <= _LAST_1BYTE_EVENT:
            # This is a one-byte midi channel event,
            # such as program change, use 1 byte preallocated buffer
            data = self._buffer1
            data[0] = data_byte

        else:
            # This is a two-byte midi channel event, such as note on,
            # note off, use preallocated buffer
            data = self._buffer2
            data[0] = data_byte
            data[1]= next( self._midi_data )

        return event_status, data

    @micropython.native
    def _parse_message( self ):
        # Parse a MIDI  message in a MIDI file. Uses _parse_channel_event
        # or _parse_non_channel_events depending on the event status byte.
        # Precondition: the next byte in the midi_data is the
        # event status byte.
        midi_data = self._midi_data

        # Preconditions: the next byte in midi_data should now be
        # the starting byte of a midi event, i.e a
        # midi event status byte. Delta time has already been parsed

        # Get event_status byte
        event_status = next( midi_data )
        if event_status < 0x80:
            # This is a running event. It has no event status byte,
            # only data, the event status byte is the one from the last midi channel
            # event seen in the midi_data.

            # A running event at the beginning of a track is an error
            if self._running_status is None:
                raise RuntimeError("Midi running status without previous channel event")

            # Reuse the event_status as first data byte and parse the event
            return self._parse_channel_event(
                    self._running_status,
                    event_status )

        if _FIRST_CHANNEL_EVENT \
                <= event_status \
                <= _LAST_CHANNEL_EVENT:
            # Not a running event, this is a midi channel event
            # (status 0x80-0xef) followed by 1 or 2 bytes of data

            # Remember event status in case next event is a
            # running status event
            self._running_status = event_status

            return self._parse_channel_event(
                    event_status,
                    next( midi_data ) )

        if event_status in (_META_PREFIX, SYSEX, ESCAPE ):
            return self._parse_non_channel_events( event_status )

        # Neither midi channel event, nor meta, nor sysex/escape.
        # Real time and system common events are not expected in MIDI files.
        raise RuntimeError("Real time/system common event"
                f" status 0x{event_status:x}"
                " not supported in midi files")


class MidiEvent:
    """
    Represents a parsed midi event.

    PROPERTIES AVAILABLE FOR ALL EVENTS

    event.status: this is the event type, such as note on, note off,
    set tempo, end of track, sysex. You can compare event.status
    with the constants umidiparser.NOTE_ON, umidiparser.NOTE_OFF,
    umidiparser.PROGRAM_CHANGE, etc.

    event.delta_miditicks: difference, in midi ticks or pulses between last event
    and this event, also known as "delta time" of the event.
    For single track files, the time difference is with the previous event
    of the same track. When parsing multitrack files, tracks are merged and this
    time is set during playback to the time difference with the previous event in any track.

    event.delta_us: time in microseconds since the last event for this
    event to start. For example, you might use sleep_us( event.delta_us ) to
    sleep the appropriate time for the event to start.

    event.data contains the raw event data.

    str(event) will a string like this:


    PROPERTIES BY EVENT TYPE

    For each type of event, only the applicable properties are enabled.
    The following list shows the event status and properties
    that you can get.

    For example: for a note_on event, event.status is umidiparser.NOTE_ON
    and event.note, event.channel, and event.velocity have the corresponding
    values. But for a program change event, event.velocity will not be available.

    Attributes that are not allowed generate an AttributeError on access.

    PROPERTIES FOR MIDI CHANNEL EVENTS
    NOTE_OFF /midi event status byte=0x80 to 0x8f)
        channel (int)
        note (int)
        velocity (int)
    NOTE_ON (midi event status byte=0x90 to 0x9f)
        channel (int)
        note (int)
        velocity (int)
    POLYTOUCH (midi event status byte=0xa0 to 0xaf)
        channel (int)
        note (int)
        value (int)
    CONTROL_CHANGE (midi event status byte=0xb0 to 0xbf)
        channel (int)
        control (int)
        value (int)
    PROGRAM_CHANGE (midi event status byte=0xc0 to 0xcf)
        channel (int)
        program (int)
    AFTERTOUCH (midi event status byte=0xd0 to 0xdf)
        channel (int)
        value (int)
    PITCHWHEEL (midi event status byte=0xe0 to 0xef)
        channel (int)
        pitch (int)

    PROPERTIES FOR META AND SYSEX EVENTS
    SEQUENCE_NUMBER (midi meta 0xff 0x00)
        number (int)
    TEXT (midi meta 0xff 0x01)
        text (str)
    COPYRIGHT (midi meta 0xff 0x02)
        text (str)
    TRACK_NAME (midi meta 0xff 0x03)
        name (str)
    INSTRUMENT_NAME (midi meta 0xff 0x04)
        name (str)
    LYRICS (midi meta 0xff 0x05)
        text (str)
    MARKER (midi meta 0xff 0x06)
        text (str)
    CUE_MARKER (midi meta 0xff 0x07)
        text (str)
    PROGRAM_NAME (midi meta 0xff 0x08)
        name (str)
    DEVICE_NAME (midi meta 0xff 0x09)
        name (str)
    CHANNEL_PREFIX (midi meta 0xff 0x20)
        channel (int)
    MIDI_PORT (midi meta 0xff 0x21)
        port (int)
    END_OF_TRACK (midi meta 0xff 0x2f)
        no event specific attributes available
    SET_TEMPO (midi meta 0xff 0x51)
        tempo (int)
    SMPTE_OFFSET (midi meta 0xff 0x54)
        frame_rate (int)
        frames (int)
        hours (int)
        minutes (int)
        seconds (int)
        sub_frames (int)
    TIME_SIGNATURE (midi meta 0xff 0x58)
        clocks_per_click (int)
        denominator (int)
        notated_32nd_notes_per_beat (int)
        numerator (int)
    KEY_SIGNATURE (midi meta 0xff 0x59)
        key (str)
    SEQUENCER_SPECIFIC (midi meta 0xff 0x7f)
        data (memoryview)

    SYSEX  0xf0
        data (memoryview)
    ESCAPE  0xf7
        data (memoryview)
    """
    @micropython.native
    def __init__( self ):
        """
        Initializes MidiEvent, all instances are assigned None as value,
        this is. This method is used internally by MidiParser.

        Usually you will not need to create an instance of MidiEvent,
        MidiEvent objects are returned by iterating over the MidiFile
        object.

        """
        # MidiEvent private instance variables:
        #   self._event_status_byte
        #       The original event status byte, as detected in the midi file.
        #       The difference with self.status is that the _event_status_byte
        #       still has the channel number in the lower half in the case of
        #       a midi channel event.
        #
        #   self._status
        #       Same as self._event_status_byte but with the lower nibble
        #       cleared for midi channel events. self.status is a read only
        #       property for self._status.
        #
        #   self._data
        #       The raw data of the event. self.data is the read only
        #       property for self._data.

        self._event_status_byte = None
        self._data = None

        self._status = None
        self.delta_miditicks = None
        self.delta_us = None

    @micropython.native
    def _set( self, event_status, data, delta_miditicks ):
        # Set event information to the event status byte, data and
        # delta time (in miditicks) specified in the parameters, replacing all
        # previous information in the event (if there was any).

        # event_status: contains the event status byte as found in the file.
        # In case of midi channel events, lower nibble has the channel number.
        # For meta messages, the first byte of the meta status is 0xff,
        # so the event_status contains the second byte or "meta event type"
        # with values from 0 to 0x7f (_FIRST_META_EVENT to _LAST_META_EVENT).

        # data: a buffer with the raw data of the event.

        # delta_miditicks: the delta time (time difference with previous event)
        # in midi ticks (or pulses).

        # Store event status byte and compute event.status
        self._event_status_byte = event_status
        if _FIRST_CHANNEL_EVENT <= event_status <= _LAST_CHANNEL_EVENT:
            self._status = event_status & 0xf0
        else:
            self._status = event_status

        self._data = data
        self.delta_miditicks = delta_miditicks
        self.delta_us = None

        return self


    def _set_end_of_track( self ):
        self._set( END_OF_TRACK, b'', 0 )
        self.delta_us = 0
        return self

    @micropython.native
    def _check_property_available( self, *argv ):
        # This method is used to check availabilty of a property.
        # Check if self._status is in list of possible status values
        # and raises AttributeError if not.
        if self._status not in argv:
            raise AttributeError(
                    f"Midi event 0x{self._status:02x}"
                    " does not support attribute")


    def _get_event_name( self ):
        # This metod is used by __str___.
        # Computes the event name as a string. To keep memory
        # requirements at a minimum, instead of having a dictionary of
        # names, this method uses the global variables of thid
        # module as dictionary.

        # Make a dictionary out of the global names of this module
        # Exclude private names starting with _ and
        # exclude names that don't translate to an integer
        event_names_dict = { globals()[varname] : varname.lower() \
                             for varname in globals() \
                             if isinstance(globals()[varname], int) \
                             and varname[0:1] != "_" }

        try:
            name = event_names_dict[self._status]
        except KeyError:
            # Show meaningful information for custom event numbers
            if _FIRST_META_EVENT <= self._status <= _LAST_META_EVENT:
                name = f"meta_0x{self._status:02x}"
            else:
                name = f"midi_0x{self._status:02x}"
        return name

    def _get_property_dict( self ):
        # This is used by __str__
        # Get values for allvalid @properties for
        # this event, except the "data" property

        property_dict = {}
        for prop in dir(MidiEvent):
            if prop[0:1] != "_":
                try:
                    value = getattr( self, prop )
                    # Filter methods from the list
                    if isinstance(value,(int,str)):
                        property_dict[prop] = getattr(self, prop )
                except AttributeError:
                    pass
        return property_dict

    def __str__( self ):
        """
        Standard method to translate the event information to a string,
        for example:
            print(event)
            or
            event_as_a_string = str(event)
        Returns a string with a description of the MidiEvent, starting
        with tne event name in lowercase (note_on, note_off, pitchwheel, set_tempo,
        end_of_track, etc), delta time in midi ticks, delta time in microseconds,
        first few bytes of the raw data, and all properties
        that are allowed for the event type. For example, a "note on" event might
        be shown as:
        "note_on delta[miditicks]=10 delta[usec]=9500 note=60 velocity=64 channel=5"

        The order of the properties in the string may vary.
        """
        description = self._get_event_name()
        # Add event time attributes
        description += " delta[miditicks]=" + str( self.delta_miditicks )
        # Add data, show only a couple of bytes of data
        description += " data=" + str( bytes( self._data[0:5] ) )
        if len(self._data) > 5:
            # Show only first 5 bytes in the data field.
            description = description[0:-1] + "...'"

        # Show time in microseconds only if already computed
        if self.delta_us is not None:
            description += " delta[usec]=" + str(self.delta_us)

        # Get all @property names and their values
        for prop, value in self._get_property_dict().items():
            description += " " + prop + "=" + str(value)
        return description

    @property
    @micropython.native
    def status( self ):
        """
        Returns the event status. For midi channel events, such as note on, note off,
        program change, the lower nibble (lower 4 bits) are cleared (set to zero).
        For a meta event, this is the meta type, for example 0x2f for "end of track".

        Available for all possible events. For custom or proprietary meta events, this
        will be the meta type of that event.

        Examples:
            if event.status == umidiparser.NOTE_OFF:
                .... process note off event ...
            elif event.status == umidiparser.KEY_SIGNATURE:
                ... process key signature meta event ...

        Possible values
        All names are global constants in this module e.g. umidiparser.NOTE_OFF
        NOTE_OFF 0x80
        NOTE_ON 0x90
        POLYTOUCH 0xa0
        CONTROL_CHANGE 0xb0
        PROGRAM_CHANGE 0xc0
        AFTERTOUCH 0xd0
        PITCHWHEEL 0xe0

        Meta messages (all with prefix 0xff)
        SEQUENCE_NUMBER 0x00
        TEXT 0x01
        COPYRIGHT 0x02
        TRACK_NAME 0x03
        INSTRUMENT_NAME 0x04
        LYRICS 0x05
        MARKER 0x06
        CUE_MARKER 0x07
        PROGRAM_NAME 0x08
        DEVICE_NAME 0x09
        CHANNEL_PREFIX 0x20
        MIDI_PORT 0x21
        END_OF_TRACK 0x2f
        SET_TEMPO 0x51
        SMPTE_OFFSET 0x54
        TIME_SIGNATURE 0x58
        KEY_SIGNATURE 0x59
        SEQUENCER_SPECIFIC 0x7f

        Sysex/escape events
        SYSEX 0xf0
        ESCAPE 0xf7
        """
        return self._status

    @property
    @micropython.native
    def channel( self ):
        """
        Returns the channel number for the event, 0-15.

        channel property available for:  NOTE_OFF NOTE_ON
        POLYTOUCH CONTROL_CHANGE PROGRAM_CHANGE AFTERTOUCH
        CHANNEL_PREFIX
        """
        if _FIRST_CHANNEL_EVENT<= self._status <= \
             _LAST_CHANNEL_EVENT:
            # For midi event status byte 0x80 to 0xef,
            # the channel is part of the event status byte
            return self._event_status_byte & 0x0f
        if self._status == CHANNEL_PREFIX:
            return self._data[0]
        raise AttributeError


    @property
    @micropython.native
    def note( self ):
        """
        Returns the note number for the event, usually 0-127.

        note property available for:  NOTE_OFF NOTE_ON POLYTOUCH
        """
        self._check_property_available( NOTE_ON,
                                        NOTE_OFF,
                                        POLYTOUCH )
        return self._data[0]

    @property
    @micropython.native
    def velocity( self ):
        """
        Returns the velocity fot the event, usually 0-127.

        velocity property available for:  NOTE_OFF NOTE_ON
        """

        self._check_property_available( NOTE_ON, NOTE_OFF )
        return self._data[1]

    @property
    def value( self ):
        """
        Returns the the value in the event.

        value property available for:  AFTERTOUCH, CONTROL_CHANGE, POLYTOUCH
        """
        if self._status == AFTERTOUCH:
            return self._data[0]
        if self._status in ( CONTROL_CHANGE, POLYTOUCH):
            return self._data[1]
        raise AttributeError

    @property
    def pitch( self ):
        """
        Returns the pitch for a PITCHWHEEL midi channel event.

        -8192 is the lowest value possible, 0 (zero) means "no pitch bend"
        and 8191 is the highest possible value.
        """
        self._check_property_available( PITCHWHEEL )
        # lsb (0 - 127) and msb (0 - 127) together form a 14-bit number,
        # allowing fine adjustment to pitch.
        # Using hex, 00 40 is the central (no bend) setting.
        # 00 00 gives the maximum downwards bend, and 7F 7F the
        # maximum upwards bend.
        # Return 0 for no bend/central bend, -8192 to -1 for downward
        # bend and -1 to 8191 for upward bend
        return (((self._data[1]&0x7f)-0x40)<<7)| (self._data[0]&0x7f)

    @property
    def program( self ):
        """
        Returns the program number 0-127 for a PROGRAM_CHANGE event.
        """
        self._check_property_available( PROGRAM_CHANGE )
        return self._data[0]

    @property
    def control( self ):
        """
        Returns the value for the controller 0-127 for a CONTROL_CHANGE event.
        """
        self._check_property_available( CONTROL_CHANGE )
        return self._data[0]

    @property
    def number( self ):
        """
        Returns number of a SEQUENCE_NUMBER meta event.
        Values range from 0 to 2**24.
        """
        self._check_property_available(  SEQUENCE_NUMBER )
        # Meta event sequence number has a 2 byte big endian number
        return int.from_bytes(self._data[0:2], "big" )

    def _convert_data_to_iso8859_1( self ):
        return bytearray(self._data).decode("iso8859_1")

    @property
    def text( self ):
        """
        Returns the text for a meta events.

        text property is available for:  TEXT COPYRIGHT LYRICS MARKER CUE_MARKER

        In MIDI files, text is stored as "extended ASCII", this is
        decoded with the iso8859_1 encoding.

        The raw data can be retrieved using the data property.
        """
        self._check_property_available( TEXT,
                                        COPYRIGHT,
                                        LYRICS,
                                        MARKER,
                                        CUE_MARKER )

        return self._convert_data_to_iso8859_1()

    @property
    def name( self ):
        """
        Returns the text for a meta events.

        name property available for:  TRACK_NAME INSTRUMENT_NAME PROGRAM_NAME DEVICE_NAME

        See text property for description of text conversion.

        The raw data can be retrieved using the data property.
        """
        self._check_property_available( TRACK_NAME,
                                        INSTRUMENT_NAME,
                                        PROGRAM_NAME,
                                        DEVICE_NAME )
        return self._convert_data_to_iso8859_1()

    @property
    def port( self ):
        """
        Returns the port number  0-256 for a meta MIDI_PORT message
        """
        self._check_property_available( MIDI_PORT )
        # Meta port event
        return self._data[0]

    @property
    def tempo( self ):
        """
        Returns the tempo (0 to 2**32 microseconds per quarter beat)
        for a SET_TEMPO meta event.
        This module interprets the tempo event before returning it, so
        the following events returned will have their delta_us property
        calculated with the new tempo value.

        """
        self._check_property_available( SET_TEMPO )
        # Meta tempo event, 4 bytes big endian with tempo
        # in microseconds per quarter note or beat
        return int.from_bytes( self._data[0:3], "big")

    @property
    def key( self ):
        """
        Returns the key, as str, for a KEY_SIGNATURE meta event.
  
        For mayor keys:
        C, D, E, F, G, A, B, C#, F#, Cb, Db, Eb, Gb, Ab

        For minor keys:
        Cm, Dm, Em, Fm, Gm, Am, Bm, C#m, F#m, Cbm, Dbm, Ebm, Gbm, Abm

        If the midi message contains a value out of range, a ValueError
        is raised. The raw data can be read with the data property.
        """
        self._check_property_available( KEY_SIGNATURE )
        # Translate data of key meta messages to scale name
        # 2 data bytes: sharps/flats and mayor/minor
        # sharps/flats: 0=no flats/sharps, 1 to 7 number of sharps, -1 to -7 number of flats
        # mayor/minor: 0=mayor, 1=minor
        sharps_flats = self._data[0]
        minor_mayor = self._data[1]

        if sharps_flats > 128:
            sharps_flats -= 256
        if sharps_flats not in range(-7,8) \
                or minor_mayor not in [0,1]:
            raise ValueError(
                    "Midi file format error, key signature meta unrecogized data" )
        if minor_mayor == 0:
            scale_names = ("Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F",
                    "C",
                    "G", "D", "A", "E", "B", "F#", "C#"  )
        else:
            scale_names = ( "Abm", "Ebm", "Bbm", "Fm", "Cm", "Gm", "Dm",
                "Am",
                "Em", "Bm", "F#m", "C#m", "G#m", "D#m", "A#m" )
        return scale_names[sharps_flats+7]

    # Time signature meta message
    @property
    def numerator( self ):
        """
        Returns the numerator for the TIME_SIGNATURE meta messages, 0-255.
        """
        self._check_property_available( TIME_SIGNATURE )
        return self._data[0]

    @property
    def denominator( self ):
        """
        Returns the denominator for the TIME_SIGNATURE meta messages, 0-255.
        """
        self._check_property_available( TIME_SIGNATURE )
        return 2**self._data[1]

    @property
    def clocks_per_click( self ):
        """
        Returns the clocks_per_click for the TIME_SIGNATURE meta messages, 0-255.
        """
        self._check_property_available( TIME_SIGNATURE )
        return self._data[2]

    @property
    def notated_32nd_notes_per_beat( self ):
        """
        Returns the notated_32nd_notes_per_beat for the TIME_SIGNATURE meta messages,
        0-255.
        """
        self._check_property_available( TIME_SIGNATURE )
        return self._data[3]

    @property
    def frame_rate( self ):
        """
        Returns the frame for the SMPTE_OFFSET meta messages,
        which can be 24, 25, 29.97 or 30.

        An invalid value in the MIDI file will raise a IndexError
        """
        self._check_property_available( SMPTE_OFFSET )
        return [24,25,29.97,30][(self._data[0] >> 5)]

    @property
    def hours( self ):
        """
        Returns the hour for the SMPTE_OFFSET meta message,
        usually from 0 to 23.
        """
        self._check_property_available( SMPTE_OFFSET )
        return self._data[0] & 0x1f

    @property
    def minutes( self ):
        """
        Returns the minutes for the SMPTE_OFFSET meta message,
        usually from 0 to 59.
        """
        self._check_property_available( SMPTE_OFFSET )
        return self._data[1]

    @property
    def seconds( self ):
        """
        Returns the seconds for the SMPTE_OFFSET meta message,
        usually from 0 to 59.
        """
        self._check_property_available( SMPTE_OFFSET )
        return self._data[2]

    @property
    def frames( self ):
        """
        Returns the frames for the SMPTE_OFFSET meta message,
        usually from 0 to 255.
        """
        self._check_property_available( SMPTE_OFFSET )
        return self._data[3]

    @property
    def sub_frames( self ):
        """
        Returns the sub frames for the SMPTE_OFFSET meta message,
        usually from 0 to 59.
        """
        self._check_property_available( SMPTE_OFFSET )
        return self._data[4]

    @property
    def data( self ):
        """
        Returns the raw data for the underlying message, with no transofrmations,
        as a memoryview, without the event status byte or meta prefix.

        For midi channel events, the length is either 1 or 2 bytes
        according to the event type, for example a "note on" event always
        has 2 bytes of data.
        For a meta or sysex event, "data" contains the payload of the message,
        that is, without meta prefix and length.
        For sysex and escape events, the status (0xf0, xf7) is not included.

        The main purpose is to retrieve message data for sysex and escape events.
        """

        return self._data

    @micropython.native
    def copy( self ):
        """
        Returns a deep copy (a complete independent copy) of the event.
        All values are equal to the original event.

        This can be useful to get a copy of the event in case of using
        the reuse_event_object=True option in the MidiFile.

        Example 1: if you need a list of all MidiEvents
        in a file, then either use:
            event_list = [ event for event in MidiFile("example.mid") ]
        or use:
            event_list = [event.copy for event in MidiFile("example.mid",
                          reuse_event_object=True) ]

        The following code will give an unexpected result, because all
        elements in the list will be equal to the last event of the file:
            event_list = [event for event in MidiFile("example.mid",
                          reuse_event_object=True) ]

        """

        my_copy = MidiEvent()
        my_copy._event_status_byte = self._event_status_byte
        my_copy._status = self._status
        my_copy._data = bytearray( self._data )
        my_copy.delta_miditicks = self.delta_miditicks
        my_copy.delta_us = self.delta_us
        return my_copy

    def is_meta( self ):
        """
        Returns True if this is a Meta event, such as
        lyrics, set tempo or key signature.
        Returns False if this is a MIDI channel event,
        or a Sysex or Escape event.
        """
        return _FIRST_META_EVENT <= self._status <= _LAST_META_EVENT

    def to_midi( self ):
        """
        Returns the event as bytes, in a format that allows sending the
        data to a MIDI controller.

        to_midi will raise AttributeError if the event is for MIDI meta messages, these
        occur in MIDI files and are not normally sent to MIDI controllers.
        """
        if self.is_meta():
            raise AttributeError
        return self._event_status_byte.to_bytes( 1, "big") + self._data



class MidiTrack:
    """
    This object contains the track of a midi file. It is
    created internally by the MidiFile function for each track
    chunk found in the midi file.

    MidiTrack objects are accessible via the MidiFile.tracks list

    """
    def __init__( self,
                file,
                midifile ):
        """
        The MidiTrack cosntructor is called internally by MidiFile,
        you don't need to create a MidiTrack.
        """

        # Parameters are:
        # file: The currently open file midi file, positioned at the start
        # of the track data,
        # just before the 4 bytes with the track or chunk length.
        # midifile: the MidiFile object where this track belongs.

        self._midifile = midifile

        # MTrk header in file has just been processed, get chunk length
        self._tracklen = int.from_bytes( file.read(4), "big" )

        if midifile.buffer_size <= 0:
            # Read the entire track data to RAM
            self._track_data = file.read( self._tracklen )
            self._start_position = None
        else:
            # Remember only start position in file to seek later on
            # During playback if the midi file, one file is opened per track

            self._track_data = None
            self._start_position = file.tell()
            # Skip rest of track chunk
            file.seek( self._tracklen, 1 )

        self._track_parser = None
        self.event = None
        self.current_miditicks = None

    def _buffered_data_generator( self ):
        # Generator to return byte by byte from a buffered track
        # (a track entirely in memory, buffer_size=0)
        # This way seems to be rather fast:
        return ( data_byte for data_byte in self._track_data )


    def _file_data_generator( self ):
        # Generator to return byte by byte of a track with
        # buffer_size=n (n>0). Reads portions of n bytes and then returns
        # byte by byte.

        # Allocate buffer for small portion of the track data,
        # reuse this buffer for each read
        buffer = bytearray( self._midifile.buffer_size )

        # Open file again to read the track
        with open( self._midifile.filename, "rb") as file:
            unread_bytes = self._tracklen
            file.seek( self._start_position )
            while True:
                # Read a buffer of data and yield byte by byte to caller
                bytes_read = file.readinto( buffer )
                yield from memoryview(buffer)[0:bytes_read]
                # Check if end of track reached
                unread_bytes -= bytes_read
                if unread_bytes <= 0 or bytes_read == 0:
                    return

    def _get_midi_data( self ):
        # Sets up generator to yield track data byte per byte
        # deciding which generator to use depending on buffer_size parameter
        if self._track_data is not None:
            return self._buffered_data_generator()
        return self._file_data_generator()


    def __iter__( self ):
        """
        Iterating through a track will yield all events of that track
        of MIDI file. For example, to parser the first track in a midi file:

            for event in MidiFile("example.mid").track[0]:
                .... process event ...

        event.delta_miditicks will have the time difference with the previous
        event, in MIDI ticks (pulses).

        event.delta_us is calculated as the time difference with the previous event
        in microseconds. For this calculation, the set tempo events and
        the MIDI ticks per quarter note (also called "pulses per beat")
        of the MIDI file header are taken into consideration.

        This function should only be necessary to play a single
        track of a format type 2 file. Format 2 type files are
        not very common.

        The last event will always be a END_OF_TRACK event, if missing in the file.

        """
        # Get the parser to return event by event, process set tempo meta events,
        # calculate delta_us and ensure END_OF_TRACK present at the end.
        return _process_events(
                _MidiParser( self._get_midi_data() )._parse_events(),
                self._midifile.miditicks_per_quarter,
                self._midifile.reuse_event_object )

    def _track_parse_start( self ):
        # This is an internal method called by MidiFile for multitrack processing.
        # It starts a parser on the track to return event for event, and
        # keeps the sum of MIDI ticks since the beginning of the track.

        # Two tracks can then compared with track1 > track2 to know which is earlier
        # or later.

        # The events can then retrieved by track.event and advanced to the next
        # with track_parse_next.
        self._track_parser = _MidiParser( self._get_midi_data() )._parse_events()

        # Get first event to get things going...
        self.event = next( self._track_parser )
        self.current_miditicks = self.event.delta_miditicks

        return self


    @micropython.native
    def _track_parse_next( self ):
        # Used internally by MidiFile object.

        # After doing a _track_parse_start, this will return the next event in track.
        self.event = next( self._track_parser )
        self.current_miditicks += self.event.delta_miditicks
        return self.event


    @micropython.native
    def __lt__( self, compare_to ):
        """
        Used internally by the min function to compare the current time in miditicks
        of the different tracks, the goal is to find the next midi event
        of all tracks (the one with the smallest time since the beginning of the track)
        """
        # Compares the _get_current_miditicks value of this track to
        # the same value of another track. Track1 > track2 means that
        # the current event of track 1 will occur later than the current
        # event of track 2, measured in midi ticks.

        # Valid after _track_parse_start.
        return self.current_miditicks < compare_to.current_miditicks

    def _get_current_miditicks(self):
        return self.current_miditicks

class MidiFile:
    """
    Parses a MIDI file.
    Once initialized, you can iterate through the events of the file or
    through the events of a certain track, see __iter__ and play methods.

    """
    def __init__( self,
                  filename,
                  buffer_size=100,
                  reuse_event_object=False ):
        """
        filename

        The name of a MIDI file, usually a .mid or .rtx MIDI file.
        The MIDI file will always be opened read only.

        buffer_size=100

        The buffer size that will be allocated for each track.
        In order to process files larger than the available RAM,
        buffer_size=n will allocate "n" bytes of buffer for
        each track, and read each tracks in "n" byte portions during the
        processing of the file, i.e. while iterating through the events. This will
        need one file descriptor (one open file) for each track, but will
        consume only a fraction of RAM needed for the processing of a file,
        as opposed to reading the file into memory with buffer_size=0.
        A buffer size of less than 10 bytes will increase CPU overhead and is not
        recommended. A buffer size much larger than 100 will probably not give a
        relevant performance advantage, unless the device where the file
        resides is slow.

        If buffer_size=0, all tracks will be read to memory.
        This will need as much RAM as the file size of a complete MIDI file.
        In this case, the time needed to process each event will not depend on
        file access nd will be both faster and more dependable than using a
        buffer_size different to 0, if the device where the file resides is slow.

        The default value for buffer_size is 100 bytes.

        reuse_event_object=False

        With the default value of False, for each call a new MidiEvent is returned,
        this is, if you do:
            for event in MidiFile("example.mid"):
                ... process each event ...

        then in each iteration of the loop you get a different, and new, MidiEvent.
        This is the normal and expected behavior for Python iterators.

        If you need higher processing speed, and if you don't want to
        fragment RAM heap space, use:

            for event in MidiFile("example.mid", reuse_event_object=True):
                ... process each event ....

        In this case, for each iteration of the loop, the same MidiEvent is returned,
        and is overwritten with the last data. The event data will not be
        changed in the body of the for loop. However, if you want to store an event
        for later use,  you'll have to use event.copy.

        All combinations of reuse_event_object and buffer_size are valid.

        Instance variables:

        tracks
        List object with the tracks of the file. len(midifile.tracks) is the number of tracks.
        To get the events in an individual track, use:
            for event in MidiFile("example.mid").tracks[3]:
            ... process events of track 3 of the list ....

        Exceptions:
        The file must start with a standard MIDI file header (MThd), if not, a
        ValueError is raised.
        The MIDI header chunk must be at least 6 bytes long, or a ValueError
        is raised.
        ValueError is raised if no header present, or too short.
        ValueError is raised if the header contains SMPTE time codes (not supported).
        Chunks after the header that are not tracks
        (i.e. don't have a "MTrk" MIDI header) are ignored.

        """

        # Store parameters
        self._reuse_event_object = reuse_event_object
        self._buffer_size = buffer_size

        # Process file
        with open( filename, "rb" ) as file:

            # First chunk must be MThd midi header, process header and validate
            self._format_type, \
                number_of_chunks, \
                self._miditicks_per_quarter = self._get_header( file )
            # Get absolute path to file. Storing
            # a relative path results in error if the calling
            # program changes the working directory
            self._filename = os_path_abspath( filename )

            # Get all track objects of the file.
            # Disregard the number of chunks, read the real number of tracks present.
            self.tracks = []
            for _ in range(number_of_chunks):
                track_id = file.read(4).decode( "ANSI" )
                # Only process MTrk chunks
                if track_id == "MTrk":
                    self.tracks.append( MidiTrack( file, self ) )
                else:
                    # Skip non-track chunk,
                    # parse chunk using MidiTrack but don't append to track list
                    MidiTrack( file, self )


    def _get_header( self, file ):
        # Decodes the MIDI file header, returns the
        # values of the header:
        # format type (0-2), number of data chunks, MIDI ticks per quarter note

        track_id = file.read(4).decode( "ANSI" )
        if track_id != "MThd":
            # It is said that Mac midi files may have 128 extra
            # bytes prepended (i.e. a Mac BInary Header)
            # Just in case, skip bytes until 128 bytes have been ignored,
            # then read track_id again
            # I have not been able to verify this.
            file.read(128-4)
            track_id = file.read(4).decode( "ANSI" )
            if track_id != "MThd":
                raise ValueError("Midi file does not start with MThd header")
        header_len = int.from_bytes( file.read(4), "big" )

        if header_len < 6:
            raise ValueError(
                f"Midi file header MThd length ({header_len}) is smaller than 6 bytes"
                )
            # IF header is larger than 6 bytes, the extra bytes are ignored.

        header_data = file.read( header_len )

        # Format type 0: single MTrk chunk
        # Format type 1: two or more MTrk chunks to be merged
        # Format type 2: multiple MTrk chunks, each to be used separately
        format_type = int.from_bytes( header_data[0:2], "big" )

        # Get number of data chunks (track chunks) in the file
        number_of_chunks = int.from_bytes( header_data[2:4], "big" )

        # Get pulses per beat
        miditicks_per_quarter = int.from_bytes( header_data[4:6], "big" )

        if miditicks_per_quarter > 32767:
            raise ValueError("Midi SMPTE time codes not supported")

        return format_type, number_of_chunks, miditicks_per_quarter

    @property
    def format_type( self ):
        """
        Returns the MIDI format type as stored in the header of the MIDI file:
        0   single track MIDI file, should have only one track.
            To parse a type 0 file, use the MIdiFile object as iterator:
                for event in MidiFile("example.mid"):
                    process each event
        1   multitrack MIDI file, can have many tracks. During playback, the tracks
        are merged into one ordered sequence of events.
            To parse a type 1 file, proceed as with a type 0 file.
        2   each track behaves like a format 0 single track MIDI file. Merging
        tracks is not allowed. Track number "n" is parsed as follows:
            for event in MidiFile("format2file.mid").tracks[n]:
                .... process event...

        """
        return self._format_type

    @property
    def miditicks_per_quarter( self ):
        """
        Return the midi ticks per quarter note (also called pulses per beat)
        parameter in the MIDI header of the file.
        """
        return self._miditicks_per_quarter

    @property
    def filename( self ):
        """
        Return the file name of the MIDI file, with absolute path.
        """
        return self._filename

    @property
    def buffer_size( self ):
        """
        Return the buffer_size value. 0=tracks are buffered entirely in RAM.
        A number, for example buffer_size=100 means a buffer of 100 bytes is
        allocated per track to read the track data.

        This allows to read large MIDI files efficiently on microcontrollers with small RAM.
        """
        return self._buffer_size

    @property
    def reuse_event_object( self ):
        """
        Return the value of reuse_event_object.
        True: when iterating through a track or midi file, the same event object
        is returned over and over (this is an optimization recommended for Micropython)

        False: when iterating through a track or midi file, a different event
        object is returned each time (this is the typical Python behavior).
        """
        return self._reuse_event_object

    def _track_merger( self ):
        # Merges all tracks of a multitrack format 1 file

        # Iterate through each track, set up one iterator for each track
        # For this code to work, the track interator will always yield
        # a END_OF_TRACK event at the end of the track.
        play_tracks = [ track._track_parse_start() for track in self.tracks ]

        # Current miditicks keeps the time, in MIDI ticks, since start of track
        # of the last event returned
        current_miditicks = 0

        while True:
            # From all tracks, select the track with the next event, this is
            # the one with the lowest "current MIDI ticks time".
            next_track = min( play_tracks ) # Uses the __lt__ function of track

            # Get the current event of the selected track
            event = next_track.event

            # Adjust event miditicks to time difference with last event overall,
            # replacing delta time with last event in the event's track
            track_miditicks = next_track._get_current_miditicks()
            event.delta_miditicks = track_miditicks - current_miditicks

            # If end_of_track is seen, don't continue to process this track
            if event.status == END_OF_TRACK:
                # Delete the track from the list of tracks being processed
                track_index = play_tracks.index(next_track)
                del play_tracks[track_index]

                # If all tracks have ended, stop processing file
                if len(play_tracks) == 0:
                    # Yield only the last end_of_track found
                    yield event
                    # And stop iteration
                    return

                # Don't yield end of track events (except for the last track)
                continue

            yield event

            # Update current time, this is now the time of the event
            # just returned
            current_miditicks = track_miditicks

            # Get  the next event of the selected track.
            # This has to be done after the yield, because this might
            # overwrite the yielded message if reuse_event_object=True.
            next_track._track_parse_next()


    def __iter__( self ):
        """
        To get all the events of a format type 0 or format type 1 MIDI file,
        iterate through the MidiFile object, for example:
            for event in MidiFile("example.mid"):
                print(event)


        Events will be returned in ascending order in time. For format type 1
        multitrack files, all tracks are merged.

        The event.delta_us property is calculated as the
        time in microseconds between last and this event, taking into account both
        the set tempo meta events and the "MIDI ticks per quarter note"
        parameter in the MIDI file header. For type 1 files, all set tempo meta
        events may be in track 0 (as it is usually done), or they may occur in any track.

        For a multitrack file, event.delta_us is the time difference with the
        previous event, which may be in the same or a different track.

        For a format type 2 MIDI file, a single track must be selected, track
        numbers range from 0 to len(MidiFile.tracks)-1

            for event in MidiFile("example.mid").tracks[5]:
                ... process event ...

        When parsing a file format 2 track, then only the set tempo
        events of that track are processed to calculate delta_us.

        To process each event at the time due, a simple version could be:
            for event in MidiFile("example.mid"):
                time.sleep_us( event.delta_us )
                ... process the event ...

        To implement this function with time error compensation, use the
        MidiFile.play method.

        In all cases, only one end of track meta event is returned
        to the caller when the end of file is reached.
        Events beyond a end of track event are ignored.

        Exceptions:
        RuntimeError is raised if format type 2 is processed with this method.
        Use the MidiFile.tracks[n] to iterate through a single track.

        """
        # Check if there are tracks, there should be....
        if len(self.tracks) == 0:
            # No tracks in file, simulate an empty track
            # This will yield a single END_OF_TRACK event.
            return _process_events( iter([]),
                    self._miditicks_per_quarter,
                    self._reuse_event_object )

        # For format 2, iteration over the track to be played should be used...
        if self._format_type == 2 and len(self.tracks) > 1:
            raise RuntimeError(
                    "It's not possible to merge tracks of a MIDI format type 2 file")

        # If there is only one track present,
        # iterate through the track only, no track merge is needed.
        # This reduces CPU usage, in some cases by up to 15%.
        if len(self.tracks) == 1:
            return iter(self.tracks[0])

        # For multitrack file type 1 files, tracks must be merged.
        # If there is a file type 0 multitrack file,
        # treat it as multitrack file type 1 instead of raising an error.
        # A file type 0
        # file should really have only one track, according to the standard.
        return _process_events( self._track_merger(),
                    self._miditicks_per_quarter,
                    self._reuse_event_object )

    def length_us( self ):
        """
        Returns the length of the MidiFile in microseconds.

        Beware, on a slow microcontroller, calculating the length of
        a large MIDI file might take a several of seconds.
        This is due to the way MIDI files work, in order to
        get the playing length, this method needs to parse
        the entire file, compute and sum the time differences of all events.

        Exceptions:
        RuntimeError for format type 2 files. It is not possible to calculate the
        playing time of a format 2 file, since for format 2 files,
        the tracks are not meant to be merged.

        """
        # Returns the duration of playback time of the midi file microseconds

        # Start playing time at 0, in case there are no events
        playback_time_us = 0

        # Iterate through all events
        # The complete file must be processed to compute length
        # Open another instance of the file, so that the current process is not disturbed
        for event in MidiFile( self.filename ):
            playback_time_us += event.delta_us

        # Return the last time seen, or 0 if there were no events
        return playback_time_us

    def play( self, track_number=None ):
        """
        Iterate through the events of a MIDI file or a track,
        sleep until the event has to take place, and
        yield the event.

        Parameters
        track_number=None

        If track_number=None, and the MIDI file is format 0 or 1,
        play the complete file. Merge all tracks.

        If a track number is specified, then that track number is played. This
        is intended for use with format type 2 files, to play a certain track.

        Example:
            for event in MidiFile("example.mid").play():
                .... process the event ...
        The play function will wait the necessary time between iterations
        so that each event is yielded on time to be processed.

        This function compensates for the accumulated error in the
        processing of each event. Since sleep functions will sleep
        AT LEAST the time specified, normally the time slept will be longer. This
        means, for a long file of several thousand events, events may get ever later.
        This is noticeable especially of another thread or process is active, or
        if the processing of each event takes significant time.
        Even so, since play uses the sleep_us function, sometimes
        you may get the event a bit later than the correct time.

        For Micropython, time.sleep_us() is used. For CPython time.sleep() is used.

        """

        if track_number is None:
            midi_event_iterator = iter(self)
        else:
            midi_event_iterator = iter(self.tracks[track_number])

        playing_started_at = ticks_now_us()
        midi_time = 0

        for event in midi_event_iterator:
            midi_time += event.delta_us

            now = ticks_now_us()
            playing_time = ticks_diff_us( now, playing_started_at )

            wait_time = (midi_time - playing_time)
            if wait_time > 0:
                time_sleep_us( wait_time )
            yield event
