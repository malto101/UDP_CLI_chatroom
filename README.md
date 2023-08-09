# UDP Chat Application

This repository contains Python scripts for a basic UDP chat application consisting of a client (`client.py`) and a server (`server.py`), enabling communication over the User Datagram Protocol (UDP).

## Client Script (`client.py`)

The `client.py` script functions as a UDP client for the chat application.

### Usage

1. Run the script: `python client.py`
2. Enter your desired nickname.
3. Messages you send will be displayed in the chat.
4. To exit the chat, type `!q`.

## Server Script (`server.py`)

The `server.py` script functions as a UDP server for the chat application.

### Usage

1. Run the script: `python server.py`
2. The server will listen for incoming messages from clients and broadcast them to all connected clients.

## How It Works

- The client script binds to a random port on the localhost and sends a signup message with the chosen nickname to the server.
- The server script binds to a specific port and listens for incoming messages.
- When a message is received, the server processes it and broadcasts it to all clients.
- Clients receive messages and display them in the console.

## Important Notes

- This UDP chat application provides a basic demonstration of communication between clients and a server using UDP.
- The application lacks advanced features and security mechanisms.
- It's recommended for educational purposes and local usage only.
