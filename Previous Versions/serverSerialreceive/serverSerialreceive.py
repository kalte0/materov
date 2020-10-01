import asyncio
import serial

ser = serial.Serial('/dev/tty.usbmodem142101', 9600)

async def receiveSerial():
	while True:
		if ser.isOpen():
			print("Serial open")
			if (ser.in_waiting > 0): # prevents stall on readline. 
				incoming = ser.readline().decode("utf-8")
				print("The oracle has spoken:...")
				print("< {}".format(incoming))
			await asyncio.sleep(0.5)

loop = asyncio.get_event_loop()
asyncio.ensure_future(receiveSerial())
loop.run_forever()
