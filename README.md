# umidiparser - low footprint MIDI file parser for Micropython, CircuitPython and Python

## DESCRIPTION
This module reads MIDI files (SMF files) and gets all the MIDI events contained in the file. It also can return each event at the corresponding time.

Example:

´´´python
    import umidiparser
    import utime
    for event in umidiplay.MidiFile("example.mid").play():
        # .play will sleep, avoiding time drift, before returning the event on time
        # Process the event according to type
        if event.status == umidiplay.NOTE_ON:
            ... start the note with midi number event.note 
		on channel event.channel with event.velocity
        elif event.status == umidiplay.NOTE_OFF :
            ... stop the note event.note .
        elif event.status == umidiplay.PROGRAM_CHANGE:
            ... change midi program to event.program on event.channel ....
        else:
           # Show all events not processed
           print("other event", event )
´´´

This module does not contain a sound synthesizer, only the capabilities to
read and interpret a MIDI file.

Memory and CPU usage are optimized for a microcontroller with limited resources with Micropython or CircuitPython.

CPU and memory usage can be lowered even more by reusing the same MidiEvent over and over
during the process:

    for event in MidiFile("example.mid", reuse_event_object=True ):
        ... process event....

Normally, only a small portion of the file will be buffered in memory. The default is 100 bytes per track.
This allows to process a files
much larger than the available heap or RAM. See "CPU AND MEMORY" below.

If there is enough RAM available to buffer the complete file, you can use `for event in MidiFile("example.mid", buffer_size=0)`. This will load the complete file in RAM and uses a bit less of CPU for the parsing of each event.

This module will calculate the time between events, using the parameters and events available in the MIDI file (pulses per beat field in the file header and set tempo events).

## INSTALLATION

You can install with `pip install umidiparser`

You can install the package in the microcontroller, or just copy the umidiparser.py file.


## MIDI FILE COMPATIBILITY
The parser will parse MIDI files, also known as SMF files, with format type 0, 1 and 2. 
Running status events are
recognized. All standard MIDI channel events (note on, note off,
program change, control change, etc) and meta and sysex events (track name,
key signature, time signature, etc) recognized. This module is based on the MIDI file standard version 1.1

For multitrack file type 1 files, tracks are automatically
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

## CPU AND MEMORY (RAM) USAGE
Parsing on a ESP32 at 200 Mhz CPUclock with Micropython takes about
one millisecond per event, and even less if you use the reuse_event_object
of the MidiFile object. Times with CircuitPython on a RP2040 are similar.

With the reuse_event_object parameter set to true, CPU overhead should be
about 15% lower, and less heap is used.

On the ESP32 with MicroPython, parsing a MIDI file with buffer_size=100 and
reuse_event_object=True uses about 20kbytes of heap. Heap usage on a RP2040 (Raspberry Pi Pico) is similar. Each MIDI event parsed will
allocate and free less than 100 bytes of heap, so garbage collections are less
frequent if little RAM is available.
Most of the processing such as parsing event data into individual fields
is delayed until the information is really needed or asked for.

Frequently used methods have the @micropython.native decorator for speed.

## PORTABILITY
The code is optimized for Micropython or CircuitPython.
It also works with same functionality under regular Python (CPython).
This allows to develop or test on Linux, Mac or Windows and then port to
Micropython. 

## CLASSES
The starting point is the MidiFile object, allowing to iterate through
the events. Events are returned as MidiEvent objects, and the fields
of the event are visible as attributes of the MidiEvent.

## DEPENDENCIES
Imports *time* to compute time differences. MidiFile.play() will use the time.sleep or time.sleep_us function.

Imports *asyncio* for async version of MidiFile.play() 

Imports *sys* to get sys.name.implementation.


# Class MidiFile

`mf = MidiFile( filename, buffer_size=100, reuse_event_object=false)`

Parses a MIDI file, returning an iterator over the MIDI events in the file. You then can iterate through the events of the file, see the iterator and the *play* method.

It is also possible to get the tracks using the mf.track[] list and iterate through the events of one track only, useful for format type 2 files.

## MidiFile constructor parameters

### filename

The name of a MIDI file, usually a .mid, .kar or .rtx MIDI file.
The MIDI file will always be opened read only.

### buffer_size=100

The buffer size that will be allocated for each track. a value of zero means copy all tracks to RAM during processing.The default value is 100 bytes.

In order to process files larger than the available RAM,
*buffer_size=n* will allocate *n* bytes of buffer for
each track, and read each tracks in *n* byte portions during the
processing of the file, i.e. while iterating through the events. One file descriptor (one open file) will be used for each track, but the total RAM needed will be about *buffer_size* multiplied by the number of tracks of the MIDI file.

MIDI file format 0 files have only one track, so only one buffer will be allocated. 

A buffer size of less than 10 bytes will increase CPU overhead. A buffer size much larger than 100 will probably not give a
relevant performance advantage, unless the device where the file
resides is very slow.

If *buffer_size=0^, all tracks will be read to memory.
This will need as much RAM as the file size of a complete MIDI file.
In this case, the time needed to process each event will not depend on
file access and will be both faster and more dependable than using a
*buffer_size* different to 0, if the device where the file resides is slow.

The default value for *buffer_size* is 100 bytes.

* reuse_event_object=False

With the default value of False, for each step of the iteration a new MidiEvent is returned.
If you do:

            for event in MidiFile("example.mid"):
                ... process each event ...

then each iteration of the loop will yield a new MidiEvent object.
This is the normal and expected behavior for Python iterators.

However, if you if you have little RAM or need higher processing speed use:

    for event in MidiFile("example.mid", reuse_event_object=True):
         ... process each event ....

In this case, for each iteration of the loop, the same MidiEvent object is returned over over and over 
for each step of the loop, but overwritten with the new data. However, if you want to store an event
for later use,  you'll have to make a deep copy using `event.copy`.

All combinations of *reuse_event_object* and *buffer_size* are valid.

Exceptions raised:

The file must start with a standard MIDI file header (MThd), if not, a
ValueError is raised.
The MIDI header chunk must be at least 6 bytes long, or a ValueError
is raised.
ValueError is raised if no header present, or too short.
ValueError is raised if the header contains SMPTE time codes (not supported).
Chunks after the header that are not tracks identified with the MTrk header are ignored.


## MidiFile Methods

### Iterating through the events of a MIDI file

To get all the events of a format type 0 or format type 1 MIDI file,
iterate through the MidiFile object, for example:
    
    import umidiparser
    for event in MidiFile("example.mid"):
        print(event)


Events will be returned in ascending order in time. For format type 1
multitrack files, all tracks are merged.

The *event.delta_us* property is calculated as the
time in microseconds between last and this event, taking into account both
the set tempo meta events and the "MIDI ticks per quarter note" (also known as "pulses per beat")
parameter in the MIDI file header. For type 1 files, all set tempo meta
events may be in track 0 (as it is usually done), or they may occur in any track.

For a multitrack file, *event.delta_us^ is the time difference with the
previous event, which may be in the same or a different track.

To get each event at the proper time of the event, use the 
*MidiFile.play* method. This method compensates for the delays during processing.

In all cases, only one end of track meta event is returned
to the caller when the end of file is reached.
Events beyond an end of track event are ignored.

Exceptions:

A *RuntimeError* is raised if format type 2 is processed with this method.


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

For Micropython, *time.sleep_us()* is used. For CircuitPython and CPython *time.sleep()* is used. 

There is also a asyncio version of MidiFile.play() available:

	async for event in MidiFile("example.mid").play():
		... process the event ...

This will work exactly like the normal for, except it will pause for the next event with *await asyncio.sleep()* for CPython or *asyncio.sleep_ms()* for MicroPython an CircuitPython. 

### length_us

Computes and returns the length of the MidiFile in microseconds.

Be aware that on a microcontroller, calculating the length of
a large MIDI file might take a several seconds.
This is due to the way MIDI files work. In order to
get the playing length, this method needs to parse
the entire file, compute and add the time differences of all events.

Exceptions:

*RuntimeError* for format type 2 files. It is not possible to calculate the
playing time of a format 2 file, since for format 2 files,
the tracks are not meant to be merged.

       

## MidiFile properties

The properties cannot be changed, they are set with the MidiFile constructor.

### buffer_size

Returns the *buffer_size value*. 
        
### filename

Returns the file name of the MIDI file. 
        
### format_type

Returns the MIDI format type as stored in the header of the MIDI file:

* format_type 0 files are single track MIDI files.
To parse a type 0 file, use the MIdiFile object as iterator:

    for event in MidiFile("example.mid"):
        ...process each event

* format_type 1 files are multitrack MIDI files. During playback, this module will merge the tracks
into an ordered sequence of events.

To parse a type 1 file, use the same code as with a type 0 file. 

* format_type 2 files are multitrack files where each track behaves like a format 0 single track MIDI file. Merging
tracks is not allowed. Track number "n" can be  parsed as follows:

    for event in MidiFile("format2file.mid").tracks[n]:
         .... process event...

Or also:

    For event in MidiFile("format2file.mid").tracks[n].play():
         .... process event...

        
### miditicks_per_quarter

Return the MIDI ticks per quarter note (also called pulses per beat) field of the MIDI file header.
        
        
### reuse_event_object

Return the value of the reuse_event_object property.

## MidiFile instance variables
### tracks
List of MidiTrack objects, one for each track.

# Class MidiTrack
The MidiFile object exposes the list of tracks.

## Methods


# Class MidiEvent

Represents a parsed MIDI event. You get MidiEvent objects iterating through a MidiFile.

## Properties available for all events

### status

This is the event type, such as note on, note off,
set tempo, end of track, sysex. You can compare event.status
with the constants umidiparser.NOTE_ON, umidiparser.NOTE_OFF,
umidiparser.PROGRAM_CHANGE, umidiparser.LYRICS, umidiparser.SYSEX, etc.

Available for all events types. 

Example:

    if event.status == umidiparser.NOTE_OFF:
        .... process note off event ...
     elif event.status == umidiparser.KEY_SIGNATURE:
          ... process key signature meta event ...

Possible values are constants in umidiparser:
* Channel messages
- NOTE_OFF
- NOTE_ON
- POLYTOUCH
- CONTROL_CHANGE
- PROGRAM_CHANGE
- AFTERTOUCH
- PITCHWHEEL

* Meta messages 
- SEQUENCE_NUMBER
- TEXT
- COPYRIGHT
- TRACK_NAME
- INSTRUMENT_NAME
- LYRICS
- MARKER
- CUE_MARKER
- PROGRAM_NAME
- DEVICE_NAME
- CHANNEL_PREFIX
- MIDI_PORT
- END_OF_TRACK
- SET_TEMPO
- SMPTE_OFFSET
- TIME_SIGNATURE
- KEY_SIGNATURE
- SEQUENCER_SPECIFIC

 * Sysex/escape events
 - SYSEX
 - ESCAPE



### delta_us

Time in microseconds since the last event for this
event to start. delta_us is calculated using the delta in MIDI ticks, the pulses per quarter in the MIDI file header and the set tempo events in the file, using integer arithmetic to avoid floating point use.

### delta_miditicks

Difference, in MIDI ticks (MIDI pulses) between last event
and this event. This number is also known as "delta time" of the event.
For single track files, the time difference is with the previous event
of the same track. When parsing multitrack files, tracks are merged and this
time is set during playback to the time difference with the previous event, which may or may not be in the same track.

### data 
Contains the raw event data.


## Event specific properties

For each type of event, only the applicable properties are enabled.
The following list shows the event status and properties
that you can get.

For example: for a note_on event, event.status is umidiparser.NOTE_ON
and the properties event.note, event.channel, and event.velocity return the 
values of the event.

Attributes that are not available throw an AttributeError on access.

## MIDI channel event specific properties

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
    - value (int)
* PROGRAM_CHANGE (midi event status byte=0xc0 to 0xcf)
    - channel (int)
    - program (int)
* AFTERTOUCH (midi event status byte=0xd0 to 0xdf)
    - channel (int)
    - value (int)
* PITCHWHEEL (midi event status byte=0xe0 to 0xef)
    - channel (int)
    - pitch (int)

## Meta and Sysex event specific properties
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

Text strings are decoded as ASCII. Non ASCII characters are shown in hexa i.e. \x80.

* SYSEX  0xf0
    - data (memoryview)
* ESCAPE  0xf7
    - data (memoryview)

## MidiEvent methods

### copy()

Returns a deep copy (a complete independent copy) of the event as a new object.

This can be useful to get a copy of the event in case of using
the reuse_event_object=True option in the MidiFile.

Example 1: if you need a list of all MidiEvents
in a file, then either use:

    event_list = [event.copy for event in MidiFile("example.mid",
        reuse_event_object=True) ]

or use:

    event_list = [ event for event in MidiFile("example.mid") ]
        
### is_channel()

Returns True if this is a channel event such as note on, program change
or pitchwheel. 

Returns False for meta events, Sysex or Escape events.

### is_meta()

Returns True if this is a Meta event, such as
lyrics, set tempo or key signature.

Returns False if this is a MIDI channel event,
or a Sysex or Escape event.

### str(event) 
Will translate the event information to a string, for example:

    print(event)    
    event_as_a_string = str(event)

Returns a string with a description of the MidiEvent, starting
with the event name in lowercase (note_on, note_off, pitchwheel, set_tempo,
end_of_track, etc), delta time in MIDI ticks, delta time in microseconds,
first few bytes of the raw data for meta events, and all properties
that are allowed for the event type. For example, a "note on" event might
be shown as:

"note_on delta[miditicks]=10 delta[usec]=9500 note=60 velocity=64 channel=5"

The order of the properties in the string may vary. 


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

The main purpose is to retrieve message data for sysex and escape events. Also, you can decode text and name fields, such as lyrics, with a encoding better suited for the file, if available.
        
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

Returns the *name* data field for certain meta events.

name property is available for:  TRACK_NAME INSTRUMENT_NAME PROGRAM_NAME DEVICE_NAME

See text property for description of text decoding.

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
       
### sub_frames

Returns the sub frames for the SMPTE_OFFSET meta message,
usually from 0 to 59.
        
### tempo

Returns the tempo in microseconds per quarter beat
for a SET_TEMPO meta event.
This module interprets the tempo event before returning it, so
the following events returned will have their *delta_us* property
calculated with the new tempo value.

### text

Returns the text for a meta events.

text property is available for:  TEXT COPYRIGHT LYRICS MARKER CUE_MARKER

Both event.text and event.name decode the data with ASCII. Unmapped characters are shown in hexadecimal, for example \x0d

There are many MIDI files where text and name fields are encoded 
with other encodings. The encoding used is not stored in the file.
         
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

## Change log for version 1.1 and 1.2

Added CircuitPython compatibility
Removed use of os.path.abspath, does not exist in micropython/circuitpython
Renamed time functions "ticks_now_us", "ticks_diff_us" to "time_now_us", "time_diff_us"
Changed decode from meta event data for compatibility with all Python versions, now only ascii is decoded.
New method MidiTrack.play plays one single track.
Corrected possible error if playing open file again.
Added event.is_channel() to test for channel events.
Allow MidiFile.play() used in async for (with asyncio.sleep instead of sleep). Requires asyncio.
Play funcion computes event.timestamp_us for each event


## AUTHOR
Hermann Paul von Borries

## LICENSE
MIT, Copyright (c) 2022 Hermann Paul von Borries


        


        
