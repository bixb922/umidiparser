
Python: module umidiparser




|  |  |
| --- | --- |
| 
 **umidiparser** | [index](.)[/Users/hermannvonborries/Library/CloudStorage/GoogleDrive-hermannvb@gmail.com/My Drive/cosas/micropython/umidiparser/umidiparser.py](file:/Users/hermannvonborries/Library/CloudStorage/GoogleDrive-hermannvb%40gmail.com/My%20Drive/cosas/micropython/umidiparser/umidiparser.py) |






|  |
| --- |
| 
**Modules** |
|        |  | 

|  |  |  |  |
| --- | --- | --- | --- |
| [os](os.html) | [time](time.html) |  |  |

 |




|  |
| --- |
| 
**Classes** |
|        |  | 
[builtins.object](builtins.html#object)


[MidiEvent](umidiparser.html#MidiEvent)
[MidiFile](umidiparser.html#MidiFile)
[MidiTrack](umidiparser.html#MidiTrack)






|  |
| --- |
| 
class **MidiEvent**([builtins.object](builtins.html#object)) |
|     | Represents a parsed midi event.
 
PROPERTIES AVAILABLE FOR ALL EVENTS
 
event.status: this is the event type, such as note on, note off,
set tempo, end of track, sysex. You can compare event.status
with the constants umidiparser.NOTE\_ON, umidiparser.NOTE\_OFF,
umidiparser.PROGRAM\_CHANGE, etc.
 
event.delta\_miditicks: difference, in midi ticks or pulses between last event
and this event, also known as "delta time" of the event.
For single track files, the time difference is with the previous event
of the same track. When parsing multitrack files, tracks are merged and this
time is set during playback to the time difference with the previous event in any track.
 
event.delta\_us: time in microseconds since the last event for this
event to start. For example, you might use sleep\_us( event.delta\_us ) to
sleep the appropiate time for the event to start.
 
event.data contains the raw event data.
 
str(event) will a string like this:
 
 
PROPERTIES BY EVENT TYPE
 
For each type of event, only the applicable properties are enabled.
The following list shows the event status and properties
that you can get.
 
For example: for a note\_on event, event.status is umidiparser.NOTE\_ON
and event.note, event.channel, and event.velocity have the corresponding
values. But for a program change event, event.velocity will not be available.
 
Attributes that are not allowed generate an AttributeError on access.
 
PROPERTIES FOR MIDI CHANNEL EVENTS
NOTE\_OFF /midi event status byte=0x80 to 0x8f)
    channel (int)
    note (int)
    velocity (int)
NOTE\_ON (midi event status byte=0x90 to 0x9f)
    channel (int)
    note (int)
    velocity (int)
POLYTOUCH (midi event status byte=0xa0 to 0xaf)
    channel (int)
    note (int)
    value (int)
CONTROL\_CHANGE (midi event status byte=0xb0 to 0xbf)
    channel (int)
    control (int)
    value (int)
PROGRAM\_CHANGE (midi event status byte=0xc0 to 0xcf)
    channel (int)
    program (int)
AFTERTOUCH (midi event status byte=0xd0 to 0xdf)
    channel (int)
    value (int)
PITCHWHEEL (midi event status byte=0xe0 to 0xef)
    channel (int)
    pitch (int)
 
PROPERTIES FOR META AND SYSEX EVENTS
SEQUENCE\_NUMBER (midi meta 0xff 0x00)
    number (int)
TEXT (midi meta 0xff 0x01)
    text (str)
COPYRIGHT (midi meta 0xff 0x02)
    text (str)
TRACK\_NAME (midi meta 0xff 0x03)
    name (str)
INSTRUMENT\_NAME (midi meta 0xff 0x04)
    name (str)
LYRICS (midi meta 0xff 0x05)
    text (str)
MARKER (midi meta 0xff 0x06)
    text (str)
CUE\_MARKER (midi meta 0xff 0x07)
    text (str)
PROGRAM\_NAME (midi meta 0xff 0x08)
    name (str)
DEVICE\_NAME (midi meta 0xff 0x09)
    name (str)
CHANNEL\_PREFIX (midi meta 0xff 0x20)
    channel (int)
MIDI\_PORT (midi meta 0xff 0x21)
    port (int)
END\_OF\_TRACK (midi meta 0xff 0x2f)
    no event specific attributes available
SET\_TEMPO (midi meta 0xff 0x51)
    tempo (int)
SMPTE\_OFFSET (midi meta 0xff 0x54)
    frame\_rate (int)
    frames (int)
    hours (int)
    minutes (int)
    seconds (int)
    sub\_frames (int)
TIME\_SIGNATURE (midi meta 0xff 0x58)
    clocks\_per\_click (int)
    denominator (int)
    notated\_32nd\_notes\_per\_beat (int)
    numerator (int)
KEY\_SIGNATURE (midi meta 0xff 0x59)
    key (str)
SEQUENCER\_SPECIFIC (midi meta 0xff 0x7f)
    data (memoryview)
 
SYSEX  0xf0
    data (memoryview)
ESCAPE  0xf7
    data (memoryview)  |
|  | Methods defined here:
**\_\_init\_\_**(self)Initializes [MidiEvent](#MidiEvent), all instances are assigned None as value,
this is. This method is used internally by MidiParser.
 
Usually you will not need to create an instance of [MidiEvent](#MidiEvent),
[MidiEvent](#MidiEvent) objects are returned by iterating over the [MidiFile](#MidiFile)
[object](builtins.html#object).
**\_\_str\_\_**(self)Standard method to translate the event information to a string,
for example:
    print(event)
    or
    event\_as\_a\_string = str(event)
Returns a string with a description of the [MidiEvent](#MidiEvent), starting
with tne event name in lowercase (note\_on, note\_off, pitchwheel, set\_tempo,
end\_of\_track, etc), delta time in midi ticks, delta time in microseconds,
first few bytes of the raw data, and all properties
that are allowed for the event type. For example, a "note on" event might
be shown as:
"note\_on delta[miditicks]=10 delta[usec]=9500 note=60 velocity=64 channel=5"
 
The order of the properties in the string may vary.
**copy**(self)Returns a deep copy (a complete independent copy) of the event.
All values are equal to the original event.
 
This can be useful to get a copy of the event in case of using
the reuse\_event\_object=True option in the [MidiFile](#MidiFile).
 
Example 1: if you need a list of all MidiEvents
in a file, then either use:
    event\_list = [ event for event in [MidiFile](#MidiFile)("example.mid") ]
or use:
    event\_list = [event.copy for event in [MidiFile](#MidiFile)("example.mid",
                  reuse\_event\_object=True) ]
 
The following code will give an unexpected result, because all
elements in the list will be equal to the last event of the file:
    event\_list = [event for event in [MidiFile](#MidiFile)("example.mid",
                  reuse\_event\_object=True) ]
**is\_meta**(self)Returns True if this is a Meta event, such as
lyrics, set tempo or key signature.
Returns False if this is a MIDI channel event,
or a Sysex or Escape event.
**to\_midi**(self)Returns the event as bytes, in a format that allows sending the
data to a MIDI controller.
 
to\_midi will raise AttributeError if the event is for MIDI meta messages, these
occur in MIDI files and are not normally sent to MIDI controllers.


---


Readonly properties defined here:
**channel**
Returns the channel number for the event, 0-15.
 
channel property available for:  NOTE\_OFF NOTE\_ON
POLYTOUCH CONTROL\_CHANGE PROGRAM\_CHANGE AFTERTOUCH
CHANNEL\_PREFIX

**clocks\_per\_click**
Returns the clocks\_per\_click for the TIME\_SIGNATURE meta messages, 0-255.

**control**
Returns the value for the controller 0-127 for a CONTROL\_CHANGE event.

**data**
Returns the raw data for the underlying message, with no transofrmations,
as a memoryview, without the event status byte or meta prefix.
 
For midi channel events, the length is either 1 or 2 bytes
according to the event type, for example a "note on" event always
has 2 bytes of data.
For a meta or sysex event, "data" contains the payload of the message,
that is, without meta prefix and length.
For sysex and escape events, the status (0xf0, xf7) is not included.
 
The main purpose is to retrieve message data for sysex and escape events.

**denominator**
Returns the denominator for the TIME\_SIGNATURE meta messages, 0-255.

**frame\_rate**
Returns the frame for the SMPTE\_OFFSET meta messages,
which can be 24, 25, 29.97 or 30.
 
An invalid value in the MIDI file will raise a IndexError

**frames**
Returns the frames for the SMPTE\_OFFSET meta message,
usually from 0 to 255.

**hours**
Returns the hour for the SMPTE\_OFFSET meta message,
usually from 0 to 23.

**key**
Returns the key, as str, for a KEY\_SIGNATURE meta event.
Key names are "american" key names.
 
For mayor keys:
C, D, E, F, G, A, B, C#, F#, Cb, Db, Eb, Gb, Ab
 
For minor keys:
Cm, Dm, Em, Fm, Gm, Am, Bm, C#m, F#m, Cbm, Dbm, Ebm, Gbm, Abm
 
If the midi message contains a value out of range, a ValueError
is raised. The raw data can be read with the data property.

**minutes**
Returns the minutes for the SMPTE\_OFFSET meta message,
usually from 0 to 59.

**name**
Returns the text for a meta events.
 
name property available for:  TRACK\_NAME INSTRUMENT\_NAME PROGRAM\_NAME DEVICE\_NAME
 
See text property for description of text conversion.
 
The raw data can be retrieved using the data property.

**notated\_32nd\_notes\_per\_beat**
Returns the notated\_32nd\_notes\_per\_beat for the TIME\_SIGNATURE meta messages,
0-255.

**note**
Returns the note number for the event, usually 0-127.
 
note property available for:  NOTE\_OFF NOTE\_ON POLYTOUCH

**number**
Returns numbef for a SEQUENCE\_NUMBER meta event.
Values range from 0 to 2\*\*24.

**numerator**
Returns the numerator for the TIME\_SIGNATURE meta messages, 0-255.

**pitch**
Returns the pitch for a PITCHWHEEL midi channel event.
 
-8192 is the lowest value possible, 0 (zero) means "no pitch bend"
and 8191 is the highest possible value.

**port**
Returns the port number  0-256 for a meta MIDI\_PORT message

**program**
Returns the program number 0-127 for a PROGRAM\_CHANGE event.

**seconds**
Returns the seconds for the SMPTE\_OFFSET meta message,
usually from 0 to 59.

**status**
Returns the event status. For midi channel events, such as note on, note off,
program change, the lower nibble (lower 4 bits) are cleared (set to zero).
For a meta event, this is the meta type, for example 0x2f for "end of track".
 
Available for all possible events. For custom or proprietary meta events, this
will be the meta type of that event.
 
Examples:
    if event.status == umidiparser.NOTE\_OFF:
        .... process note off event ...
    elif event.status == umidiparser.KEY\_SIGNATURE:
        ... process key signature meta event ...
 
Possible values
All names are global constants in this module e.g. umidiparser.NOTE\_OFF
NOTE\_OFF 0x80
NOTE\_ON 0x90
POLYTOUCH 0xa0
CONTROL\_CHANGE 0xb0
PROGRAM\_CHANGE 0xc0
AFTERTOUCH 0xd0
PITCHWHEEL 0xe0
 
Meta messages (all with prefix 0xff)
SEQUENCE\_NUMBER 0x00
TEXT 0x01
COPYRIGHT 0x02
TRACK\_NAME 0x03
INSTRUMENT\_NAME 0x04
LYRICS 0x05
MARKER 0x06
CUE\_MARKER 0x07
PROGRAM\_NAME 0x08
DEVICE\_NAME 0x09
CHANNEL\_PREFIX 0x20
MIDI\_PORT 0x21
END\_OF\_TRACK 0x2f
SET\_TEMPO 0x51
SMPTE\_OFFSET 0x54
TIME\_SIGNATURE 0x58
KEY\_SIGNATURE 0x59
SEQUENCER\_SPECIFIC 0x7f
 
Sysex/escape events
SYSEX 0xf0
ESCAPE 0xf7

**sub\_frames**
Returns the sub frames for the SMPTE\_OFFSET meta message,
usually from 0 to 59.

**tempo**
Returns the tempo (0 to 2\*\*32 microseconds per quarter beat)
for a SET\_TEMPO meta event.
This module interprets the tempo event before returning it, so
the following events returned will have their delta\_us property
calculated with the new tempo value.

**text**
Returns the text for a meta events.
 
text property is available for:  TEXT COPYRIGHT LYRICS MARKER CUE\_MARKER
 
In MIDI files, text is stored as "extended ASCII", this is
decoded with the iso8859\_1 encoding.
 
The raw data can be retrieved using the data property.

**value**
Returns the the value in the event.
 
value property available for:  AFTERTOUCH, CONTROL\_CHANGE, POLYTOUCH

**velocity**
Returns the velocity fot the event, usually 0-127.
 
velocity property available for:  NOTE\_OFF NOTE\_ON



---


Data descriptors defined here:
**\_\_dict\_\_**
dictionary for instance variables (if defined)

**\_\_weakref\_\_**
list of weak references to the object (if defined)
 |

 


|  |
| --- |
| 
class **MidiFile**([builtins.object](builtins.html#object)) |
|     | [MidiFile](#MidiFile)(filename, buffer\_size=100, reuse\_event\_object=False)
 
Parses a MIDI file.
Once initialized, you can iterate through the events of the file or
tnrough the events of a certain track, see \_\_iter\_\_ and play methods.  |
|  | Methods defined here:
**\_\_init\_\_**(self, filename, buffer\_size=100, reuse\_event\_object=False)filename
 
The name of a MIDI file, usually a .mid or .rtx MIDI file.
The MIDI file will always be opened read only.
 
buffer\_size=100
 
The buffer size that will be allocated for each track.
In order to process files larger than the available RAM,
buffer\_size=n will allocate "n" bytes of buffer for
each track, and read each tracks in "n" byte portions during the
processing of the file, i.e. while iterating through the events. This will
need one file descriptor (one open file) for each track, but will
consume only a fraction of RAM needed for the processing of a file,
as opposed to reading the file into memory with buffer\_size=0.
A buffer size of less than 10 bytes will increase CPU overhead and is not
recommended. A buffer size much larger than 100 will probably not give a
relevant performance advantage, unless the device where the file
resides is slow.
 
If buffer\_size=0, all tracks will be read to memory.
This will need as much RAM as the file size of a complete MIDI file.
In this case, the time needed to process each event will not depend on
file access nd will be both faster and more dependable than using a
buffer\_size different to 0, if the device where the file resides is slow.
 
The default value for buffer\_size is 100 bytes.
 
reuse\_event\_object=False
 
With the default value of False, for each call a new [MidiEvent](#MidiEvent) is returned,
this is, if you do:
    for event in [MidiFile](#MidiFile)("example.mid"):
        ... process each event ...
 
then in each iteration of the loop you get a different, and new, [MidiEvent](#MidiEvent).
This is the normal and expected behaviour for Python iterators.
 
If you need higher processing speed, and if you don't want to
fragment RAM heap space, use:
 
    for event in [MidiFile](#MidiFile)("example.mid", reuse\_event\_object=True):
        ... process each event ....
 
In this case, for each iteration of the loop, the same [MidiEvent](#MidiEvent) is returned,
and is overwritten with the last data. The event data will not be
changed in the body of the for loop. However, if you want to store an event
for later use,  you'll have to use event.copy.
 
All combinations of reuse\_event\_object and buffer\_size are valid.
 
Instance variables:
 
tracks
List [object](builtins.html#object) with the tracks of the file. len(midifile.tracks) is the number of tracks.
To get the events in an individual track, use:
    for event in [MidiFile](#MidiFile)("example.mid").tracks[3]:
    ... process events of track 3 of the list ....
 
Exceptions:
The file must start with a standard MIDI file header (MThd), if not, a
ValueError is raised.
The MIDI header chunk must be at least 6 bytes long, or a ValueError
is raised.
ValueError is raised if no header present, or too short.
ValueError is raised if the header contains SMPTE time codes (not supported).
Chunks after the header that are not tracks
(i.e. don't have a "MTrk" MIDI header) are ignored.
**\_\_iter\_\_**(self)To get all the events of a format type 0 or format type 1 MIDI file,
iterate through the [MidiFile](#MidiFile) [object](builtins.html#object), for example:
    for event in [MidiFile](#MidiFile)("example.mid"):
        print(event)
 
 
Events will be returned in ascending order in time. For format type 1
multitrack files, all tracks are merged.
 
The event.delta\_us property is calculated as the
time in microseconds between last and this event, taking into account both
the set tempo meta events and the "MIDI ticks per quarter note"
parameter in the MIDI file header. For type 1 files, all set tempo meta
events may be in track 0 (as it is usually done), or they may occur in any track.
 
For a multitrack file, event.delta\_us is the time difference with the
previous event, which may be in the same or a different track.
 
For a format type 2 MIDI file, a single track must be selected, track
numbers range from 0 to len([MidiFile](#MidiFile).tracks)-1
 
    for event in [MidiFile](#MidiFile)("example.mid").tracks[5]:
        ... process event ...
 
When parsing a file format 2 track, then only the set tempo
events of that track are processed to calculate delta\_us.
 
To process each event at the time due, a simple version could be:
    for event in [MidiFile](#MidiFile)("example.mid"):
        time.sleep\_us( event.delta\_us )
        ... process the event ...
 
To implement this function with time error compensation, use the
[MidiFile](#MidiFile).play method.
 
In all cases, only one end of track meta event is returned
to the caller when the end of file is reached.
Events beyond a end of track event are ignored.
 
Exceptions:
RuntimeError is raised if format type 2 is processed with this method.
Use the [MidiFile](#MidiFile).tracks[n] to iterate through a single track.
**length\_us**(self)Returns the length of the [MidiFile](#MidiFile) in microseconds.
 
Beware, on a slow microcontroller, calculating the length of
a large MIDI file might take a several of seconds.
This is due to the way MIDI files work, in order to
get the playing length, this method needs to parse
the entire file, compute and sum the time differences of all events.
 
Exceptions:
RuntimeError for format type 2 files. It is not possible to calculate the
playing time of a format 2 file, since for format 2 files,
the tracks are not meant to be merged.
**play**(self, track\_number=None)Iterate through the events of a MIDI file or a track,
sleep until the event has to take place, and
yield the event.
 
Parameters
track\_number=None
 
If track\_number=None, and the MIDI file is format 0 or 1,
play the complete file. Merge all tracks.
 
If a track number is specified, then that track number is played. This
is intended for use with format type 2 files, to play a certain track.
 
Example:
    for event in [MidiFile](#MidiFile)("example.mid").[play](#MidiFile-play)():
        .... process the event ...
The play function will wait the necessary time between iterations
so that each event is yielded on time to be processed.
 
This function compensates for the accumulated error in the
processing of each event. Since sleep functions will sleep
AT LEAST the time specified, normally the time slept will be longer. This
means, for a long file of several thousand events, events may get ever later.
This is noticeable especially of another thread or process is active, or
if the processing of each event takes significant time.
Even so, since play uses the sleep\_us function, sometimes
you may get the event a bit later than the correct time.
 
For Micropython, time.sleep\_us() is used. For CPython time.sleep() is used.


---


Readonly properties defined here:
**buffer\_size**
Return the buffer\_size value. 0=tracks are buffered entirely in RAM.
A number, for example buffer\_size=100 means a buffer of 100 bytes is
allocated per track to read the track data.
 
This allows to read large MIDI files efficiently on microcontrollers with small RAM.

**filename**
Return the file name of the MIDI file, with absolute path.

**format\_type**
Returns the MIDI format type as stored in the header of the MIDI file:
0   single track MIDI file, should have only one track.
    To parse a type 0 file, use the MIdiFile object as iterator:
        for event in MidiFile("example.mid"):
            process each event
1   multitrack MIDI file, can have many tracks. During playback, the tracks
are merged into one ordered sequence of events.
    To parse a type 1 file, proceeed as with a type 0 file.
2   each track behaves like a format 0 single track MIDI file. Merging
tracks is not allowed. Track number "n" is parsed as follows:
    for event in MidiFile("format2file.mid").tracks[n]:
        .... process event...

**miditicks\_per\_quarter**
Return the midi ticks per quarter note (also called pulses per beat)
parameter in the MIDI header of the file.

**reuse\_event\_object**
Return the value of reuse\_event\_object.
True: when iterating through a track or midi file, the same event object
is returned over and over (this is a optimization recommended for Micropython)
 
False: when iterating through a track or midi file, a different event
object is returned each time (this is the typical Python behaviour).



---


Data descriptors defined here:
**\_\_dict\_\_**
dictionary for instance variables (if defined)

**\_\_weakref\_\_**
list of weak references to the object (if defined)
 |

 


|  |
| --- |
| 
class **MidiTrack**([builtins.object](builtins.html#object)) |
|     | [MidiTrack](#MidiTrack)(file, midifile)
 
This [object](builtins.html#object) contains the track of a midi file. It is
created internally by the [MidiFile](#MidiFile) function for each track
chunk found in the midi file.
 
[MidiTrack](#MidiTrack) objects are accessible via the [MidiFile](#MidiFile).tracks list  |
|  | Methods defined here:
**\_\_init\_\_**(self, file, midifile)The [MidiTrack](#MidiTrack) cosntructor is called internally by [MidiFile](#MidiFile),
you don't need to create a [MidiTrack](#MidiTrack).
**\_\_iter\_\_**(self)Iterating through a track will yield all events of that track
of MIDI file. For example, to parser the first track in a midi file:
 
    for event in [MidiFile](#MidiFile)("example.mid").track[0]:
        .... process event ...
 
event.delta\_miditicks will have the time difference with the previous
event, in MIDI ticks (pulses).
 
event.delta\_us is calculated as the time difference with the previous event
in microseconds. For this calculation, the set tempo events and
the MIDI ticks per quarter note (also called "pulses per beat")
of the MIDI file header are taken into consideration.
 
This function should only be necessary to play a single
track of a format type 2 file. Format 2 type files are
not very common.
 
The last event will always be a END\_OF\_TRACK event, if missing in the file.
**\_\_lt\_\_**(self, compare\_to)Used internally by the min function to compare the current time in miditicks
of the different tracks, the goal is to find the next midi event
of all tracks (the one with the smallest time since the beginning of the track)


---


Data descriptors defined here:
**\_\_dict\_\_**
dictionary for instance variables (if defined)

**\_\_weakref\_\_**
list of weak references to the object (if defined)
 |

 |




|  |
| --- |
| 
**Functions** |
|        |  | **const** *lambda* x# Ignore const
**micropython**(function)# Make the @micropython.native decorator do nothing
**os\_path\_abspath** *lambda* x
**ticks\_diff\_us** *lambda* x, y
**ticks\_now\_us** *lambda* (...)
**time\_sleep\_us** *lambda* usec# These functions only are available in Micropython |




|  |
| --- |
| 
**Data** |
|        |  | **AFTERTOUCH** = 208
**CHANNEL\_PREFIX** = 32
**CONTROL\_CHANGE** = 176
**COPYRIGHT** = 2
**CUE\_MARKER** = 7
**DEVICE\_NAME** = 9
**END\_OF\_TRACK** = 47
**ESCAPE** = 247
**INSTRUMENT\_NAME** = 4
**KEY\_SIGNATURE** = 89
**LYRICS** = 5
**MARKER** = 6
**MIDI\_PORT** = 33
**NOTE\_OFF** = 128
**NOTE\_ON** = 144
**PITCHWHEEL** = 224
**POLYTOUCH** = 160
**PROGRAM\_CHANGE** = 192
**PROGRAM\_NAME** = 8
**SEQUENCER\_SPECIFIC** = 127
**SEQUENCE\_NUMBER** = 0
**SET\_TEMPO** = 81
**SMPTE\_OFFSET** = 84
**SYSEX** = 240
**TEXT** = 1
**TIME\_SIGNATURE** = 88
**TRACK\_NAME** = 3
**UPYTHON** = False |










