import websockets
import asyncio

async def time(websocket,path):
	while True:
		await websocket.send(2)
		await asyncio.sleep(1)

start_server = websockets.serve(time, "127.0.0.1", 5678) 

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
