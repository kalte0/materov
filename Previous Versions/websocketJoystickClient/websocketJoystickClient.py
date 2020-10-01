import asyncio 
import websockets
import pygame
import time
import json

pygame.init() #Starts the game, finds the joysticks on the system. Automatically includes pygame.joystick.init()
#print(pygame.joystick.Joystick(0).get_axis(0)) 

if pygame.joystick.get_init():
    print("Joystick object initialized")
#pygame.joystick.Joystick(1).init()


done = False; #for the loop, set to False at the beginning of the 

async def hello():
    uri = "ws://192.168.1.22:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected")
        while True:
            joystick = pygame.joystick.Joystick(0) # We're only connecting one joystick, no need to do the scan 
            joystick.init()
            pygame.event.pump()
            greeting = "test"
            await websocket.send(greeting)
            hello = await websocket.recv()
            #print(hello) 
            #numAxes = joystick.get_numaxes()
            for event in pygame.event.get(): 
                if event.type == pygame.JOYAXISMOTION:
                    dict = {}
                    dict['test'] = 1
                    dict['axis0'] = int(1000*joystick.get_axis(0)) #For just the number I want to send, testing out rounding 2 decimal places here. Add *1000 here later?
                    print(int(1000*joystick.get_axis(0)))
                    #dict['axis1'] = joystick.get_axis(1)
                    #dict['axis2'] = joystick.get_axis(2)
                    #dict['axis3'] = joystick.get_axis(3)
            json_string = json.dumps(dict)
            await websocket.send(json_string)
            greeting = await websocket.recv()
            print(f"< {greeting}")   
            
            time.sleep(0.5)
                    

asyncio.run(hello())
asyncio.get_event_loop().run_forever()

#pygame.quit() #the loop above will keep looping until you exit out of it. Notice while loop inside def numbers will keep sending data until uesr clicks close, then "numbers" will be considered complete and run this.  
