import websockets
import asyncio
import json

connected = set()
dict= {"test":1}
async def time(websocket,path): 
	connected.add(websocket) 
	print(connected)
	while True:
		try:
			msg = json.dumps(dict)
			print(json.dumps(dict)) 
			await asyncio.wait([user.send(msg) for user in connected]) # Ech  back msg. 
		except:
			connected.remove(websocket)
		await asyncio.sleep(1)
start_server = websockets.serve(time, "127.0.0.1", 5678) 

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
