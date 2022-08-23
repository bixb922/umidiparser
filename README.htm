<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module umidiparser</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>umidiparser</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/Users/hermannvonborries/Library/CloudStorage/GoogleDrive-hermannvb%40gmail.com/My%20Drive/cosas/micropython/umidiparser/umidiparser.py">/Users/hermannvonborries/Library/CloudStorage/GoogleDrive-hermannvb@gmail.com/My Drive/cosas/micropython/umidiparser/umidiparser.py</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="os.html">os</a><br>
</td><td width="25%" valign=top><a href="time.html">time</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>
    
<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="builtins.html#object">builtins.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="umidiparser.html#MidiEvent">MidiEvent</a>
</font></dt><dt><font face="helvetica, arial"><a href="umidiparser.html#MidiFile">MidiFile</a>
</font></dt><dt><font face="helvetica, arial"><a href="umidiparser.html#MidiTrack">MidiTrack</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="MidiEvent">class <strong>MidiEvent</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt>Represents&nbsp;a&nbsp;parsed&nbsp;midi&nbsp;event.<br>
&nbsp;<br>
PROPERTIES&nbsp;AVAILABLE&nbsp;FOR&nbsp;ALL&nbsp;EVENTS<br>
&nbsp;<br>
event.status:&nbsp;this&nbsp;is&nbsp;the&nbsp;event&nbsp;type,&nbsp;such&nbsp;as&nbsp;note&nbsp;on,&nbsp;note&nbsp;off,<br>
set&nbsp;tempo,&nbsp;end&nbsp;of&nbsp;track,&nbsp;sysex.&nbsp;You&nbsp;can&nbsp;compare&nbsp;event.status<br>
with&nbsp;the&nbsp;constants&nbsp;umidiparser.NOTE_ON,&nbsp;umidiparser.NOTE_OFF,<br>
umidiparser.PROGRAM_CHANGE,&nbsp;etc.<br>
&nbsp;<br>
event.delta_miditicks:&nbsp;difference,&nbsp;in&nbsp;midi&nbsp;ticks&nbsp;or&nbsp;pulses&nbsp;between&nbsp;last&nbsp;event<br>
and&nbsp;this&nbsp;event,&nbsp;also&nbsp;known&nbsp;as&nbsp;"delta&nbsp;time"&nbsp;of&nbsp;the&nbsp;event.<br>
For&nbsp;single&nbsp;track&nbsp;files,&nbsp;the&nbsp;time&nbsp;difference&nbsp;is&nbsp;with&nbsp;the&nbsp;previous&nbsp;event<br>
of&nbsp;the&nbsp;same&nbsp;track.&nbsp;When&nbsp;parsing&nbsp;multitrack&nbsp;files,&nbsp;tracks&nbsp;are&nbsp;merged&nbsp;and&nbsp;this<br>
time&nbsp;is&nbsp;set&nbsp;during&nbsp;playback&nbsp;to&nbsp;the&nbsp;time&nbsp;difference&nbsp;with&nbsp;the&nbsp;previous&nbsp;event&nbsp;in&nbsp;any&nbsp;track.<br>
&nbsp;<br>
event.delta_us:&nbsp;time&nbsp;in&nbsp;microseconds&nbsp;since&nbsp;the&nbsp;last&nbsp;event&nbsp;for&nbsp;this<br>
event&nbsp;to&nbsp;start.&nbsp;For&nbsp;example,&nbsp;you&nbsp;might&nbsp;use&nbsp;sleep_us(&nbsp;event.delta_us&nbsp;)&nbsp;to<br>
sleep&nbsp;the&nbsp;appropiate&nbsp;time&nbsp;for&nbsp;the&nbsp;event&nbsp;to&nbsp;start.<br>
&nbsp;<br>
event.data&nbsp;contains&nbsp;the&nbsp;raw&nbsp;event&nbsp;data.<br>
&nbsp;<br>
str(event)&nbsp;will&nbsp;a&nbsp;string&nbsp;like&nbsp;this:<br>
&nbsp;<br>
&nbsp;<br>
PROPERTIES&nbsp;BY&nbsp;EVENT&nbsp;TYPE<br>
&nbsp;<br>
For&nbsp;each&nbsp;type&nbsp;of&nbsp;event,&nbsp;only&nbsp;the&nbsp;applicable&nbsp;properties&nbsp;are&nbsp;enabled.<br>
The&nbsp;following&nbsp;list&nbsp;shows&nbsp;the&nbsp;event&nbsp;status&nbsp;and&nbsp;properties<br>
that&nbsp;you&nbsp;can&nbsp;get.<br>
&nbsp;<br>
For&nbsp;example:&nbsp;for&nbsp;a&nbsp;note_on&nbsp;event,&nbsp;event.status&nbsp;is&nbsp;umidiparser.NOTE_ON<br>
and&nbsp;event.note,&nbsp;event.channel,&nbsp;and&nbsp;event.velocity&nbsp;have&nbsp;the&nbsp;corresponding<br>
values.&nbsp;But&nbsp;for&nbsp;a&nbsp;program&nbsp;change&nbsp;event,&nbsp;event.velocity&nbsp;will&nbsp;not&nbsp;be&nbsp;available.<br>
&nbsp;<br>
Attributes&nbsp;that&nbsp;are&nbsp;not&nbsp;allowed&nbsp;generate&nbsp;an&nbsp;AttributeError&nbsp;on&nbsp;access.<br>
&nbsp;<br>
PROPERTIES&nbsp;FOR&nbsp;MIDI&nbsp;CHANNEL&nbsp;EVENTS<br>
NOTE_OFF&nbsp;/midi&nbsp;event&nbsp;status&nbsp;byte=0x80&nbsp;to&nbsp;0x8f)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;note&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;velocity&nbsp;(int)<br>
NOTE_ON&nbsp;(midi&nbsp;event&nbsp;status&nbsp;byte=0x90&nbsp;to&nbsp;0x9f)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;note&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;velocity&nbsp;(int)<br>
POLYTOUCH&nbsp;(midi&nbsp;event&nbsp;status&nbsp;byte=0xa0&nbsp;to&nbsp;0xaf)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;note&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;value&nbsp;(int)<br>
CONTROL_CHANGE&nbsp;(midi&nbsp;event&nbsp;status&nbsp;byte=0xb0&nbsp;to&nbsp;0xbf)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;control&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;value&nbsp;(int)<br>
PROGRAM_CHANGE&nbsp;(midi&nbsp;event&nbsp;status&nbsp;byte=0xc0&nbsp;to&nbsp;0xcf)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;program&nbsp;(int)<br>
AFTERTOUCH&nbsp;(midi&nbsp;event&nbsp;status&nbsp;byte=0xd0&nbsp;to&nbsp;0xdf)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;value&nbsp;(int)<br>
PITCHWHEEL&nbsp;(midi&nbsp;event&nbsp;status&nbsp;byte=0xe0&nbsp;to&nbsp;0xef)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;pitch&nbsp;(int)<br>
&nbsp;<br>
PROPERTIES&nbsp;FOR&nbsp;META&nbsp;AND&nbsp;SYSEX&nbsp;EVENTS<br>
SEQUENCE_NUMBER&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x00)<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&nbsp;(int)<br>
TEXT&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x01)<br>
&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;(str)<br>
COPYRIGHT&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x02)<br>
&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;(str)<br>
TRACK_NAME&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x03)<br>
&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;(str)<br>
INSTRUMENT_NAME&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x04)<br>
&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;(str)<br>
LYRICS&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x05)<br>
&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;(str)<br>
MARKER&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x06)<br>
&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;(str)<br>
CUE_MARKER&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x07)<br>
&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;(str)<br>
PROGRAM_NAME&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x08)<br>
&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;(str)<br>
DEVICE_NAME&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x09)<br>
&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;(str)<br>
CHANNEL_PREFIX&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x20)<br>
&nbsp;&nbsp;&nbsp;&nbsp;channel&nbsp;(int)<br>
MIDI_PORT&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x21)<br>
&nbsp;&nbsp;&nbsp;&nbsp;port&nbsp;(int)<br>
END_OF_TRACK&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x2f)<br>
&nbsp;&nbsp;&nbsp;&nbsp;no&nbsp;event&nbsp;specific&nbsp;attributes&nbsp;available<br>
SET_TEMPO&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x51)<br>
&nbsp;&nbsp;&nbsp;&nbsp;tempo&nbsp;(int)<br>
SMPTE_OFFSET&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x54)<br>
&nbsp;&nbsp;&nbsp;&nbsp;frame_rate&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;frames&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;hours&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;minutes&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;seconds&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;sub_frames&nbsp;(int)<br>
TIME_SIGNATURE&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x58)<br>
&nbsp;&nbsp;&nbsp;&nbsp;clocks_per_click&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;denominator&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;notated_32nd_notes_per_beat&nbsp;(int)<br>
&nbsp;&nbsp;&nbsp;&nbsp;numerator&nbsp;(int)<br>
KEY_SIGNATURE&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x59)<br>
&nbsp;&nbsp;&nbsp;&nbsp;key&nbsp;(str)<br>
SEQUENCER_SPECIFIC&nbsp;(midi&nbsp;meta&nbsp;0xff&nbsp;0x7f)<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;(memoryview)<br>
&nbsp;<br>
SYSEX&nbsp;&nbsp;0xf0<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;(memoryview)<br>
ESCAPE&nbsp;&nbsp;0xf7<br>
&nbsp;&nbsp;&nbsp;&nbsp;data&nbsp;(memoryview)<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="MidiEvent-__init__"><strong>__init__</strong></a>(self)</dt><dd><tt>Initializes&nbsp;<a href="#MidiEvent">MidiEvent</a>,&nbsp;all&nbsp;instances&nbsp;are&nbsp;assigned&nbsp;None&nbsp;as&nbsp;value,<br>
this&nbsp;is.&nbsp;This&nbsp;method&nbsp;is&nbsp;used&nbsp;internally&nbsp;by&nbsp;MidiParser.<br>
&nbsp;<br>
Usually&nbsp;you&nbsp;will&nbsp;not&nbsp;need&nbsp;to&nbsp;create&nbsp;an&nbsp;instance&nbsp;of&nbsp;<a href="#MidiEvent">MidiEvent</a>,<br>
<a href="#MidiEvent">MidiEvent</a>&nbsp;objects&nbsp;are&nbsp;returned&nbsp;by&nbsp;iterating&nbsp;over&nbsp;the&nbsp;<a href="#MidiFile">MidiFile</a><br>
<a href="builtins.html#object">object</a>.</tt></dd></dl>

<dl><dt><a name="MidiEvent-__str__"><strong>__str__</strong></a>(self)</dt><dd><tt>Standard&nbsp;method&nbsp;to&nbsp;translate&nbsp;the&nbsp;event&nbsp;information&nbsp;to&nbsp;a&nbsp;string,<br>
for&nbsp;example:<br>
&nbsp;&nbsp;&nbsp;&nbsp;print(event)<br>
&nbsp;&nbsp;&nbsp;&nbsp;or<br>
&nbsp;&nbsp;&nbsp;&nbsp;event_as_a_string&nbsp;=&nbsp;str(event)<br>
Returns&nbsp;a&nbsp;string&nbsp;with&nbsp;a&nbsp;description&nbsp;of&nbsp;the&nbsp;<a href="#MidiEvent">MidiEvent</a>,&nbsp;starting<br>
with&nbsp;tne&nbsp;event&nbsp;name&nbsp;in&nbsp;lowercase&nbsp;(note_on,&nbsp;note_off,&nbsp;pitchwheel,&nbsp;set_tempo,<br>
end_of_track,&nbsp;etc),&nbsp;delta&nbsp;time&nbsp;in&nbsp;midi&nbsp;ticks,&nbsp;delta&nbsp;time&nbsp;in&nbsp;microseconds,<br>
first&nbsp;few&nbsp;bytes&nbsp;of&nbsp;the&nbsp;raw&nbsp;data,&nbsp;and&nbsp;all&nbsp;properties<br>
that&nbsp;are&nbsp;allowed&nbsp;for&nbsp;the&nbsp;event&nbsp;type.&nbsp;For&nbsp;example,&nbsp;a&nbsp;"note&nbsp;on"&nbsp;event&nbsp;might<br>
be&nbsp;shown&nbsp;as:<br>
"note_on&nbsp;delta[miditicks]=10&nbsp;delta[usec]=9500&nbsp;note=60&nbsp;velocity=64&nbsp;channel=5"<br>
&nbsp;<br>
The&nbsp;order&nbsp;of&nbsp;the&nbsp;properties&nbsp;in&nbsp;the&nbsp;string&nbsp;may&nbsp;vary.</tt></dd></dl>

<dl><dt><a name="MidiEvent-copy"><strong>copy</strong></a>(self)</dt><dd><tt>Returns&nbsp;a&nbsp;deep&nbsp;copy&nbsp;(a&nbsp;complete&nbsp;independent&nbsp;copy)&nbsp;of&nbsp;the&nbsp;event.<br>
All&nbsp;values&nbsp;are&nbsp;equal&nbsp;to&nbsp;the&nbsp;original&nbsp;event.<br>
&nbsp;<br>
This&nbsp;can&nbsp;be&nbsp;useful&nbsp;to&nbsp;get&nbsp;a&nbsp;copy&nbsp;of&nbsp;the&nbsp;event&nbsp;in&nbsp;case&nbsp;of&nbsp;using<br>
the&nbsp;reuse_event_object=True&nbsp;option&nbsp;in&nbsp;the&nbsp;<a href="#MidiFile">MidiFile</a>.<br>
&nbsp;<br>
Example&nbsp;1:&nbsp;if&nbsp;you&nbsp;need&nbsp;a&nbsp;list&nbsp;of&nbsp;all&nbsp;MidiEvents<br>
in&nbsp;a&nbsp;file,&nbsp;then&nbsp;either&nbsp;use:<br>
&nbsp;&nbsp;&nbsp;&nbsp;event_list&nbsp;=&nbsp;[&nbsp;event&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid")&nbsp;]<br>
or&nbsp;use:<br>
&nbsp;&nbsp;&nbsp;&nbsp;event_list&nbsp;=&nbsp;[event.copy&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reuse_event_object=True)&nbsp;]<br>
&nbsp;<br>
The&nbsp;following&nbsp;code&nbsp;will&nbsp;give&nbsp;an&nbsp;unexpected&nbsp;result,&nbsp;because&nbsp;all<br>
elements&nbsp;in&nbsp;the&nbsp;list&nbsp;will&nbsp;be&nbsp;equal&nbsp;to&nbsp;the&nbsp;last&nbsp;event&nbsp;of&nbsp;the&nbsp;file:<br>
&nbsp;&nbsp;&nbsp;&nbsp;event_list&nbsp;=&nbsp;[event&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reuse_event_object=True)&nbsp;]</tt></dd></dl>

<dl><dt><a name="MidiEvent-is_meta"><strong>is_meta</strong></a>(self)</dt><dd><tt>Returns&nbsp;True&nbsp;if&nbsp;this&nbsp;is&nbsp;a&nbsp;Meta&nbsp;event,&nbsp;such&nbsp;as<br>
lyrics,&nbsp;set&nbsp;tempo&nbsp;or&nbsp;key&nbsp;signature.<br>
Returns&nbsp;False&nbsp;if&nbsp;this&nbsp;is&nbsp;a&nbsp;MIDI&nbsp;channel&nbsp;event,<br>
or&nbsp;a&nbsp;Sysex&nbsp;or&nbsp;Escape&nbsp;event.</tt></dd></dl>

<dl><dt><a name="MidiEvent-to_midi"><strong>to_midi</strong></a>(self)</dt><dd><tt>Returns&nbsp;the&nbsp;event&nbsp;as&nbsp;bytes,&nbsp;in&nbsp;a&nbsp;format&nbsp;that&nbsp;allows&nbsp;sending&nbsp;the<br>
data&nbsp;to&nbsp;a&nbsp;MIDI&nbsp;controller.<br>
&nbsp;<br>
to_midi&nbsp;will&nbsp;raise&nbsp;AttributeError&nbsp;if&nbsp;the&nbsp;event&nbsp;is&nbsp;for&nbsp;MIDI&nbsp;meta&nbsp;messages,&nbsp;these<br>
occur&nbsp;in&nbsp;MIDI&nbsp;files&nbsp;and&nbsp;are&nbsp;not&nbsp;normally&nbsp;sent&nbsp;to&nbsp;MIDI&nbsp;controllers.</tt></dd></dl>

<hr>
Readonly properties defined here:<br>
<dl><dt><strong>channel</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;channel&nbsp;number&nbsp;for&nbsp;the&nbsp;event,&nbsp;0-15.<br>
&nbsp;<br>
channel&nbsp;property&nbsp;available&nbsp;for:&nbsp;&nbsp;NOTE_OFF&nbsp;NOTE_ON<br>
POLYTOUCH&nbsp;CONTROL_CHANGE&nbsp;PROGRAM_CHANGE&nbsp;AFTERTOUCH<br>
CHANNEL_PREFIX</tt></dd>
</dl>
<dl><dt><strong>clocks_per_click</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;clocks_per_click&nbsp;for&nbsp;the&nbsp;TIME_SIGNATURE&nbsp;meta&nbsp;messages,&nbsp;0-255.</tt></dd>
</dl>
<dl><dt><strong>control</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;value&nbsp;for&nbsp;the&nbsp;controller&nbsp;0-127&nbsp;for&nbsp;a&nbsp;CONTROL_CHANGE&nbsp;event.</tt></dd>
</dl>
<dl><dt><strong>data</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;raw&nbsp;data&nbsp;for&nbsp;the&nbsp;underlying&nbsp;message,&nbsp;with&nbsp;no&nbsp;transofrmations,<br>
as&nbsp;a&nbsp;memoryview,&nbsp;without&nbsp;the&nbsp;event&nbsp;status&nbsp;byte&nbsp;or&nbsp;meta&nbsp;prefix.<br>
&nbsp;<br>
For&nbsp;midi&nbsp;channel&nbsp;events,&nbsp;the&nbsp;length&nbsp;is&nbsp;either&nbsp;1&nbsp;or&nbsp;2&nbsp;bytes<br>
according&nbsp;to&nbsp;the&nbsp;event&nbsp;type,&nbsp;for&nbsp;example&nbsp;a&nbsp;"note&nbsp;on"&nbsp;event&nbsp;always<br>
has&nbsp;2&nbsp;bytes&nbsp;of&nbsp;data.<br>
For&nbsp;a&nbsp;meta&nbsp;or&nbsp;sysex&nbsp;event,&nbsp;"data"&nbsp;contains&nbsp;the&nbsp;payload&nbsp;of&nbsp;the&nbsp;message,<br>
that&nbsp;is,&nbsp;without&nbsp;meta&nbsp;prefix&nbsp;and&nbsp;length.<br>
For&nbsp;sysex&nbsp;and&nbsp;escape&nbsp;events,&nbsp;the&nbsp;status&nbsp;(0xf0,&nbsp;xf7)&nbsp;is&nbsp;not&nbsp;included.<br>
&nbsp;<br>
The&nbsp;main&nbsp;purpose&nbsp;is&nbsp;to&nbsp;retrieve&nbsp;message&nbsp;data&nbsp;for&nbsp;sysex&nbsp;and&nbsp;escape&nbsp;events.</tt></dd>
</dl>
<dl><dt><strong>denominator</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;denominator&nbsp;for&nbsp;the&nbsp;TIME_SIGNATURE&nbsp;meta&nbsp;messages,&nbsp;0-255.</tt></dd>
</dl>
<dl><dt><strong>frame_rate</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;frame&nbsp;for&nbsp;the&nbsp;SMPTE_OFFSET&nbsp;meta&nbsp;messages,<br>
which&nbsp;can&nbsp;be&nbsp;24,&nbsp;25,&nbsp;29.97&nbsp;or&nbsp;30.<br>
&nbsp;<br>
An&nbsp;invalid&nbsp;value&nbsp;in&nbsp;the&nbsp;MIDI&nbsp;file&nbsp;will&nbsp;raise&nbsp;a&nbsp;IndexError</tt></dd>
</dl>
<dl><dt><strong>frames</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;frames&nbsp;for&nbsp;the&nbsp;SMPTE_OFFSET&nbsp;meta&nbsp;message,<br>
usually&nbsp;from&nbsp;0&nbsp;to&nbsp;255.</tt></dd>
</dl>
<dl><dt><strong>hours</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;hour&nbsp;for&nbsp;the&nbsp;SMPTE_OFFSET&nbsp;meta&nbsp;message,<br>
usually&nbsp;from&nbsp;0&nbsp;to&nbsp;23.</tt></dd>
</dl>
<dl><dt><strong>key</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;key,&nbsp;as&nbsp;str,&nbsp;for&nbsp;a&nbsp;KEY_SIGNATURE&nbsp;meta&nbsp;event.<br>
Key&nbsp;names&nbsp;are&nbsp;"american"&nbsp;key&nbsp;names.<br>
&nbsp;<br>
For&nbsp;mayor&nbsp;keys:<br>
C,&nbsp;D,&nbsp;E,&nbsp;F,&nbsp;G,&nbsp;A,&nbsp;B,&nbsp;C#,&nbsp;F#,&nbsp;Cb,&nbsp;Db,&nbsp;Eb,&nbsp;Gb,&nbsp;Ab<br>
&nbsp;<br>
For&nbsp;minor&nbsp;keys:<br>
Cm,&nbsp;Dm,&nbsp;Em,&nbsp;Fm,&nbsp;Gm,&nbsp;Am,&nbsp;Bm,&nbsp;C#m,&nbsp;F#m,&nbsp;Cbm,&nbsp;Dbm,&nbsp;Ebm,&nbsp;Gbm,&nbsp;Abm<br>
&nbsp;<br>
If&nbsp;the&nbsp;midi&nbsp;message&nbsp;contains&nbsp;a&nbsp;value&nbsp;out&nbsp;of&nbsp;range,&nbsp;a&nbsp;ValueError<br>
is&nbsp;raised.&nbsp;The&nbsp;raw&nbsp;data&nbsp;can&nbsp;be&nbsp;read&nbsp;with&nbsp;the&nbsp;data&nbsp;property.</tt></dd>
</dl>
<dl><dt><strong>minutes</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;minutes&nbsp;for&nbsp;the&nbsp;SMPTE_OFFSET&nbsp;meta&nbsp;message,<br>
usually&nbsp;from&nbsp;0&nbsp;to&nbsp;59.</tt></dd>
</dl>
<dl><dt><strong>name</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;text&nbsp;for&nbsp;a&nbsp;meta&nbsp;events.<br>
&nbsp;<br>
name&nbsp;property&nbsp;available&nbsp;for:&nbsp;&nbsp;TRACK_NAME&nbsp;INSTRUMENT_NAME&nbsp;PROGRAM_NAME&nbsp;DEVICE_NAME<br>
&nbsp;<br>
See&nbsp;text&nbsp;property&nbsp;for&nbsp;description&nbsp;of&nbsp;text&nbsp;conversion.<br>
&nbsp;<br>
The&nbsp;raw&nbsp;data&nbsp;can&nbsp;be&nbsp;retrieved&nbsp;using&nbsp;the&nbsp;data&nbsp;property.</tt></dd>
</dl>
<dl><dt><strong>notated_32nd_notes_per_beat</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;notated_32nd_notes_per_beat&nbsp;for&nbsp;the&nbsp;TIME_SIGNATURE&nbsp;meta&nbsp;messages,<br>
0-255.</tt></dd>
</dl>
<dl><dt><strong>note</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;note&nbsp;number&nbsp;for&nbsp;the&nbsp;event,&nbsp;usually&nbsp;0-127.<br>
&nbsp;<br>
note&nbsp;property&nbsp;available&nbsp;for:&nbsp;&nbsp;NOTE_OFF&nbsp;NOTE_ON&nbsp;POLYTOUCH</tt></dd>
</dl>
<dl><dt><strong>number</strong></dt>
<dd><tt>Returns&nbsp;numbef&nbsp;for&nbsp;a&nbsp;SEQUENCE_NUMBER&nbsp;meta&nbsp;event.<br>
Values&nbsp;range&nbsp;from&nbsp;0&nbsp;to&nbsp;2**24.</tt></dd>
</dl>
<dl><dt><strong>numerator</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;numerator&nbsp;for&nbsp;the&nbsp;TIME_SIGNATURE&nbsp;meta&nbsp;messages,&nbsp;0-255.</tt></dd>
</dl>
<dl><dt><strong>pitch</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;pitch&nbsp;for&nbsp;a&nbsp;PITCHWHEEL&nbsp;midi&nbsp;channel&nbsp;event.<br>
&nbsp;<br>
-8192&nbsp;is&nbsp;the&nbsp;lowest&nbsp;value&nbsp;possible,&nbsp;0&nbsp;(zero)&nbsp;means&nbsp;"no&nbsp;pitch&nbsp;bend"<br>
and&nbsp;8191&nbsp;is&nbsp;the&nbsp;highest&nbsp;possible&nbsp;value.</tt></dd>
</dl>
<dl><dt><strong>port</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;port&nbsp;number&nbsp;&nbsp;0-256&nbsp;for&nbsp;a&nbsp;meta&nbsp;MIDI_PORT&nbsp;message</tt></dd>
</dl>
<dl><dt><strong>program</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;program&nbsp;number&nbsp;0-127&nbsp;for&nbsp;a&nbsp;PROGRAM_CHANGE&nbsp;event.</tt></dd>
</dl>
<dl><dt><strong>seconds</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;seconds&nbsp;for&nbsp;the&nbsp;SMPTE_OFFSET&nbsp;meta&nbsp;message,<br>
usually&nbsp;from&nbsp;0&nbsp;to&nbsp;59.</tt></dd>
</dl>
<dl><dt><strong>status</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;event&nbsp;status.&nbsp;For&nbsp;midi&nbsp;channel&nbsp;events,&nbsp;such&nbsp;as&nbsp;note&nbsp;on,&nbsp;note&nbsp;off,<br>
program&nbsp;change,&nbsp;the&nbsp;lower&nbsp;nibble&nbsp;(lower&nbsp;4&nbsp;bits)&nbsp;are&nbsp;cleared&nbsp;(set&nbsp;to&nbsp;zero).<br>
For&nbsp;a&nbsp;meta&nbsp;event,&nbsp;this&nbsp;is&nbsp;the&nbsp;meta&nbsp;type,&nbsp;for&nbsp;example&nbsp;0x2f&nbsp;for&nbsp;"end&nbsp;of&nbsp;track".<br>
&nbsp;<br>
Available&nbsp;for&nbsp;all&nbsp;possible&nbsp;events.&nbsp;For&nbsp;custom&nbsp;or&nbsp;proprietary&nbsp;meta&nbsp;events,&nbsp;this<br>
will&nbsp;be&nbsp;the&nbsp;meta&nbsp;type&nbsp;of&nbsp;that&nbsp;event.<br>
&nbsp;<br>
Examples:<br>
&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;event.status&nbsp;==&nbsp;umidiparser.NOTE_OFF:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;....&nbsp;process&nbsp;note&nbsp;off&nbsp;event&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;elif&nbsp;event.status&nbsp;==&nbsp;umidiparser.KEY_SIGNATURE:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;process&nbsp;key&nbsp;signature&nbsp;meta&nbsp;event&nbsp;...<br>
&nbsp;<br>
Possible&nbsp;values<br>
All&nbsp;names&nbsp;are&nbsp;global&nbsp;constants&nbsp;in&nbsp;this&nbsp;module&nbsp;e.g.&nbsp;umidiparser.NOTE_OFF<br>
NOTE_OFF&nbsp;0x80<br>
NOTE_ON&nbsp;0x90<br>
POLYTOUCH&nbsp;0xa0<br>
CONTROL_CHANGE&nbsp;0xb0<br>
PROGRAM_CHANGE&nbsp;0xc0<br>
AFTERTOUCH&nbsp;0xd0<br>
PITCHWHEEL&nbsp;0xe0<br>
&nbsp;<br>
Meta&nbsp;messages&nbsp;(all&nbsp;with&nbsp;prefix&nbsp;0xff)<br>
SEQUENCE_NUMBER&nbsp;0x00<br>
TEXT&nbsp;0x01<br>
COPYRIGHT&nbsp;0x02<br>
TRACK_NAME&nbsp;0x03<br>
INSTRUMENT_NAME&nbsp;0x04<br>
LYRICS&nbsp;0x05<br>
MARKER&nbsp;0x06<br>
CUE_MARKER&nbsp;0x07<br>
PROGRAM_NAME&nbsp;0x08<br>
DEVICE_NAME&nbsp;0x09<br>
CHANNEL_PREFIX&nbsp;0x20<br>
MIDI_PORT&nbsp;0x21<br>
END_OF_TRACK&nbsp;0x2f<br>
SET_TEMPO&nbsp;0x51<br>
SMPTE_OFFSET&nbsp;0x54<br>
TIME_SIGNATURE&nbsp;0x58<br>
KEY_SIGNATURE&nbsp;0x59<br>
SEQUENCER_SPECIFIC&nbsp;0x7f<br>
&nbsp;<br>
Sysex/escape&nbsp;events<br>
SYSEX&nbsp;0xf0<br>
ESCAPE&nbsp;0xf7</tt></dd>
</dl>
<dl><dt><strong>sub_frames</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;sub&nbsp;frames&nbsp;for&nbsp;the&nbsp;SMPTE_OFFSET&nbsp;meta&nbsp;message,<br>
usually&nbsp;from&nbsp;0&nbsp;to&nbsp;59.</tt></dd>
</dl>
<dl><dt><strong>tempo</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;tempo&nbsp;(0&nbsp;to&nbsp;2**32&nbsp;microseconds&nbsp;per&nbsp;quarter&nbsp;beat)<br>
for&nbsp;a&nbsp;SET_TEMPO&nbsp;meta&nbsp;event.<br>
This&nbsp;module&nbsp;interprets&nbsp;the&nbsp;tempo&nbsp;event&nbsp;before&nbsp;returning&nbsp;it,&nbsp;so<br>
the&nbsp;following&nbsp;events&nbsp;returned&nbsp;will&nbsp;have&nbsp;their&nbsp;delta_us&nbsp;property<br>
calculated&nbsp;with&nbsp;the&nbsp;new&nbsp;tempo&nbsp;value.</tt></dd>
</dl>
<dl><dt><strong>text</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;text&nbsp;for&nbsp;a&nbsp;meta&nbsp;events.<br>
&nbsp;<br>
text&nbsp;property&nbsp;is&nbsp;available&nbsp;for:&nbsp;&nbsp;TEXT&nbsp;COPYRIGHT&nbsp;LYRICS&nbsp;MARKER&nbsp;CUE_MARKER<br>
&nbsp;<br>
In&nbsp;MIDI&nbsp;files,&nbsp;text&nbsp;is&nbsp;stored&nbsp;as&nbsp;"extended&nbsp;ASCII",&nbsp;this&nbsp;is<br>
decoded&nbsp;with&nbsp;the&nbsp;iso8859_1&nbsp;encoding.<br>
&nbsp;<br>
The&nbsp;raw&nbsp;data&nbsp;can&nbsp;be&nbsp;retrieved&nbsp;using&nbsp;the&nbsp;data&nbsp;property.</tt></dd>
</dl>
<dl><dt><strong>value</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;the&nbsp;value&nbsp;in&nbsp;the&nbsp;event.<br>
&nbsp;<br>
value&nbsp;property&nbsp;available&nbsp;for:&nbsp;&nbsp;AFTERTOUCH,&nbsp;CONTROL_CHANGE,&nbsp;POLYTOUCH</tt></dd>
</dl>
<dl><dt><strong>velocity</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;velocity&nbsp;fot&nbsp;the&nbsp;event,&nbsp;usually&nbsp;0-127.<br>
&nbsp;<br>
velocity&nbsp;property&nbsp;available&nbsp;for:&nbsp;&nbsp;NOTE_OFF&nbsp;NOTE_ON</tt></dd>
</dl>
<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table> <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="MidiFile">class <strong>MidiFile</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt><a href="#MidiFile">MidiFile</a>(filename,&nbsp;buffer_size=100,&nbsp;reuse_event_object=False)<br>
&nbsp;<br>
Parses&nbsp;a&nbsp;MIDI&nbsp;file.<br>
Once&nbsp;initialized,&nbsp;you&nbsp;can&nbsp;iterate&nbsp;through&nbsp;the&nbsp;events&nbsp;of&nbsp;the&nbsp;file&nbsp;or<br>
tnrough&nbsp;the&nbsp;events&nbsp;of&nbsp;a&nbsp;certain&nbsp;track,&nbsp;see&nbsp;__iter__&nbsp;and&nbsp;play&nbsp;methods.<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="MidiFile-__init__"><strong>__init__</strong></a>(self, filename, buffer_size=100, reuse_event_object=False)</dt><dd><tt>filename<br>
&nbsp;<br>
The&nbsp;name&nbsp;of&nbsp;a&nbsp;MIDI&nbsp;file,&nbsp;usually&nbsp;a&nbsp;.mid&nbsp;or&nbsp;.rtx&nbsp;MIDI&nbsp;file.<br>
The&nbsp;MIDI&nbsp;file&nbsp;will&nbsp;always&nbsp;be&nbsp;opened&nbsp;read&nbsp;only.<br>
&nbsp;<br>
buffer_size=100<br>
&nbsp;<br>
The&nbsp;buffer&nbsp;size&nbsp;that&nbsp;will&nbsp;be&nbsp;allocated&nbsp;for&nbsp;each&nbsp;track.<br>
In&nbsp;order&nbsp;to&nbsp;process&nbsp;files&nbsp;larger&nbsp;than&nbsp;the&nbsp;available&nbsp;RAM,<br>
buffer_size=n&nbsp;will&nbsp;allocate&nbsp;"n"&nbsp;bytes&nbsp;of&nbsp;buffer&nbsp;for<br>
each&nbsp;track,&nbsp;and&nbsp;read&nbsp;each&nbsp;tracks&nbsp;in&nbsp;"n"&nbsp;byte&nbsp;portions&nbsp;during&nbsp;the<br>
processing&nbsp;of&nbsp;the&nbsp;file,&nbsp;i.e.&nbsp;while&nbsp;iterating&nbsp;through&nbsp;the&nbsp;events.&nbsp;This&nbsp;will<br>
need&nbsp;one&nbsp;file&nbsp;descriptor&nbsp;(one&nbsp;open&nbsp;file)&nbsp;for&nbsp;each&nbsp;track,&nbsp;but&nbsp;will<br>
consume&nbsp;only&nbsp;a&nbsp;fraction&nbsp;of&nbsp;RAM&nbsp;needed&nbsp;for&nbsp;the&nbsp;processing&nbsp;of&nbsp;a&nbsp;file,<br>
as&nbsp;opposed&nbsp;to&nbsp;reading&nbsp;the&nbsp;file&nbsp;into&nbsp;memory&nbsp;with&nbsp;buffer_size=0.<br>
A&nbsp;buffer&nbsp;size&nbsp;of&nbsp;less&nbsp;than&nbsp;10&nbsp;bytes&nbsp;will&nbsp;increase&nbsp;CPU&nbsp;overhead&nbsp;and&nbsp;is&nbsp;not<br>
recommended.&nbsp;A&nbsp;buffer&nbsp;size&nbsp;much&nbsp;larger&nbsp;than&nbsp;100&nbsp;will&nbsp;probably&nbsp;not&nbsp;give&nbsp;a<br>
relevant&nbsp;performance&nbsp;advantage,&nbsp;unless&nbsp;the&nbsp;device&nbsp;where&nbsp;the&nbsp;file<br>
resides&nbsp;is&nbsp;slow.<br>
&nbsp;<br>
If&nbsp;buffer_size=0,&nbsp;all&nbsp;tracks&nbsp;will&nbsp;be&nbsp;read&nbsp;to&nbsp;memory.<br>
This&nbsp;will&nbsp;need&nbsp;as&nbsp;much&nbsp;RAM&nbsp;as&nbsp;the&nbsp;file&nbsp;size&nbsp;of&nbsp;a&nbsp;complete&nbsp;MIDI&nbsp;file.<br>
In&nbsp;this&nbsp;case,&nbsp;the&nbsp;time&nbsp;needed&nbsp;to&nbsp;process&nbsp;each&nbsp;event&nbsp;will&nbsp;not&nbsp;depend&nbsp;on<br>
file&nbsp;access&nbsp;nd&nbsp;will&nbsp;be&nbsp;both&nbsp;faster&nbsp;and&nbsp;more&nbsp;dependable&nbsp;than&nbsp;using&nbsp;a<br>
buffer_size&nbsp;different&nbsp;to&nbsp;0,&nbsp;if&nbsp;the&nbsp;device&nbsp;where&nbsp;the&nbsp;file&nbsp;resides&nbsp;is&nbsp;slow.<br>
&nbsp;<br>
The&nbsp;default&nbsp;value&nbsp;for&nbsp;buffer_size&nbsp;is&nbsp;100&nbsp;bytes.<br>
&nbsp;<br>
reuse_event_object=False<br>
&nbsp;<br>
With&nbsp;the&nbsp;default&nbsp;value&nbsp;of&nbsp;False,&nbsp;for&nbsp;each&nbsp;call&nbsp;a&nbsp;new&nbsp;<a href="#MidiEvent">MidiEvent</a>&nbsp;is&nbsp;returned,<br>
this&nbsp;is,&nbsp;if&nbsp;you&nbsp;do:<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid"):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;process&nbsp;each&nbsp;event&nbsp;...<br>
&nbsp;<br>
then&nbsp;in&nbsp;each&nbsp;iteration&nbsp;of&nbsp;the&nbsp;loop&nbsp;you&nbsp;get&nbsp;a&nbsp;different,&nbsp;and&nbsp;new,&nbsp;<a href="#MidiEvent">MidiEvent</a>.<br>
This&nbsp;is&nbsp;the&nbsp;normal&nbsp;and&nbsp;expected&nbsp;behaviour&nbsp;for&nbsp;Python&nbsp;iterators.<br>
&nbsp;<br>
If&nbsp;you&nbsp;need&nbsp;higher&nbsp;processing&nbsp;speed,&nbsp;and&nbsp;if&nbsp;you&nbsp;don't&nbsp;want&nbsp;to<br>
fragment&nbsp;RAM&nbsp;heap&nbsp;space,&nbsp;use:<br>
&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid",&nbsp;reuse_event_object=True):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;process&nbsp;each&nbsp;event&nbsp;....<br>
&nbsp;<br>
In&nbsp;this&nbsp;case,&nbsp;for&nbsp;each&nbsp;iteration&nbsp;of&nbsp;the&nbsp;loop,&nbsp;the&nbsp;same&nbsp;<a href="#MidiEvent">MidiEvent</a>&nbsp;is&nbsp;returned,<br>
and&nbsp;is&nbsp;overwritten&nbsp;with&nbsp;the&nbsp;last&nbsp;data.&nbsp;The&nbsp;event&nbsp;data&nbsp;will&nbsp;not&nbsp;be<br>
changed&nbsp;in&nbsp;the&nbsp;body&nbsp;of&nbsp;the&nbsp;for&nbsp;loop.&nbsp;However,&nbsp;if&nbsp;you&nbsp;want&nbsp;to&nbsp;store&nbsp;an&nbsp;event<br>
for&nbsp;later&nbsp;use,&nbsp;&nbsp;you'll&nbsp;have&nbsp;to&nbsp;use&nbsp;event.copy.<br>
&nbsp;<br>
All&nbsp;combinations&nbsp;of&nbsp;reuse_event_object&nbsp;and&nbsp;buffer_size&nbsp;are&nbsp;valid.<br>
&nbsp;<br>
Instance&nbsp;variables:<br>
&nbsp;<br>
tracks<br>
List&nbsp;<a href="builtins.html#object">object</a>&nbsp;with&nbsp;the&nbsp;tracks&nbsp;of&nbsp;the&nbsp;file.&nbsp;len(midifile.tracks)&nbsp;is&nbsp;the&nbsp;number&nbsp;of&nbsp;tracks.<br>
To&nbsp;get&nbsp;the&nbsp;events&nbsp;in&nbsp;an&nbsp;individual&nbsp;track,&nbsp;use:<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid").tracks[3]:<br>
&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;process&nbsp;events&nbsp;of&nbsp;track&nbsp;3&nbsp;of&nbsp;the&nbsp;list&nbsp;....<br>
&nbsp;<br>
Exceptions:<br>
The&nbsp;file&nbsp;must&nbsp;start&nbsp;with&nbsp;a&nbsp;standard&nbsp;MIDI&nbsp;file&nbsp;header&nbsp;(MThd),&nbsp;if&nbsp;not,&nbsp;a<br>
ValueError&nbsp;is&nbsp;raised.<br>
The&nbsp;MIDI&nbsp;header&nbsp;chunk&nbsp;must&nbsp;be&nbsp;at&nbsp;least&nbsp;6&nbsp;bytes&nbsp;long,&nbsp;or&nbsp;a&nbsp;ValueError<br>
is&nbsp;raised.<br>
ValueError&nbsp;is&nbsp;raised&nbsp;if&nbsp;no&nbsp;header&nbsp;present,&nbsp;or&nbsp;too&nbsp;short.<br>
ValueError&nbsp;is&nbsp;raised&nbsp;if&nbsp;the&nbsp;header&nbsp;contains&nbsp;SMPTE&nbsp;time&nbsp;codes&nbsp;(not&nbsp;supported).<br>
Chunks&nbsp;after&nbsp;the&nbsp;header&nbsp;that&nbsp;are&nbsp;not&nbsp;tracks<br>
(i.e.&nbsp;don't&nbsp;have&nbsp;a&nbsp;"MTrk"&nbsp;MIDI&nbsp;header)&nbsp;are&nbsp;ignored.</tt></dd></dl>

<dl><dt><a name="MidiFile-__iter__"><strong>__iter__</strong></a>(self)</dt><dd><tt>To&nbsp;get&nbsp;all&nbsp;the&nbsp;events&nbsp;of&nbsp;a&nbsp;format&nbsp;type&nbsp;0&nbsp;or&nbsp;format&nbsp;type&nbsp;1&nbsp;MIDI&nbsp;file,<br>
iterate&nbsp;through&nbsp;the&nbsp;<a href="#MidiFile">MidiFile</a>&nbsp;<a href="builtins.html#object">object</a>,&nbsp;for&nbsp;example:<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid"):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(event)<br>
&nbsp;<br>
&nbsp;<br>
Events&nbsp;will&nbsp;be&nbsp;returned&nbsp;in&nbsp;ascending&nbsp;order&nbsp;in&nbsp;time.&nbsp;For&nbsp;format&nbsp;type&nbsp;1<br>
multitrack&nbsp;files,&nbsp;all&nbsp;tracks&nbsp;are&nbsp;merged.<br>
&nbsp;<br>
The&nbsp;event.delta_us&nbsp;property&nbsp;is&nbsp;calculated&nbsp;as&nbsp;the<br>
time&nbsp;in&nbsp;microseconds&nbsp;between&nbsp;last&nbsp;and&nbsp;this&nbsp;event,&nbsp;taking&nbsp;into&nbsp;account&nbsp;both<br>
the&nbsp;set&nbsp;tempo&nbsp;meta&nbsp;events&nbsp;and&nbsp;the&nbsp;"MIDI&nbsp;ticks&nbsp;per&nbsp;quarter&nbsp;note"<br>
parameter&nbsp;in&nbsp;the&nbsp;MIDI&nbsp;file&nbsp;header.&nbsp;For&nbsp;type&nbsp;1&nbsp;files,&nbsp;all&nbsp;set&nbsp;tempo&nbsp;meta<br>
events&nbsp;may&nbsp;be&nbsp;in&nbsp;track&nbsp;0&nbsp;(as&nbsp;it&nbsp;is&nbsp;usually&nbsp;done),&nbsp;or&nbsp;they&nbsp;may&nbsp;occur&nbsp;in&nbsp;any&nbsp;track.<br>
&nbsp;<br>
For&nbsp;a&nbsp;multitrack&nbsp;file,&nbsp;event.delta_us&nbsp;is&nbsp;the&nbsp;time&nbsp;difference&nbsp;with&nbsp;the<br>
previous&nbsp;event,&nbsp;which&nbsp;may&nbsp;be&nbsp;in&nbsp;the&nbsp;same&nbsp;or&nbsp;a&nbsp;different&nbsp;track.<br>
&nbsp;<br>
For&nbsp;a&nbsp;format&nbsp;type&nbsp;2&nbsp;MIDI&nbsp;file,&nbsp;a&nbsp;single&nbsp;track&nbsp;must&nbsp;be&nbsp;selected,&nbsp;track<br>
numbers&nbsp;range&nbsp;from&nbsp;0&nbsp;to&nbsp;len(<a href="#MidiFile">MidiFile</a>.tracks)-1<br>
&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid").tracks[5]:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;process&nbsp;event&nbsp;...<br>
&nbsp;<br>
When&nbsp;parsing&nbsp;a&nbsp;file&nbsp;format&nbsp;2&nbsp;track,&nbsp;then&nbsp;only&nbsp;the&nbsp;set&nbsp;tempo<br>
events&nbsp;of&nbsp;that&nbsp;track&nbsp;are&nbsp;processed&nbsp;to&nbsp;calculate&nbsp;delta_us.<br>
&nbsp;<br>
To&nbsp;process&nbsp;each&nbsp;event&nbsp;at&nbsp;the&nbsp;time&nbsp;due,&nbsp;a&nbsp;simple&nbsp;version&nbsp;could&nbsp;be:<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid"):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time.sleep_us(&nbsp;event.delta_us&nbsp;)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;process&nbsp;the&nbsp;event&nbsp;...<br>
&nbsp;<br>
To&nbsp;implement&nbsp;this&nbsp;function&nbsp;with&nbsp;time&nbsp;error&nbsp;compensation,&nbsp;use&nbsp;the<br>
<a href="#MidiFile">MidiFile</a>.play&nbsp;method.<br>
&nbsp;<br>
In&nbsp;all&nbsp;cases,&nbsp;only&nbsp;one&nbsp;end&nbsp;of&nbsp;track&nbsp;meta&nbsp;event&nbsp;is&nbsp;returned<br>
to&nbsp;the&nbsp;caller&nbsp;when&nbsp;the&nbsp;end&nbsp;of&nbsp;file&nbsp;is&nbsp;reached.<br>
Events&nbsp;beyond&nbsp;a&nbsp;end&nbsp;of&nbsp;track&nbsp;event&nbsp;are&nbsp;ignored.<br>
&nbsp;<br>
Exceptions:<br>
RuntimeError&nbsp;is&nbsp;raised&nbsp;if&nbsp;format&nbsp;type&nbsp;2&nbsp;is&nbsp;processed&nbsp;with&nbsp;this&nbsp;method.<br>
Use&nbsp;the&nbsp;<a href="#MidiFile">MidiFile</a>.tracks[n]&nbsp;to&nbsp;iterate&nbsp;through&nbsp;a&nbsp;single&nbsp;track.</tt></dd></dl>

<dl><dt><a name="MidiFile-length_us"><strong>length_us</strong></a>(self)</dt><dd><tt>Returns&nbsp;the&nbsp;length&nbsp;of&nbsp;the&nbsp;<a href="#MidiFile">MidiFile</a>&nbsp;in&nbsp;microseconds.<br>
&nbsp;<br>
Beware,&nbsp;on&nbsp;a&nbsp;slow&nbsp;microcontroller,&nbsp;calculating&nbsp;the&nbsp;length&nbsp;of<br>
a&nbsp;large&nbsp;MIDI&nbsp;file&nbsp;might&nbsp;take&nbsp;a&nbsp;several&nbsp;of&nbsp;seconds.<br>
This&nbsp;is&nbsp;due&nbsp;to&nbsp;the&nbsp;way&nbsp;MIDI&nbsp;files&nbsp;work,&nbsp;in&nbsp;order&nbsp;to<br>
get&nbsp;the&nbsp;playing&nbsp;length,&nbsp;this&nbsp;method&nbsp;needs&nbsp;to&nbsp;parse<br>
the&nbsp;entire&nbsp;file,&nbsp;compute&nbsp;and&nbsp;sum&nbsp;the&nbsp;time&nbsp;differences&nbsp;of&nbsp;all&nbsp;events.<br>
&nbsp;<br>
Exceptions:<br>
RuntimeError&nbsp;for&nbsp;format&nbsp;type&nbsp;2&nbsp;files.&nbsp;It&nbsp;is&nbsp;not&nbsp;possible&nbsp;to&nbsp;calculate&nbsp;the<br>
playing&nbsp;time&nbsp;of&nbsp;a&nbsp;format&nbsp;2&nbsp;file,&nbsp;since&nbsp;for&nbsp;format&nbsp;2&nbsp;files,<br>
the&nbsp;tracks&nbsp;are&nbsp;not&nbsp;meant&nbsp;to&nbsp;be&nbsp;merged.</tt></dd></dl>

<dl><dt><a name="MidiFile-play"><strong>play</strong></a>(self, track_number=None)</dt><dd><tt>Iterate&nbsp;through&nbsp;the&nbsp;events&nbsp;of&nbsp;a&nbsp;MIDI&nbsp;file&nbsp;or&nbsp;a&nbsp;track,<br>
sleep&nbsp;until&nbsp;the&nbsp;event&nbsp;has&nbsp;to&nbsp;take&nbsp;place,&nbsp;and<br>
yield&nbsp;the&nbsp;event.<br>
&nbsp;<br>
Parameters<br>
track_number=None<br>
&nbsp;<br>
If&nbsp;track_number=None,&nbsp;and&nbsp;the&nbsp;MIDI&nbsp;file&nbsp;is&nbsp;format&nbsp;0&nbsp;or&nbsp;1,<br>
play&nbsp;the&nbsp;complete&nbsp;file.&nbsp;Merge&nbsp;all&nbsp;tracks.<br>
&nbsp;<br>
If&nbsp;a&nbsp;track&nbsp;number&nbsp;is&nbsp;specified,&nbsp;then&nbsp;that&nbsp;track&nbsp;number&nbsp;is&nbsp;played.&nbsp;This<br>
is&nbsp;intended&nbsp;for&nbsp;use&nbsp;with&nbsp;format&nbsp;type&nbsp;2&nbsp;files,&nbsp;to&nbsp;play&nbsp;a&nbsp;certain&nbsp;track.<br>
&nbsp;<br>
Example:<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid").<a href="#MidiFile-play">play</a>():<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;....&nbsp;process&nbsp;the&nbsp;event&nbsp;...<br>
The&nbsp;play&nbsp;function&nbsp;will&nbsp;wait&nbsp;the&nbsp;necessary&nbsp;time&nbsp;between&nbsp;iterations<br>
so&nbsp;that&nbsp;each&nbsp;event&nbsp;is&nbsp;yielded&nbsp;on&nbsp;time&nbsp;to&nbsp;be&nbsp;processed.<br>
&nbsp;<br>
This&nbsp;function&nbsp;compensates&nbsp;for&nbsp;the&nbsp;accumulated&nbsp;error&nbsp;in&nbsp;the<br>
processing&nbsp;of&nbsp;each&nbsp;event.&nbsp;Since&nbsp;sleep&nbsp;functions&nbsp;will&nbsp;sleep<br>
AT&nbsp;LEAST&nbsp;the&nbsp;time&nbsp;specified,&nbsp;normally&nbsp;the&nbsp;time&nbsp;slept&nbsp;will&nbsp;be&nbsp;longer.&nbsp;This<br>
means,&nbsp;for&nbsp;a&nbsp;long&nbsp;file&nbsp;of&nbsp;several&nbsp;thousand&nbsp;events,&nbsp;events&nbsp;may&nbsp;get&nbsp;ever&nbsp;later.<br>
This&nbsp;is&nbsp;noticeable&nbsp;especially&nbsp;of&nbsp;another&nbsp;thread&nbsp;or&nbsp;process&nbsp;is&nbsp;active,&nbsp;or<br>
if&nbsp;the&nbsp;processing&nbsp;of&nbsp;each&nbsp;event&nbsp;takes&nbsp;significant&nbsp;time.<br>
Even&nbsp;so,&nbsp;since&nbsp;play&nbsp;uses&nbsp;the&nbsp;sleep_us&nbsp;function,&nbsp;sometimes<br>
you&nbsp;may&nbsp;get&nbsp;the&nbsp;event&nbsp;a&nbsp;bit&nbsp;later&nbsp;than&nbsp;the&nbsp;correct&nbsp;time.<br>
&nbsp;<br>
For&nbsp;Micropython,&nbsp;time.sleep_us()&nbsp;is&nbsp;used.&nbsp;For&nbsp;CPython&nbsp;time.sleep()&nbsp;is&nbsp;used.</tt></dd></dl>

<hr>
Readonly properties defined here:<br>
<dl><dt><strong>buffer_size</strong></dt>
<dd><tt>Return&nbsp;the&nbsp;buffer_size&nbsp;value.&nbsp;0=tracks&nbsp;are&nbsp;buffered&nbsp;entirely&nbsp;in&nbsp;RAM.<br>
A&nbsp;number,&nbsp;for&nbsp;example&nbsp;buffer_size=100&nbsp;means&nbsp;a&nbsp;buffer&nbsp;of&nbsp;100&nbsp;bytes&nbsp;is<br>
allocated&nbsp;per&nbsp;track&nbsp;to&nbsp;read&nbsp;the&nbsp;track&nbsp;data.<br>
&nbsp;<br>
This&nbsp;allows&nbsp;to&nbsp;read&nbsp;large&nbsp;MIDI&nbsp;files&nbsp;efficiently&nbsp;on&nbsp;microcontrollers&nbsp;with&nbsp;small&nbsp;RAM.</tt></dd>
</dl>
<dl><dt><strong>filename</strong></dt>
<dd><tt>Return&nbsp;the&nbsp;file&nbsp;name&nbsp;of&nbsp;the&nbsp;MIDI&nbsp;file,&nbsp;with&nbsp;absolute&nbsp;path.</tt></dd>
</dl>
<dl><dt><strong>format_type</strong></dt>
<dd><tt>Returns&nbsp;the&nbsp;MIDI&nbsp;format&nbsp;type&nbsp;as&nbsp;stored&nbsp;in&nbsp;the&nbsp;header&nbsp;of&nbsp;the&nbsp;MIDI&nbsp;file:<br>
0&nbsp;&nbsp;&nbsp;single&nbsp;track&nbsp;MIDI&nbsp;file,&nbsp;should&nbsp;have&nbsp;only&nbsp;one&nbsp;track.<br>
&nbsp;&nbsp;&nbsp;&nbsp;To&nbsp;parse&nbsp;a&nbsp;type&nbsp;0&nbsp;file,&nbsp;use&nbsp;the&nbsp;MIdiFile&nbsp;object&nbsp;as&nbsp;iterator:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;MidiFile("example.mid"):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;process&nbsp;each&nbsp;event<br>
1&nbsp;&nbsp;&nbsp;multitrack&nbsp;MIDI&nbsp;file,&nbsp;can&nbsp;have&nbsp;many&nbsp;tracks.&nbsp;During&nbsp;playback,&nbsp;the&nbsp;tracks<br>
are&nbsp;merged&nbsp;into&nbsp;one&nbsp;ordered&nbsp;sequence&nbsp;of&nbsp;events.<br>
&nbsp;&nbsp;&nbsp;&nbsp;To&nbsp;parse&nbsp;a&nbsp;type&nbsp;1&nbsp;file,&nbsp;proceeed&nbsp;as&nbsp;with&nbsp;a&nbsp;type&nbsp;0&nbsp;file.<br>
2&nbsp;&nbsp;&nbsp;each&nbsp;track&nbsp;behaves&nbsp;like&nbsp;a&nbsp;format&nbsp;0&nbsp;single&nbsp;track&nbsp;MIDI&nbsp;file.&nbsp;Merging<br>
tracks&nbsp;is&nbsp;not&nbsp;allowed.&nbsp;Track&nbsp;number&nbsp;"n"&nbsp;is&nbsp;parsed&nbsp;as&nbsp;follows:<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;MidiFile("format2file.mid").tracks[n]:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;....&nbsp;process&nbsp;event...</tt></dd>
</dl>
<dl><dt><strong>miditicks_per_quarter</strong></dt>
<dd><tt>Return&nbsp;the&nbsp;midi&nbsp;ticks&nbsp;per&nbsp;quarter&nbsp;note&nbsp;(also&nbsp;called&nbsp;pulses&nbsp;per&nbsp;beat)<br>
parameter&nbsp;in&nbsp;the&nbsp;MIDI&nbsp;header&nbsp;of&nbsp;the&nbsp;file.</tt></dd>
</dl>
<dl><dt><strong>reuse_event_object</strong></dt>
<dd><tt>Return&nbsp;the&nbsp;value&nbsp;of&nbsp;reuse_event_object.<br>
True:&nbsp;when&nbsp;iterating&nbsp;through&nbsp;a&nbsp;track&nbsp;or&nbsp;midi&nbsp;file,&nbsp;the&nbsp;same&nbsp;event&nbsp;object<br>
is&nbsp;returned&nbsp;over&nbsp;and&nbsp;over&nbsp;(this&nbsp;is&nbsp;a&nbsp;optimization&nbsp;recommended&nbsp;for&nbsp;Micropython)<br>
&nbsp;<br>
False:&nbsp;when&nbsp;iterating&nbsp;through&nbsp;a&nbsp;track&nbsp;or&nbsp;midi&nbsp;file,&nbsp;a&nbsp;different&nbsp;event<br>
object&nbsp;is&nbsp;returned&nbsp;each&nbsp;time&nbsp;(this&nbsp;is&nbsp;the&nbsp;typical&nbsp;Python&nbsp;behaviour).</tt></dd>
</dl>
<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table> <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="MidiTrack">class <strong>MidiTrack</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt><a href="#MidiTrack">MidiTrack</a>(file,&nbsp;midifile)<br>
&nbsp;<br>
This&nbsp;<a href="builtins.html#object">object</a>&nbsp;contains&nbsp;the&nbsp;track&nbsp;of&nbsp;a&nbsp;midi&nbsp;file.&nbsp;It&nbsp;is<br>
created&nbsp;internally&nbsp;by&nbsp;the&nbsp;<a href="#MidiFile">MidiFile</a>&nbsp;function&nbsp;for&nbsp;each&nbsp;track<br>
chunk&nbsp;found&nbsp;in&nbsp;the&nbsp;midi&nbsp;file.<br>
&nbsp;<br>
<a href="#MidiTrack">MidiTrack</a>&nbsp;objects&nbsp;are&nbsp;accessible&nbsp;via&nbsp;the&nbsp;<a href="#MidiFile">MidiFile</a>.tracks&nbsp;list<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="MidiTrack-__init__"><strong>__init__</strong></a>(self, file, midifile)</dt><dd><tt>The&nbsp;<a href="#MidiTrack">MidiTrack</a>&nbsp;cosntructor&nbsp;is&nbsp;called&nbsp;internally&nbsp;by&nbsp;<a href="#MidiFile">MidiFile</a>,<br>
you&nbsp;don't&nbsp;need&nbsp;to&nbsp;create&nbsp;a&nbsp;<a href="#MidiTrack">MidiTrack</a>.</tt></dd></dl>

<dl><dt><a name="MidiTrack-__iter__"><strong>__iter__</strong></a>(self)</dt><dd><tt>Iterating&nbsp;through&nbsp;a&nbsp;track&nbsp;will&nbsp;yield&nbsp;all&nbsp;events&nbsp;of&nbsp;that&nbsp;track<br>
of&nbsp;MIDI&nbsp;file.&nbsp;For&nbsp;example,&nbsp;to&nbsp;parser&nbsp;the&nbsp;first&nbsp;track&nbsp;in&nbsp;a&nbsp;midi&nbsp;file:<br>
&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;event&nbsp;in&nbsp;<a href="#MidiFile">MidiFile</a>("example.mid").track[0]:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;....&nbsp;process&nbsp;event&nbsp;...<br>
&nbsp;<br>
event.delta_miditicks&nbsp;will&nbsp;have&nbsp;the&nbsp;time&nbsp;difference&nbsp;with&nbsp;the&nbsp;previous<br>
event,&nbsp;in&nbsp;MIDI&nbsp;ticks&nbsp;(pulses).<br>
&nbsp;<br>
event.delta_us&nbsp;is&nbsp;calculated&nbsp;as&nbsp;the&nbsp;time&nbsp;difference&nbsp;with&nbsp;the&nbsp;previous&nbsp;event<br>
in&nbsp;microseconds.&nbsp;For&nbsp;this&nbsp;calculation,&nbsp;the&nbsp;set&nbsp;tempo&nbsp;events&nbsp;and<br>
the&nbsp;MIDI&nbsp;ticks&nbsp;per&nbsp;quarter&nbsp;note&nbsp;(also&nbsp;called&nbsp;"pulses&nbsp;per&nbsp;beat")<br>
of&nbsp;the&nbsp;MIDI&nbsp;file&nbsp;header&nbsp;are&nbsp;taken&nbsp;into&nbsp;consideration.<br>
&nbsp;<br>
This&nbsp;function&nbsp;should&nbsp;only&nbsp;be&nbsp;necessary&nbsp;to&nbsp;play&nbsp;a&nbsp;single<br>
track&nbsp;of&nbsp;a&nbsp;format&nbsp;type&nbsp;2&nbsp;file.&nbsp;Format&nbsp;2&nbsp;type&nbsp;files&nbsp;are<br>
not&nbsp;very&nbsp;common.<br>
&nbsp;<br>
The&nbsp;last&nbsp;event&nbsp;will&nbsp;always&nbsp;be&nbsp;a&nbsp;END_OF_TRACK&nbsp;event,&nbsp;if&nbsp;missing&nbsp;in&nbsp;the&nbsp;file.</tt></dd></dl>

<dl><dt><a name="MidiTrack-__lt__"><strong>__lt__</strong></a>(self, compare_to)</dt><dd><tt>Used&nbsp;internally&nbsp;by&nbsp;the&nbsp;min&nbsp;function&nbsp;to&nbsp;compare&nbsp;the&nbsp;current&nbsp;time&nbsp;in&nbsp;miditicks<br>
of&nbsp;the&nbsp;different&nbsp;tracks,&nbsp;the&nbsp;goal&nbsp;is&nbsp;to&nbsp;find&nbsp;the&nbsp;next&nbsp;midi&nbsp;event<br>
of&nbsp;all&nbsp;tracks&nbsp;(the&nbsp;one&nbsp;with&nbsp;the&nbsp;smallest&nbsp;time&nbsp;since&nbsp;the&nbsp;beginning&nbsp;of&nbsp;the&nbsp;track)</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><strong>const</strong> <em>lambda</em> x</dt><dd><tt>#&nbsp;Ignore&nbsp;const</tt></dd></dl>
 <dl><dt><a name="-micropython"><strong>micropython</strong></a>(function)</dt><dd><tt>#&nbsp;Make&nbsp;the&nbsp;@micropython.native&nbsp;decorator&nbsp;do&nbsp;nothing</tt></dd></dl>
 <dl><dt><strong>os_path_abspath</strong> <em>lambda</em> x</dt></dl>
 <dl><dt><strong>ticks_diff_us</strong> <em>lambda</em> x, y</dt></dl>
 <dl><dt><strong>ticks_now_us</strong> <em>lambda</em> (...)</dt></dl>
 <dl><dt><strong>time_sleep_us</strong> <em>lambda</em> usec</dt><dd><tt>#&nbsp;These&nbsp;functions&nbsp;only&nbsp;are&nbsp;available&nbsp;in&nbsp;Micropython</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>AFTERTOUCH</strong> = 208<br>
<strong>CHANNEL_PREFIX</strong> = 32<br>
<strong>CONTROL_CHANGE</strong> = 176<br>
<strong>COPYRIGHT</strong> = 2<br>
<strong>CUE_MARKER</strong> = 7<br>
<strong>DEVICE_NAME</strong> = 9<br>
<strong>END_OF_TRACK</strong> = 47<br>
<strong>ESCAPE</strong> = 247<br>
<strong>INSTRUMENT_NAME</strong> = 4<br>
<strong>KEY_SIGNATURE</strong> = 89<br>
<strong>LYRICS</strong> = 5<br>
<strong>MARKER</strong> = 6<br>
<strong>MIDI_PORT</strong> = 33<br>
<strong>NOTE_OFF</strong> = 128<br>
<strong>NOTE_ON</strong> = 144<br>
<strong>PITCHWHEEL</strong> = 224<br>
<strong>POLYTOUCH</strong> = 160<br>
<strong>PROGRAM_CHANGE</strong> = 192<br>
<strong>PROGRAM_NAME</strong> = 8<br>
<strong>SEQUENCER_SPECIFIC</strong> = 127<br>
<strong>SEQUENCE_NUMBER</strong> = 0<br>
<strong>SET_TEMPO</strong> = 81<br>
<strong>SMPTE_OFFSET</strong> = 84<br>
<strong>SYSEX</strong> = 240<br>
<strong>TEXT</strong> = 1<br>
<strong>TIME_SIGNATURE</strong> = 88<br>
<strong>TRACK_NAME</strong> = 3<br>
<strong>UPYTHON</strong> = False</td></tr></table>
</body></html>