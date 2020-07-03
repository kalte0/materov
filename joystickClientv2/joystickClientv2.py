# usr/Documents/Github/materov/joystickClientv2.py

import asyncio
import websockets
import json
import pygame

pygame.init() # Finds joystick, includes pygame.joystick.init()

joystick = pygame.joystick.Joystick(0) # shortcut, to write less later. 
joystick.init() # Initializes this specific Joystick (I checked, it's necessary)
#print (joystick.get_axis(0)) # Cute test, might delete later.

dict = {} # This is the dictionary the joystick information will be put into, then dumpsed into JSON. 

async def main(): # The main loop for this function. 
	uri = "ws://localhost:8765"
	async with websockets.connect(uri) as websocket:
		print("Connected")
		while True: 
			pygame.event.pump() # Necessary to clear past events and make pygame run
			dict['test'] = 1 # add a test value to the dict
			joy_info = json.dumps(dict) # make json string "joy_info" with dict
			await websocket.send(joy_info) #send info + wait until done
			
			await asyncio.sleep(0.5) # Maybe make delay a variable that can be more easily changed @ top of code at a later point?
			
asyncio.run(main())
asyncio.get_event_loop().run_forever()
           
