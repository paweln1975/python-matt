import asyncio
import websockets
import serial
import json
import signal
import sys

# Serial port configuration
SERIAL_PORT = 'COM3'  # Change to your scanner's port
BAUD_RATE = 9600  # Change to your scanner's baud rate

# WebSocket server configuration
WS_HOST = 'localhost'
WS_PORT = 8765

# Global variables
connected_clients = set()
serial_port = None
running = True


async def handle_serial():
    """Read data from serial port and broadcast to all WebSocket clients"""
    global serial_port

    try:
        serial_port = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to serial port {SERIAL_PORT}")

        while running:
            if serial_port.in_waiting > 0:
                try:
                    # Read data from the scanner
                    data = serial_port.readline().decode('utf-8').strip()
                    print(f"Received from scanner: {data}")

                    # Create a message to send to clients
                    message = json.dumps({
                        "type": "scan_data",
                        "data": data,
                        "timestamp": asyncio.get_event_loop().time()
                    })

                    # Broadcast to all connected clients
                    if connected_clients:
                        await asyncio.gather(
                            *[client.send(message) for client in connected_clients]
                        )
                except Exception as e:
                    print(f"Error reading from serial: {e}")

            # Small delay to prevent CPU overuse
            await asyncio.sleep(0.01)

    except Exception as e:
        print(f"Serial port error: {e}")
    finally:
        if serial_port and serial_port.is_open:
            serial_port.close()
            print("Serial port closed")


async def handle_websocket(websocket):
    """Handle WebSocket connections from browsers"""
    global connected_clients

    try:
        # Register new client
        connected_clients.add(websocket)
        print(f"New client connected. Total clients: {len(connected_clients)}")

        # Send initial connection confirmation
        await websocket.send(json.dumps({
            "type": "connection_status",
            "status": "connected",
            "message": "Connected to scanner bridge"
        }))

        # Keep connection alive and handle client messages
        async for message in websocket:
            try:
                data = json.loads(message)

                # Handle commands from the browser
                if data.get('command') == 'get_status':
                    await websocket.send(json.dumps({
                        "type": "status",
                        "connected": serial_port is not None and serial_port.is_open,
                        "port": SERIAL_PORT
                    }))

                # Add more command handlers as needed

            except json.JSONDecodeError:
                print(f"Received invalid JSON: {message}")

    except websockets.exceptions.ConnectionClosed:
        print("Client connection closed")
    finally:
        # Unregister client on disconnect
        connected_clients.remove(websocket)
        print(f"Client disconnected. Remaining clients: {len(connected_clients)}")


async def main():
    """Main application entry point"""
    # Start the serial handling task
    serial_task = asyncio.create_task(handle_serial())

    # Start the WebSocket server
    async with websockets.serve(handle_websocket, WS_HOST, WS_PORT):
        print(f"WebSocket server started at ws://{WS_HOST}:{WS_PORT}")

        # Keep the server running until interrupted
        await asyncio.Future()


def handle_shutdown(signal, frame):
    """Handle graceful shutdown"""
    global running
    print("\nShutting down...")
    running = False

    # Close serial port
    if serial_port and serial_port.is_open:
        serial_port.close()

    sys.exit(0)


if __name__ == "__main__":
    # Register shutdown handlers
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    # Install required packages if not already installed
    print("Starting Scanner Bridge Server...")
    print(f"Serial Port: {SERIAL_PORT}, Baud Rate: {BAUD_RATE}")
    print(f"WebSocket: ws://{WS_HOST}:{WS_PORT}")

    # Run the async application
    asyncio.run(main())