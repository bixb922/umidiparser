# umidiparser - MIDI file parser for Micropython

## NAME
umidiparser

## AUTHOR
Hermann Paul von Borries

## LICENSE
MIT, Copyright (c) Hermann Paul von Borries

## INSTALLATION
Copy umidiparser.py to your device.

## DESCRIPTION
This module allows to parse midi files.
This module does not contain a sound synthesizer, only the capabilities to
read and interpret a midi file.
Example:

    import umidiparser
    import utime
    for event in umidiplay.MidiFile("example.mid"):
        utime.sleep\_us( event.delta\_us )
        if event.status == umidiplay.NOTE\_ON:
            ... start the note event.note on event.channel with event.velocity
        elif event.status == umidiplay.NOTE\_OFF :
            ... stop the note event.note stop to sound ...
        elif event.status == umidiplay.PROGRAM\_CHANGE:
            ... change midi program to event.program on event.channel ....
        else:
           print("other event", event )

Memory and CPU usage is optimized for a microcontroller with limited resources and Micropython. 
CPU usage can be lowered even more by reusing the same MidiEvent over and over
during the process, using the same event object over and over again:
    for event in MidiFile("example.mid", reuse_event_object=True ):
        ... process event....

Normally the complete midi file will be buffered in RAM when opening the
file. If RAM is scarce or may be fragmented, use:

    for event in MidiFile("example.mid", buffer_size=100 ):
        .... process event...

This will allocate *buffer\_size* bytes as a buffer for each track in the
midi file, open one file descriptor for each track and then read the file
piecemeal. This will use slightly (about 10%) more CPU, but RAM usage
is limited to the *buffer\_size* bytes per track, and you can process a files
much larger than the available heap or RAM.

## MIDI FILE COMPATIBILITY
The parser will parse midi files format type 0, 1 and 2. Running status events are
recognized. All standard MIDI channel events (note on, note off,
program change, control change, etc) and meta and sysex events (track name,
key signature, time signature, etc) recognized.

The set tempo meta events and the "pulses per beat"
(aka "midi ticks per quarter note")
field of the midi file header are used to calculate the time between events.
The time is calculated as integer rounded to the nearest microsecond,
because floating point processing may be slow on some microcontrollers.
The Micropython function *utime.sleep\_us( event.delta\_us )* can be used to sleep between events.
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

## CPU AND RAM USAGE
Parsing on a ESP32 WROOM with Micropython takes about
one millisecond, and even less if you use the reuse_event_object
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

## PORTABILITY
The code is optimized for Micropython, but
also works with same functionality under regular Python (CPython).
This allows to develop or test on Linux, Mac or Windows and then port to
Micropython. Not tested on CircuitPython so far.

## CLASSES
The starting point is the MidiFile object, allowing to iterate through
the events. Events are returned as MidiEvent objects, and the fields
of the event are visible as attributes of the MidiEvent.
The tracks of a MIDI file are also
visible as MidiTrack objects, and each track can be played individually.

## DEPENDENCIES
Imports *time/utime*. Provides a wrapper to work with CPython "import time".
Imports *os* to get the absolute path of the MIDI file.


# Class MidiFile

Parses a MIDI file.
Once initialized, you can iterate through the events of the file or
through the events of a certain track, see the iterator and the *play* method.


## MidiFile Methods

### Iterating through the events of a MIDI file

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

For a format type 2 MIDI file, a single track must be selected, see MidiTrack object.

To process each event at the time due, a simple version you could use:
    for event in MidiFile("example.mid"):
        time.sleep_us( event.delta_us )
        ... process the event ...

To implement this function with time error compensation, use the
MidiFile.play method.

In all cases, only one end of track meta event is returned
to the caller when the end of file is reached.
Events beyond an end of track event are ignored.

Exceptions:

RuntimeError is raised if format type 2 is processed with this method.
Use the MidiFile.tracks[n] to iterate through a single track.

## MidiFile methods

### play
Iterate through the events of a MIDI file or a track,
sleep until the event has to take place, and
yield the event.

Example:
    for event in MidiFile("example.mid").play():
         .... process the event ...
The play function will wait the necessary time between iterations
so that each event is yielded on time to be processed.

This function compensates for the accumulated error in the
processing of each event. Since sleep functions will sleep
AT LEAST the time specified, normally the time slept will be longer. This
means, for a long file of several thousand events, events may get ever later.
This is noticeable especially 
if the processing of each event takes significant time.
Even so, since play uses the sleep_us function, sometimes
you may get the event a bit later than the correct time.

For Micropython, time.sleep_us() is used. For CPython time.sleep() is used.
#### MidiFile play arameters
###### track_number=None

If track_number=None, and the MIDI file is format 0 or 1,
play the complete file. Merge all tracks.

If a track number is specified, then that track number is played. This
is intended for use with format type 2 files, to play a certain track. Format 2 Midi files are not very common.


## MidiFile properties

### buffer_size

Return the buffer_size value. 0=tracks are buffered entirely in RAM.
A number, for example buffer_size=100 means a buffer of 100 bytes is
allocated per track to read the track data.

This option allows to read large MIDI files efficiently on microcontrollers with small RAM.
        
### filename

Return the file name of the MIDI file, with absolute path.
        
### format_type

Returns the MIDI format type as stored in the header of the MIDI file:
* 0   single track MIDI file, should have only one track.
To parse a type 0 file, use the MIdiFile object as iterator:
    for event in MidiFile("example.mid"):
        ...process each event
* 1   multitrack MIDI file, can have many tracks. During playback, the tracks
are merged into one ordered sequence of events.
To parse a type 1 file, proceed as with a type 0 file.
* 2   each track behaves like a format 0 single track MIDI file. Merging
tracks is not allowed. Track number "n" can be  parsed as follows:
    for event in MidiFile("format2file.mid").tracks[n]:
         .... process event...

        
### length\_us

Calculates and returns the length of the MidiFile in microseconds.

Be aware that on a slow microcontroller, calculating the length of
a large MIDI file might take a several of seconds.
This is due to the way MIDI files work, in order to
get the playing length, this method needs to parse
the entire file, compute and add the time differences of all events.

Exceptions:
_RuntimeError_ for format type 2 files. It is not possible to calculate the
playing time of a format 2 file, since for format 2 files,
the tracks are not meant to be merged.

        
### miditicks_per_quarter

Return the MIDI ticks per quarter note (also called pulses per beat)
parameter of the MIDI header of the file.
        
        
### reuse_event_object

Return the value of reuse_event_object, with the same value specified in the constructor.
* True: when iterating through a track or midi file, the same event object
is returned over and over (this is an optimization recommended for Micropython)
        
* False: when iterating through a track or midi file, a different event
object is returned each time (this is the typical Python behavior).
        
# Class MidiEvent

Represents a parsed midi event.

## Properties available for all events

### event.status
This is the event type, such as note on, note off,
set tempo, end of track, sysex. You can compare event.status
with the constants umidiparser.NOTE_ON, umidiparser.NOTE_OFF,
umidiparser.PROGRAM_CHANGE, etc.

### event.delta_miditicks
difference, in midi ticks or pulses between last event
and this event, also known as "delta time" of the event.
For single track files, the time difference is with the previous event
of the same track. When parsing multitrack files, tracks are merged and this
time is set during playback to the time difference with the previous event in any track.

### event.delta\_us
time in microseconds since the last event for this
event to start. For example, you might use sleep\_us( event.delta\_us ) to
sleep the appropriate time for the event to start.

### event.data 
contains the raw event data.

### str(event) 
Will translate the event information to a string, for example:
    print(event)
    
    event_as_a_string = str(event)
Returns a string with a description of the MidiEvent, starting
with tne event name in lowercase (note_on, note_off, pitchwheel, set_tempo,
end_of_track, etc), delta time in midi ticks, delta time in microseconds,
first few bytes of the raw data, and all properties
that are allowed for the event type. For example, a "note on" event might
be shown as:
"note_on delta[miditicks]=10 delta[usec]=9500 note=60 velocity=64 channel=5"

The order of the properties in the string may vary.
 

## Properties by event type

For each type of event, only the applicable properties are enabled.
The following list shows the event status and properties
that you can get.

For example: for a note_on event, event.status is umidiparser.NOTE_ON
and event.note, event.channel, and event.velocity have the corresponding
values. But for a program change event, event.velocity will not be available.

Attributes that are not allowed generate an AttributeError on access.

## Properties for MIDI channel events
* NOTE_OFF (midi event status byte=0x80 to 0x8f)
    - channel (int)
    - note (int)
    - velocity (int)
* NOTE_ON (midi event status byte=0x90 to 0x9f)
    - channel (int)
    - note (int)
    - velocity (int)
* POLYTOUCH (midi event status byte=0xa0 to 0xaf)
    - channel (int)
    - note (int)
    - value (int)
* CONTROL_CHANGE (midi event status byte=0xb0 to 0xbf)
    - channel (int)
    - control (int)
    - svalue (int)
* PROGRAM_CHANGE (midi event status byte=0xc0 to 0xcf)
    - channel (int)
    - program (int)
* AFTERTOUCH (midi event status byte=0xd0 to 0xdf)
    - channel (int)
    - value (int)
* PITCHWHEEL (midi event status byte=0xe0 to 0xef)
    - channel (int)
    - pitch (int)

## Properties for Meta and Sysex events
* SEQUENCE_NUMBER (midi meta 0xff 0x00)
    - number (int)
* TEXT (midi meta 0xff 0x01)
    - text (str)
* COPYRIGHT (midi meta 0xff 0x02)
    - text (str)
* TRACK_NAME (midi meta 0xff 0x03)
    - name (str)
* INSTRUMENT_NAME (midi meta 0xff 0x04)
    - name (str)
* LYRICS (midi meta 0xff 0x05)
    - text (str)
* MARKER (midi meta 0xff 0x06)
    - text (str)
* CUE_MARKER (midi meta 0xff 0x07)
    - text (str)
* PROGRAM_NAME (midi meta 0xff 0x08)
    - name (str)
* DEVICE_NAME (midi meta 0xff 0x09)
    - name (str)
* CHANNEL_PREFIX (midi meta 0xff 0x20)
    - channel (int)
* MIDI_PORT (midi meta 0xff 0x21)
    - port (int)
* END_OF_TRACK (midi meta 0xff 0x2f)
    - no event specific attributes available
* SET_TEMPO (midi meta 0xff 0x51)
    - tempo (int)
* SMPTE_OFFSET (midi meta 0xff 0x54)
    - frame_rate (int)
    - frames (int)
    - hours (int)
    - minutes (int)
    - seconds (int)
    - sub_frames (int)
* TIME_SIGNATURE (midi meta 0xff 0x58)
    - clocks_per_click (int)
    - denominator (int)
    - notated_32nd_notes_per_beat (int)
    - numerator (int)
* KEY_SIGNATURE (midi meta 0xff 0x59)
    - key (str)
* SEQUENCER_SPECIFIC (midi meta 0xff 0x7f)
    - data (memoryview)

* SYSEX  0xf0
    - data (memoryview)
* ESCAPE  0xf7
    - data (memoryview)

## MidiEvent methods
### copy

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
        
### is_meta

Returns True if this is a Meta event, such as
lyrics, set tempo or key signature.

Returns False if this is a MIDI channel event,
or a Sysex or Escape event.
        


## MidiEvent properties
### channel

Returns the channel number for the event, 0-15.

channel property is available for:  NOTE_OFF NOTE_ON
POLYTOUCH CONTROL_CHANGE PROGRAM_CHANGE AFTERTOUCH
CHANNEL_PREFIX
        
### clocks_per_click

Returns the clocks_per_click for the TIME_SIGNATURE meta messages, 0-255.
        
### control

Returns the value for the controller 0-127 for a CONTROL_CHANGE event.
        
### data

Returns the raw data for the underlying message, with no transofrmations,
as a memoryview, without the event status byte or meta prefix.

For midi channel events, the length is either 1 or 2 bytes
according to the event type, for example a "note on" event always
has 2 bytes of data.
For a meta or sysex event, "data" contains the payload of the message,
that is, without meta prefix and length.
For sysex and escape events, the status (0xf0, xf7) is not included.

The main purpose is to retrieve message data for sysex and escape events.
        
### denominator

Returns the denominator for the TIME_SIGNATURE meta messages, 0-255.
        
### frame_rate

Returns the frame for the SMPTE_OFFSET meta messages,
which can be 24, 25, 29.97 or 30.

An invalid value in the MIDI file will raise a *IndexError*
        
### frames

Returns the frames for the SMPTE_OFFSET meta message,
usually from 0 to 255.
        
### hours

Returns the hour for the SMPTE_OFFSET meta message,
usually from 0 to 23.
        
### key

Returns the key, as string, for a KEY_SIGNATURE meta event.
  
For mayor keys:
C, D, E, F, G, A, B, C#, F#, Cb, Db, Eb, Gb, Ab

For minor keys:
Cm, Dm, Em, Fm, Gm, Am, Bm, C#m, F#m, Cbm, Dbm, Ebm, Gbm, Abm

If the midi message contains a value out of range, a *ValueError*
 is raised. The raw data can be accessed with the data property.
        
### minutes

Returns the minutes for the SMPTE_OFFSET meta message,
usually from 0 to 59.
        
### name

Returns the text for a meta events.

name property is available for:  TRACK_NAME INSTRUMENT_NAME PROGRAM_NAME DEVICE_NAME

See text property for description of text conversion.

The raw data can be retrieved using the data property.
        
### notated_32nd_notes_per_beat

Returns the notated_32nd_notes_per_beat for the TIME_SIGNATURE meta messages,
0-255.
        
### note

Returns the note number for the event, usually 0-127.

note property available for:  NOTE_OFF NOTE_ON POLYTOUCH
        
### number

Returns number of a SEQUENCE_NUMBER meta event.
Values range from 0 to 2**24.
        
### numerator

Returns the numerator for the TIME_SIGNATURE meta messages, 0-255.
        
### pitch

Returns the pitch for a PITCHWHEEL midi channel event.

-8192 is the lowest value possible, 0 (zero) means "no pitch bend"
and 8191 is the highest value possible.
        
### port

Returns the port number  0-256 for a meta MIDI_PORT message
        
### program

Returns the program number 0-127 for a PROGRAM_CHANGE event.
        
### seconds

Returns the seconds for the SMPTE_OFFSET meta message,
usually from 0 to 59.
        
### status

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

Possible values with hexdecimal equivalent, all names are global constants in this module e.g. umidiparser.NOTE_OFF
* Channel messages
- NOTE_OFF 0x80
- NOTE_ON 0x90
- POLYTOUCH 0xa0
- CONTROL_CHANGE 0xb0
- PROGRAM_CHANGE 0xc0
- AFTERTOUCH 0xd0
- PITCHWHEEL 0xe0

* Meta messages (all with prefix 0xff)
- SEQUENCE_NUMBER 0x00
- TEXT 0x01
- COPYRIGHT 0x02
- TRACK_NAME 0x03
- INSTRUMENT_NAME 0x04
- LYRICS 0x05
- MARKER 0x06
- CUE_MARKER 0x07
- PROGRAM_NAME 0x08
- DEVICE_NAME 0x09
- CHANNEL_PREFIX 0x20
- MIDI_PORT 0x21
- END_OF_TRACK 0x2f
- SET_TEMPO 0x51
- SMPTE_OFFSET 0x54
- TIME_SIGNATURE 0x58
- KEY_SIGNATURE 0x59
- SEQUENCER_SPECIFIC 0x7f

 * Sysex/escape events
 - SYSEX 0xf0
 - ESCAPE 0xf7

## Meta event properties        
### sub_frames

Returns the sub frames for the SMPTE_OFFSET meta message,
usually from 0 to 59.
        
### tempo

Returns the tempo (0 to 2**32 microseconds per quarter beat)
for a SET_TEMPO meta event.
This module interprets the tempo event before returning it, so
the following events returned will have their delta\_us property
calculated with the new tempo value.

        
### text

Returns the text for a meta events.

text property is available for:  TEXT COPYRIGHT LYRICS MARKER CUE_MARKER

In MIDI files, text is stored as "extended ASCII", this is
decoded with the iso8859_1 encoding.

The raw data can be retrieved using the data property.
        
### to_midi

Returns the event as bytes, in a format that allows sending the
data to a MIDI controller.

to_midi will raise AttributeError if the event is for MIDI meta messages, these
occur in MIDI files and are not normally sent to MIDI controllers.
        
### value

Returns the the value in the event.

value property available for:  AFTERTOUCH, CONTROL_CHANGE, POLYTOUCH
        
### velocity

Returns the velocity for the event, usually 0-127.

velocity property available for:  NOTE_OFF NOTE_ON
        
