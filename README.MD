# Project Title: Chat Application

## Project Description
This project consists of a simple chat application where a server and client can communicate with each other. The server script allows the user to start a server, and lets that user specify their desired IP address, port number, and username where a client can connect to.
Then the client script will allow the user to connect to the server by using an IP address and port number that is provided by the user. The user also has to put in their username and then the client first sends a message to the server (upon a successful connection) and then the server and the client can chat between each other back and forth until either the client or server types and enters the "end" keyword. If this occurs then the client and server will disconnect.

### Prerequisites
- Python installed on your machine 

## Usage Instructions:
1. Run `server.py`. Enter the IP address (press Enter for localhost), port number (press Enter for default port), and your username within the terminal.
2. Run `client.py`. Enter the IP address (again just press Enter for localhost), port number (press enter for default port), and your username to establish a connection with the server.
3. Once connected, you can start exchanging messages between client and server. To disconnect, type "end" and press Enter on either the server or client side.
