# Compares contents of MIDI files event by event parsing with MIDO and umidiparser
# Command line arguments are one or more folder names with .mid or .rtx files
# Runs on regular CPython on Mac (and I suppose on Windows and Linux too)

import sys
from glob import glob
import os.path
import mido

import umidiparser

# Count by MIDI event type to get coverage    
event_counters = {
    "note_off": 0,
    "note_on" : 0,
    "polytouch" : 0,
    "control_change" : 0,
    "program_change" : 0,
    "aftertouch" : 0,
    "pitchwheel" : 0,
    "sequence_number" : 0,
    "text" : 0,
    "copyright" : 0,
    "track_name" : 0,
    "instrument_name" : 0,
    "lyrics" : 0,
    "marker" : 0,
    "cue_marker" : 0,
    "program_name" : 0,
    "device_name" : 0,
    "channel_prefix" : 0,
    "midi_port" : 0,
    "end_of_track" : 0,
    "set_tempo" : 0,
    "smpte_offset" : 0,
    "time_signature" : 0,
    "key_signature" : 0,
    "sequencer_specific" : 0,
    "sysex" : 0,
    "escape" : 0 
    }

# These META messages have text data, with either a .text or .name method
# META messages with "_name" have a .name attribute
text_metas = {
      "text": umidiparser.TEXT,
      "copyright": umidiparser.COPYRIGHT,
      "track_name": umidiparser.TRACK_NAME,
      "instrument_name": umidiparser.INSTRUMENT_NAME,
      "lyrics": umidiparser.LYRICS,
      "marker": umidiparser.MARKER,
      "cue_marker": umidiparser.CUE_MARKER,
      "program_name": umidiparser.PROGRAM_NAME,
      "device_name": umidiparser.DEVICE_NAME
      }

def convert_to_ascii( data ):
        # Redirecting standard output may cause exception in Windoes
        # if filenames contain certain non-standard characters.
        # There is probably some encoding that does this.
        #  Characters hexa 81, 8D, 8F, 90, y 9D are not mapped
        # in ANSI. Convert to question mark before decoding, if not, an exception
        # may occur at least on Windows if standard output is redirected.
        return data.replace( '\x81', '?' ) \
                   .replace( '\x8d', '?' ) \
                   .replace( '\x8f', '?' ) \
                   .replace( '\x90', '?' ) \
                   .replace( '\x9d', '?' ) \

# Compares a MIDO event and a umidiparser event
def compare_events( mido_event, umidi_event ):
        same_output = True

        if abs(mido_event.time - umidi_event.delta_us/1_000_000) > 0.000001:
            same_output = False
        
        if umidi_event.status == umidiparser.NOTE_ON:
            if mido_event.type != "note_on":
                same_output = False
            if (mido_event.velocity != umidi_event.velocity or 
               mido_event.note != umidi_event.note or 
               mido_event.channel != umidi_event.channel):
                same_output = False

        elif umidi_event.status == umidiparser.NOTE_OFF:
            if mido_event.type != "note_off":
                same_output = False
            if (mido_event.velocity != umidi_event.velocity or 
               mido_event.note != umidi_event.note or 
               mido_event.channel != umidi_event.channel):
                same_output = False

        elif umidi_event.status == umidiparser.POLYTOUCH:
            if mido_event.type != "polytouch":
                same_output = False
            if (mido_event.value != umidi_event.value or 
               mido_event.note != umidi_event.note or 
               mido_event.channel != umidi_event.channel):
                same_output = False

        elif umidi_event.status == umidiparser.CONTROL_CHANGE:
            if mido_event.type != "control_change":
                same_output = False
            if ( mido_event.channel != umidi_event.channel or 
               mido_event.control != umidi_event.control or 
               mido_event.value != umidi_event.value):
                same_output = False

        elif umidi_event.status == umidiparser.PROGRAM_CHANGE:
            if mido_event.type != "program_change":
                same_output = False
            if (mido_event.channel != umidi_event.channel or 
               mido_event.program != umidi_event.program):
                same_output = False


        elif umidi_event.status == umidiparser.AFTERTOUCH:
            if mido_event.type != "aftertouch":
                same_output = False
            if ( mido_event.channel != umidi_event.channel or 
               mido_event.value != umidi_event.value):
                same_output = False

        elif umidi_event.status == umidiparser.PITCHWHEEL:
            if mido_event.type != "pitchwheel":
                same_output = False
            if ( mido_event.channel != umidi_event.channel or 
               mido_event.pitch != umidi_event.pitch):
                same_output = False

        elif umidi_event.status == umidiparser.SEQUENCE_NUMBER:
            if mido_event.type != "sequence_number":
                same_output = False
            if mido_event.sequence_number != umidi_event.sequence_number:
                same_output = False
                
        elif umidi_event.status == umidiparser.TIME_SIGNATURE:
            if mido_event.type != "time_signature":
                same_output = False
            if (mido_event.clocks_per_click != umidi_event.clocks_per_click or 
               mido_event.denominator != umidi_event.denominator  or 
               mido_event.numerator != umidi_event.numerator or 
               mido_event.notated_32nd_notes_per_beat != umidi_event.notated_32nd_notes_per_beat )  :
                same_output = False

        
        elif umidi_event.status == umidiparser.KEY_SIGNATURE:
            if mido_event.type != "key_signature":
                same_output = False
            if mido_event.key != umidi_event.key:
                same_output = False

        elif umidi_event.status == umidiparser.END_OF_TRACK:
            if mido_event.type != "end_of_track":
                same_output = False

        elif umidi_event.status == umidiparser.SET_TEMPO:
            if mido_event.type != "set_tempo":
                same_output = False
            if mido_event.tempo != umidi_event.tempo:
                same_output = False

        elif umidi_event.status == umidiparser.CHANNEL_PREFIX:
            if mido_event.type != "channel_prefix":
                same_output = False
            if mido_event.channel != umidi_event.channel:
                same_output = False
                
        elif umidi_event.status == umidiparser.MIDI_PORT:
            if mido_event.type != "midi_port":
                same_output = False
            if mido_event.port != umidi_event.port:
                same_output = False

        elif umidi_event.status == umidiparser.SMPTE_OFFSET:
            if mido_event.type != "smpte_offset":
                same_output = False
            # Cannot compare, MIDO decode.py says 'frame_type': data[0] >> 4
            # Shouldn't that be data[0] >> 5?
                
        elif mido_event.type in text_metas:
            if umidi_event.status != text_metas[mido_event.type]:
                same_output = False
                
            if "_name" in mido_event.type:
                # This is a meta such as track_name, device_name, instrument_name
                if mido_event.name != umidi_event.name:
                        same_output = False
            else:
                # This is a meta such as lyrics, text or copyright
                if mido_event.text != umidi_event.text:
                    same_output = False
                    
        elif umidi_event.status == umidiparser.SYSEX:
            # umidiparser yields the ending 0x7f whereas MIDO doesn't
            # MIDO sysex data is a tuple of integers, umidiparser sysex data is a bytearray
            if mido_event.type != "sysex":
                same_output = False
            # Convert umidiparser data to a tuple and compare
            udata = tuple( umidi_event.data[0:-1] )
            if udata != mido_event.data:
                same_output = False
                print(f"     sysex umidi  umidi_event.data={udata}")
                print(f"     sysex  mido   {mido_event.data=}")

            
        elif umidi_event.status == umidiparser.SEQUENCER_SPECIFIC:
            if mido_event.type != "sequencer_specific":
                same_output = False
            udata = tuple( umidi_event.data )
            if udata != mido_event.data:
                same_output = False
                
        else:
            print("    >>>UNKNOWN EVENT")
            print(f"    >>>>umidi_event={str(umidi_event)}")
            print(f"    >>>>{mido_event=}")

                
        return same_output

def compare_file( filename ):
    # Compare MIDO and umidiparser both reading this file
    print("compare", convert_to_ascii( os.path.basename( filename ) ) )

    # Set up one iterator for MIDO and another one for umidiparser
    try:
        mido_events_iterator = iter(mido.MidiFile( filename ))
    except Exception as exp:
        print("    >>>MIDO exception opening file", exp )
        return 0,0,1,0
        
    try:
        umidi_events_iterator = iter([ ue.copy() for ue in umidiparser.MidiFile( filename ) ] )
    except Exception as exp:
        print("    >>>umidiparser exception opening file", exp )
        return 0,0,1,0

    differences = 0
    playing_time = 0
    events = 0
    while True:

        mido_eof = False
        umidi_eof = False
        try:
            mido_event = next( mido_events_iterator )
        except StopIteration:
            mido_eof = True
        except Exception as exp:
            print("    >>>MIDO exception getting next event", exp )
            return differences, playing_time, 1, 0

        try:
            umidi_event = next( umidi_events_iterator )
        # StopIteration indicates a problem, must have same number of events
        except StopIteration:
            umidi_eof = True
        except Exception as exp:
            print("     >>>umidiparser exception getting next event", exp )
            return differences, playing_time, 1, events


        if mido_eof or umidi_eof:
            if mido_eof == umidi_eof:
                break
            print(f"    >>>end of file difference {umidi_eof=}")
            print(f"    >>>end of file difference {mido_eof=}")
            if not umidi_eof:
                print(f"    >>>umidi extra event umidi_event={str(umidi_event)}")
            if not mido_eof:
                print(f"    >>>>mido extra event  {mido_event=}")
            differences += 1
            break

        same_output = compare_events( mido_event, umidi_event )
        events += 1
                
        if not same_output:
            print( f"    >>>different event umidi_event={str(umidi_event)}" )
            print( f"    >>>different event  {mido_event=}" ) 
            print("")
            differences += 1

        # Count events by type for final statistics
        event_counters[mido_event.type] += 1
        
        # Sum playing time as a statistic
        playing_time += umidi_event.delta_us/1_000_000

    return differences, playing_time, 0, events
    
def process_file_list( file_list ):
 
    differences = 0
    exceptions = 0
    playing_time = 0
    events = 0
    for filename in file_list:
            dif = 0
            exc = 0
            plt = 0
            ev = 0
            try:
                dif, plt, exc, ev  = compare_file( filename )
            except Exception as exp:
                print("    >>>Unhandled exception in", convert_to_ascii( filename ) )
                print("    >>>", exp)
                exc += 1
   
            differences += dif
            exceptions += exc
            playing_time += plt
            events += ev
            
    print(  f"File count={len(file_list)} "
            f"{differences=} {exceptions=} {events=:,} "
            f"total playing time={playing_time:,.1f} sec" )
 
    return 
    
def main():
    file_types = (".mid", ".rtx")
    if len(sys.argv) != 2:
        print("Compares contents of MIDI files event by event parsing with MIDO and umidiparser")
        print(f"Command argument line must be a folder with MIDI files {file_types}) or a single MIDI file name")
        sys.exit()
        
    file_or_folder = sys.argv[1]    

    if file_or_folder[-4:].lower() in file_types:
        print("Comparing file", file_or_folder )
        file_list = [ file_or_folder ]
    else:
        file_list = [ f for f in glob( os.path.join(file_or_folder, "*.*"))
                        if f[-4:].lower() in file_types ]
        print("Comparing folder", file_or_folder )
        
    process_file_list( file_list )
    
    print("")
    print("Frequency of MIDI events")
    for k,v  in event_counters.items():
        print(f"    {k} {v:,}")
    
main()            
