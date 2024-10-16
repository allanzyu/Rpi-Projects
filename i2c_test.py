#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus
import time

addr = 0x08 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

numb = 1
def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

print ("Enter 1 for ON or 0 for OFF")
while numb == 1:

	command = input(">>>>   ")

	if command == "1":
		bus.write_byte(addr, 0x1) # switch it on
	elif command == "0":
		bus.write_byte(addr, 0x0) # switch it off
	elif command =="2":
		test = StringToBytes("test")
		bus.write_i2c_block_data(addr,0x01,test)
		##print ("Arduino sends: " + str(pin))
	elif command =="3":
		data = bytes(bus.read_i2c_block_data(addr,0x00, 4))
#		text = data.decode()
#		print(text)
	else:
		numb = 0

