import asyncio
import json
import serial
import websockets

ser = serial.Serial('/dev/tty.usbmodem141101', 9600)

connected = set() # Used in line of main(): connected.add(websocket).

dummy = {"test": 1} # basic info to be sent. (Super basic test)
# Idea of structure below: one function acts as a "bucket", a websocket taking info from joystick + sending it down. Another entirely to read serial information coming up. 

async def bucket(websocket, path):
	sent = 0
	connected.add(websocket)
	print("bucket() works")
	async for message in websocket: # if there's a message from the client. Message actually contians the information.
		sent = sent + 1
		print(sent)
		#info = await websocket.recv() # store in "info"
		info = message
		print(json.loads(message))
		#print(json.loads(info)) # print out the python dictionary
		ser.write(info.encode('ascii')) # write "info" down to arduino.
		ser.flush() # Wait for everything to be sent before continuing -- will stall if nothing sent. 
		#await asyncio.sleep(0.5) # REMOVE if message is all worky? (Ask Christy). 

async def readSerial():
	print("readSerial() works")
	while True:
		if ser.isOpen() & (ser.in_waiting > 0): # CHRISTY is there something here basically equivalent to for message in websocket? Huge delay in reading values. 
			#print("ser.isOpen + ser.in_waiting>0") 
			incoming = ser.readline().decode("utf-8") # Arduino: Println or py code blocked.  
			print("< {}".format(incoming))
			
		await asyncio.sleep(0.1) 


asyncio.ensure_future(readSerial())
loop = asyncio.get_event_loop()
server = websockets.serve(bucket, "localhost", 8765, ping_interval= None)
loop.run_until_complete(server)
loop.run_forever()
