# TCP Chat Server

A simple multi-client chat server built with Python sockets.  
The server accepts multiple clients simultaneously and allows users to communicate in a shared chat room.

## Features

- Multi-client support using **Python threads**
- **Broadcast messages** to all connected clients
- **Custom usernames**: clients can set their nickname using `/nick YourName`
- Server logs all messages, connections, disconnections, and username changes

## How it works

1. The server listens on a specified IP and port.
2. Clients can connect using a TCP socket.
3. Messages from one client are sent to all other connected clients.
4. Users can change their username anytime with the `/nick` command.
5. Informational messages notify clients when someone joins, leaves, or changes their username.

This project demonstrates core networking concepts such as TCP connections, client-server communication, threading, and managing multiple client connections.