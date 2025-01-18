import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from serial_reader import run_serial_reader
from websocket_handler import websocket_endpoint, broadcast_websocket_data
from api import router as api_router
from database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


# Initialize FastAPI app
app = FastAPI(lifespan=lifespan)


    
# Include API routes
app.include_router(api_router, prefix="/api")

# Define WebSocket route
app.add_api_websocket_route("/ws/sensor-data", websocket_endpoint)

# Start Serial Reader
run_serial_reader(broadcast_websocket_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
