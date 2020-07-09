
# usr/Documents/Github/materov/websocketServerv2.py 
import asyncio
import websockets
import json
import serial

ser = serial.Serial('/dev/tty.usbmodem142301', 9600)

connected = set() # Used in line of main(): connected.add(websocket).

async def main(websocket, path):
	connected.add(websocket) # This line allows for more clients to join the same server.
	print("Connected");
	while True:
			info = await websocket.recv() #store the information recieved from the client in a variable called "info"
			try:
				print(json.loads(info)) #attempt to unpack the json info, and print the dict
			except json.decoder.JSONDecodeError as e:
				print (e) # if that doesn't work, print the error
				pass
			if ser.isOpen():
				print("Serial is open") 
				ser.write(b'2') # send message through serial. b'' converts to bytes. Allows passage of unicode strings. 
				ser.flush() # Wait until info is sent before moving on.
				if (ser.in_waiting > 0): # ser.in_waiting is the number of bytes "arrived and stored in the serial receive buffer"
					incoming = ser.readline().decode("utf-8") #Print whatever message recieved through Serial. Note: will stall the code if nothing is being sent through Serial. 
					print(incoming) 
			await asyncio.sleep(0.5) 
 
server = websockets.serve(main, "localhost", 8765, ping_interval=None) # This is what starts up the actual websocket code. ping_inteval is intended to make not time out-- not working correctly, though.  
# If you recieve a 1006 timeout error, that's a general, nondescriptive error message, like "could not open file". Probably an issue with the timeout. 
loop = asyncio.get_event_loop() #when referring to the event loop, just call it loop to be quicker. 
loop.run_until_complete(server) #run the above command, which starts up the websocket code. 
