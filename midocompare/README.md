# Comparison test

The mido_compare.py script allows to compare the output of umidiparser compared to the excellent MIDO (MIDI Objects for Python) package (https://github.com/mido/mido). The usage of MIDO and umidiparser have similarities, so the comparison is quite straightforward. You will need to download MIDO as prerrequisite, see https://mido.readthedocs.io/en/latest/installing.html.  You also need to install umidiparser in your PC using ```python3 pip install umidiparser```

MIDI files are read and compared. No MIDI is sent to a hardware or software player, so no backend is really required for MIDO. This script is for a PC with CPython, not for a microcontroller with Micropython.

To run mido_compare.py use:

```py
python3 mido_compare.py <folder>
```
or

```py
python3 mido_compare.py <midi-file>
```

If a <folder> is specified, 
mido_compare.py will search there for .mid or .rtx files and compare them. With the <file> parameter, a single file can be compared. The script compares each MIDI event and it's attributes such as delta time converted to seconds, note velocity, note number, text in the case of MIDI meta events, etc. The number of differences and exceptions are reported by each file, with totals when finishing. 

The time for each event is compared within 0.000001 seconds (one microsecond) which is the precision of umidiparser. 

Contents of SMPTE offset meta messages are currently not compared.

Error behaviour differs, i.e. MIDI files that do not comply to the standard are detected by MIDO, but not always bu umidiparser. For example MIDO checks that values such as notes, velocities or program numbers are between 0 and 127, but umidiparser does not and passes the note to the calling program, so you can check (or not) if the value is in range. For example, MIDO checks that the key specification of the the meta key signature is correct, umidiparser maps bad key specifications to a sensible output, etc, etc. This lack of checking was intentional to keep umidiparser a bit smaller and faster. However, both check that the file format is correct, i.e. that MThd and MTrk are present, and check the message syntax, among many other verifications.

The expected output looks like this:
```
python3 mido_compare.py ../folder_with_midi_files
Comparing folder ../folder_with_midi_files
compare nice_tune.mid
compare other_tune.mid

... etc etc ..
File count= 341 differences=0 exceptions=3 events=2,735,037 total playing time= 109866.1 sec
Frequency of MIDI events
     note_off 395077
     note_on 2107949
     polytouch 0
     control_change 163230
     program_change 4040
     aftertouch 2559
     pitchwheel 40684
     sequence_number 0
     text 2629
     copyright 47
     track_name 2516
     instrument_name 155
     lyrics 1652
     marker 190
     cue_marker 27
     program_name 0
     device_name 10
     channel_prefix 246
     midi_port 1987
     end_of_track 338
     set_tempo 9588
     smpte_offset 51
     time_signature 871
     key_signature 600
     sequencer_specific 163
     sysex 428
     escape 0
```
When no message appears in the lines following the file name, no differences have been detected.

