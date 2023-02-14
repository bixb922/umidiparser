'''
Helper functions to interpret midi values assigned in General Midi (GM): 
note names, controller names,
program change names, percussion midi names,
frequency of midi note.
'''
GM_PROGRAM=[
"gm zero",
"Acoustic Grand Piano",
"Bright Acoustic Piano",
"Electric Grand Piano",
"Honky-tonk Piano",
"Electric Piano 1",
"Electric Piano 2",
"Harpsichord",
"Clavi",
"Celesta",
"Glockenspiel",
"Music Box",
"Vibraphone",
"Marimba",
"Xylophone",
"Tubular Bells",
"Dulcimer",
"Drawbar Organ",
"Percussive Organ",
"Rock Organ",
"Church Organ",
"Reed Organ",
"Accordion",
"Harmonica",
"Tango Accordion",
"Acoustic Guitar (nylon)",
"Acoustic Guitar (steel)",
"Electric Guitar (jazz)",
"Electric Guitar (clean)",
"Electric Guitar (muted)",
"Overdriven Guitar",
"Distortion Guitar",
"Guitar Harmonics",
"Acoustic Bass",
"Electric Bass (finger)",
"Electric Bass (pick)",
"Fretless Bass",
"Slap Bass 1",
"Slap Bass 2",
"Synth Bass 1",
"Synth Bass 2",
"Violin",
"Viola",
"Cello",
"Contrabass",
"Tremolo Strings",
"Pizzicato Strings",
"Orchestral Harp",
"Timpani",
"String Ensemble 1",
"String Ensemble 2",
"Synth Strings 1",
"Synth Strings 2",
"Choir Aahs",
"Voice Oohs",
"Synth Voice",
"Orchestra Hit",
"Trumpet",
"Trombone",
"Tuba",
"Muted Trumpet",
"French Horn",
"Brass Section",
"Synth Brass 1",
"Synth Brass 2",
"Soprano Sax",
"Alto Sax",
"Tenor Sax",
"Baritone Sax",
"Oboe",
"English Horn",
"Bassoon",
"Clarinet",
"Piccolo",
"Flute",
"Recorder",
"Pan Flute",
"Blown bottle",
"Shakuhachi",
"Whistle",
"Ocarina",
"Lead 1 (square",
"Lead 2 (sawtooth)",
"Lead 3 (calliope)",
"Lead 4 (chiff)",
"Lead 5 (charang)",
"Lead 6 (voice)",
"Lead 7 (fifths)",
"Lead 8 (bass + lead)",
"Pad 1 (new age)",
"Pad 2 (warm)",
"Pad 3 (polysynth)",
"Pad 4 (choir)",
"Pad 5 (bowed)",
"Pad 6 (metallic)",
"Pad 7 (halo)",
"Pad 8 (sweep)",
"FX 1 (rain)",
"FX 2 (soundtrack)",
"FX 3 (crystal=",
"FX 4 (atmosphere)",
"FX 5 (brightness)",
"FX 6 (goblins)",
"FX 7 (echoes)",
"FX 8 (sci-fi)",
"Sitar",
"Banjo",
"Shamisen",
"Koto",
"Kalimba",
"Bag pipe",
"Fiddle",
"Shanai",
"Tinkle Bell",
"Agogô",
"Steel Drums",
"Woodblock",
"Taiko Drum",
"Melodic Tom",
"Synth Drum",
"Reverse Cymbal",
"Guitar Fret Noise",
"Breath Noise",
"Seashore",
"Bird Tweet",
"Telephone Ring",
"Helicopter",
"Applause",
"Gunshot"
]

GM_PERCUSSION = {
33:"Metronome Click",
34:"Metronome Bell",
35:"Acoustic Bass Drum",
36:"Bass Drum 1",
37:"Side Stick",
38:"Acoustic Snare",
39:"Hand Clap",
40:"Electric Snare",
41:"Low Floor Tom",
42:"Closed Hi-Hat",
43:"High Floor Tom",
44:"Pedal Hi-Hat",
45:"Low Tom",
46:"Open Hi-Hat",
47:"Low-Mid Tom",
48:"Hi-Mid Tom",
49:"Crash Cymbal 1",
50:"High Tom",
51:"Ride Cymbal 1",
52:"Chinese Cymbal",
53:"Ride Bell",
54:"Tambourine",
55:"Splash Cymbal",
56:"Cowbell",
57:"Crash Cymbal 2",
58:"Vibraslap",
59:"Ride Cymbal 2",
60:"Hi Bongo",
61:"Low Bongo",
62:"Mute Hi Conga",
63:"Open Hi Conga",
64:"Low Conga",
65:"High Timbale",
66:"Low Timbale",
67:"High Agogo",
68:"Low Agogo",
69:"Cabasa",
70:"Maracas",
71:"Short Whistle",
72:"Long Whistle",
73:"Short Guiro",
74:"Long Guiro",
75:"Claves",
76:"Hi Wood Block",
77:"Low Wood Block",
78:"Mute Cuica",
79:"Open Cuica",
80:"Mute Triangle",
81:"Open Triangle"
}

GM_CC={
0:"Bank Select MSB)",
1:"Modulation MSB)",
10:"Pan MSB)",
100:"Reg-Param LSB)",
101:"Reg-Param MSB)",
11:"Expression MSB)",
12:"Effects Controller 1",
120:"All Sound Off",
121:"Reset All Controllers",
122:"Local Control",
123:"All Notes Off",
124:"Omni Off",
125:"Omni On",
126:"Mono On Poly Off)",
127:"Poly On Mono Off)",
13:"Effects Controller 2",
16:"Gen Purpose 1 MSB)",
17:"Gen Purpose 2 MSB)",
18:"Gen Purpose 3 MSB)",
19:"Gen Purpose 4 MSB)",
2:"Breath Control MSB)",
32:"Bank Select LSB)",
33:"Modulation LSB)",
34:"Breath Control LSB)",
36:"Foot Control LSB)",
37:"Portamento Time LSB",
38:"Data Entry LSB)",
39:"Channel Volume LSB",
4:"Foot Control MSB)",
40:"Balance LSB)",
42:"Pan LSB)",
43:"Expression LSB)",
48:"Gen Purpose 1 LSB)",
49:"Gen Purpose 2 LSB)",
5:"Portamento Time MSB",
50:"Gen Purpose 3 LSB)",
51:"Gen Purpose 4 LSB)",
6:"Data Entry MSB)",
64:"Sustain Pedal",
65:"Portamento on/off",
66:"Sostenuto Pedal",
67:"Soft Pedal",
68:"Legato Pedal",
69:"Hold 2",
7:"Channel Volume MSB",
70:"Sound Variation",
71:"Resonance",
72:"Release Time",
73:"Attack Time",
74:"Cut-off Frequency",
75:"Decay Time",
76:"Vibrato Rate",
77:"Vibrato Depth",
78:"Vibrato Delay",
8:"Balance MSB)",
80:"Gen Purpose 5",
81:"Gen Purpose 6",
82:"Gen Purpose 7",
83:"Gen Purpose 8",
84:"Portamento Control",
91:"Reverb Depth",
92:"Tremolo Depth",
93:"Chorus Depth",
94:"Celeste De-tune)",
95:"Phaser Depth",
96:"Data Increment",
97:"Data Decrement",
98:"non-reg param lsb",
99:"non-reg param msb"
}

def _note_name( midi, note_list ):
    return note_list[ midi%12 ] + str( (midi//12) - 1 )

def note_name_american( midi ):
    '''
    Converts midi number (0-127) to american note name, e.g. midi 60 is a C4
    Please change the accidentals to what you need.
    '''
    note_list = ( "C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B" )
    return _note_name( midi, note_list )
    
def note_name_latin( midi ):
    '''
    Converts midi number (0-127) to latin note name, e.g. midi 60 is a Do4
    Please change the accidentals to what you need.
    '''
    note_list = ( "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Fa#", "Sol", "Lab", "La", "Sib", "Si" )
    return _note_name( midi, note_list )

def midi_to_frequency( midi, central=440 ):
    '''
    Returns equal temperament frequency in Hz of midi note.
    central parameter indicates frequency of A4/La4
    '''
    return central*2**((midi-69)/12)

def program_name( program ):
    '''
    Translate program name using GM table. The parameter is the
    program attribute of the Program Change event (0-127).
    '''
    return GM_PROGRAM[program]

def percussion_name( midi ):
    '''
    Translate percussion name using GM table. The parameter is
    the midi number of the note. Will raise KeyError if not assigned.
    '''
    return GM_PERCUSSION[midi]

def controller_name( control ):
    '''
    Translate control change name using GM table.
    The parameter is the controller number of a Control Change event.
    Will raise KeyError if not assigned
    '''
    return GM_CC[control]

if __name__ == "__main__":
    print(f"{note_name_american(60)=} expected=C4")
    print(f"{note_name_latin(60)=} expected=Do4")
    print(f"{midi_to_frequency(50)=:.2f} expected 146.83")
    print(f"{program_name(43)=} expected=Contrabass")
    print(f"{percussion_name(33)=} expected=Metronome Click")
    print(f"{controller_name(64)=} expected=Sustain Pedal")
