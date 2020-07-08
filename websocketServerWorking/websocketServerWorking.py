# usr/Documents/Github/materov/websocketServerv2.py 
import asyncio
import websockets
import json
import serial

ser = serial.Serial('/dev/tty.usbmodem142301', 9600)

connected = set() # Used in line of main(): connected.add(websocket).

async def joy(websocket, path):
	connected.add(websocket) # This line allows for more clients to join the same server.
	print("Connected");
	async for message in websocket: # When recieve an information through websockets.
		info = await websocket.recv() #store the information recieved from the client in a variable called "info"
		print("Loud and Clear")
		await asyncio.sleep(0.5) 

async def websocket(): # This command is necessary to get the ACTUAL websocket code to run. 
	server = await websockets.serve(joy, "localhost", 8765, ping_interval=None)
	await server.wait_closed() 

async def ser():
	while True:
		print("ser activated!!")
		await asyncio.sleep(1)
	#if ser.isOpen():
		#print("Serial is open") #Test, may remove later if falls completely out of use 
	#	ser.write(b'2') # send message through serial. b'' converts to bytes. Allows passage of unicode strings. 
	#	ser.flush() # Wait until info is sent before moving on.
	#	if (ser.in_waiting > 0): # ser.in_waiting is the number of bytes "arrived and stored in the serial receive buffer"
	#		incoming = ser.readline().decode("utf-8") #Print whatever message recieved through Serial. Note: will stall the code if nothing is being sent through Serial. 
	#		print(incoming) 
	 
server = websockets.serve(joy, "localhost", 8765, ping_interval=None) # This is what starts up the actual websocket code. ping_inteval is intended to make not time out-- not working correctly, though.  
# If you recieve a 1006 timeout error, that's a general, nondescriptive error message, like "could not open file". Probably an issue with the timeout. 
loop = asyncio.get_event_loop() #when referring to the event loop, just call it loop to be quicker. 
loop.run_until_complete(server) #run the above command, which starts up the websocket code. 
get = loop.create_task(websocket()) # create a task called get. Automatically schedules to run soon. Joystick + websocket.
send = loop.create_task(ser())
loop.run_forever() #after that, just keep running things. 
