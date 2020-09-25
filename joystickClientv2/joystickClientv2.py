# usr/Documents/Github/materov/joystickClientv2.py

import asyncio
import websockets
import json
import pygame
import time


pygame.init() # Finds joystick, includes pygame.joystick.init()

joystick = pygame.joystick.Joystick(0) # shortcut, to write less later. 
joystick.init() # Initializes this specific Joystick (I checked, it's necessary)
#print (joystick.get_axis(0)) # Cute test, might delete later.

dict = {} # This is the dictionary the joystick information will be put into, then dumpsed into JSON. 


async def main(): # The main loop for this function. 
	timeLast = round(time.monotonic(), 4) # establish the start time with global system time
	sent = 0
	uri = "ws://localhost:8765"
	async with websockets.connect(uri, ping_interval=None) as websocket:
		print("Connected")
		while True:
			currentTime = round(time.monotonic(), 4)
			#print(timeLast)
			#print("{} seconds".format(currentTime)) 
			for event in pygame.event.get(): # Maybe later add a small small delay to not overwhelm system w/ unnecessary information
				if event.type == pygame.JOYAXISMOTION:
					lst = []
					for x in range(4):
						readval = int(1000*joystick.get_axis(x)) #Turn the axis pos into #
						#print(readval)
						lst.append(readval)
					dict["axis"] = lst
					dict["test"] = 2 # add a test value to the dict
				if (currentTime - timeLast > 0.05): #	
					joy_info = json.dumps(dict) # make json string "joy_info" with dict
					await websocket.send(joy_info) #send info + wait until done	
					sent = sent + 1
					print(sent)
					timeLast = currentTime # Reset time for our Millis alike 
					print(dict) 
				pygame.event.pump() # Necessary to clear past events and make pygame run
			
asyncio.run(main())
asyncio.get_event_loop().run_forever()
           
