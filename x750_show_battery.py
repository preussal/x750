#!/usr/bin/env python
# X750 Battery voltage & precentage reading

import struct
import smbus
import sys
import time


def readVoltage(bus):

     address = 0x36
     read = bus.read_word_data(address, 2)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     voltage = swapped * 1.25 /1000/16
     return voltage


def readCapacity(bus):

     address = 0x36
     read = bus.read_word_data(address, 4)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     capacity = swapped/256
     return capacity

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

while True:
     voltage = float(readVoltage(bus))
     battery = int(readCapacity(bus))

     print ("******************")
     print ("Voltage: "+str(round(voltage,2))+"V")
     print ("Battery: "+str(battery)+"%")

     if battery == 100:
          print ("Battery: FULL")
     if battery >= 90:
          print ("Battery: > 90% FULL")
     if battery < 20:
          print ("Battery: LOW")
     print ("******************")
     time.sleep(5)
