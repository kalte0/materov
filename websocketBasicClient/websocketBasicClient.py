import websockets
import asyncio

async def connect():
	uri = "ws://localhost:5678"
	async with websockets.connect(uri) as websocket:
		while True:		
			async for message in websocket:
				print(message)
				await websocket.send('2')
		
asyncio.run(connect())
asyncio.get_event_loop().run_forever()
