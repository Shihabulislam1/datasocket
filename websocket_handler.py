from fastapi import WebSocket, WebSocketDisconnect
import asyncio
import json
from database import store_data

connected_clients = set()

async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint to handle connections"""
    await websocket.accept()
    connected_clients.add(websocket)
    print(f"New WebSocket connection: {websocket.client}")

    try:
        while True:
            # Receive data from client
            data = await websocket.receive_text()
            print(f"Received data: {data}")
            
            # Parse the data and store it in the database
            try:
                parsed_data = json.loads(data)
                store_data(parsed_data)
            except json.JSONDecodeError:
                print(f"Invalid JSON data received: {data}")
            
            await asyncio.sleep(1)  # Keep connection alive

    except WebSocketDisconnect:
        print(f"WebSocket client {websocket.client} disconnected")
    finally:
        connected_clients.remove(websocket)

async def broadcast_websocket_data(sensor_data):
    """Sends selected sensor data to all connected WebSocket clients"""
    data_to_send = {
        "temperature": sensor_data.get("temperature"),
        "humidity": sensor_data.get("humidity"),
        "windSpeed": sensor_data.get("windSpeed"),
        "dustParticles": sensor_data.get("dustParticles"),
    }
    if connected_clients:
        for client in list(connected_clients):  # Create a copy to avoid modification during iteration
            try:
                message = json.dumps(data_to_send)
                await client.send_text(message)
            except WebSocketDisconnect:
                print(f"WebSocket client {client.client} disconnected")
                connected_clients.remove(client)  # Remove client from the set on disconnect



# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# import asyncio
# import json

# app = FastAPI()

# # WebSocket clients list
# connected_clients = set()

# async def broadcast_websocket_data(sensor_data):
#     """Sends selected sensor data to all connected WebSocket clients"""
#     data_to_send = {
#         "temperature": sensor_data.get("temperature"),
#         "humidity": sensor_data.get("humidity"),
#         "windSpeed": sensor_data.get("windSpeed"),
#         "dustParticles": sensor_data.get("dustParticles"),
#     }
#     # Make sure to send data only to connected clients
#     if connected_clients:
#         for client in list(connected_clients):  # Create a copy to avoid modification during iteration
#             try:
#                 message = json.dumps(data_to_send)
#                 await client.send_text(message)
#             except WebSocketDisconnect:
#                 print(f"WebSocket client {client.client} disconnected")
#                 connected_clients.remove(client)  # Remove client from the set on disconnect

# @app.websocket("/ws/sensor-data")
# async def websocket_endpoint(websocket: WebSocket):
#     """WebSocket endpoint to handle connections"""
#     await websocket.accept()
#     connected_clients.add(websocket)
#     print(f"New WebSocket connection: {websocket.client}")

#     try:
#         while True:
#             await asyncio.sleep(1)  # Keep connection alive
#     except WebSocketDisconnect:
#         print(f"WebSocket client {websocket.client} disconnected")
#     finally:
#         connected_clients.remove(websocket)
