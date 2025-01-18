from fastapi import WebSocket
import asyncio
import json

# WebSocket clients list
connected_clients = []

async def broadcast_websocket_data(sensor_data):
    """ Sends selected data via WebSocket """
    data_to_send = {
        "temperature": sensor_data["temperature"],
        "humidity": sensor_data["humidity"],
        "windSpeed": sensor_data["windSpeed"],
        "dustParticles": sensor_data["dustParticles"],
    }
    if connected_clients:
        await asyncio.gather(*[ws.send_json(data_to_send) for ws in connected_clients])

async def websocket_endpoint(websocket: WebSocket):
    """ WebSocket endpoint """
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            await asyncio.sleep(1)  # Keep connection alive
    except:
        connected_clients.remove(websocket)