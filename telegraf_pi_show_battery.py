#!/usr/bin/env python
# X750 Battery voltage & precentage reading for Telegraf
# Add telegrafuser to i2c group in /etc/group

import struct
import smbus
import json

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

battery_dict = {
    'Battery Voltage' : round(float(readVoltage(bus)),2),
    'Battery Charge'  : int(readCapacity(bus))
}
print(json.dumps(battery_dict))
