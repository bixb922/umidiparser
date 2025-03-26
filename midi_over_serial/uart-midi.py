from machine import UART, Pin
import time
import sys


tx_number = 10
rx_number = 9
baudrate = 31250
drive = 2

print(f"Tx pin {tx_number=} mode=Pin.OUT {drive=}")
txpin = Pin(tx_number, mode=Pin.OUT, drive=drive)
rxpin = Pin(rx_number, mode=Pin.IN)

def test_voltage_levels():
    print("Testing voltage levels")
    # Alternate between logical 0 and 1 every 5 seconds.
    while True:
        print("111111111111111")
        txpin.value(1)
        time.sleep(5)
        print("0")
        txpin.value(0)
        time.sleep(5)

# Uncomment this line if you want to do level tests.
# Comment this line if you want to play a MIDI file.     
#test_voltage_levels()

# To invert the signal add: invert=UART.INV_TX
uart = UART( 1, baudrate=baudrate, tx=txpin, rx=rxpin)
print(uart)

def test_midi_file():
    print("Testing a MIDI file")
    from umidiparser import MidiFile

    # Control change: all notes off 
    uart.write(bytes([0xB0, 123, 0x00]))
    time.sleep_ms(100)
    # Control change: reset all controllers.
    uart.write(bytes([0xB0, 129, 0x00]))
    time.sleep_ms(100)
            
    for ev in MidiFile("washington.mid").play():
        if ev.is_channel():
            print(".", end="")
            uart.write( ev.to_midi() )
        # else:
        #    print("discarded event:", ev)
            
test_midi_file()
