import socket

# Method for receiving messages from the client
def receive_message(client_socket):
    try:
        message = client_socket.recv(1024).decode()
        return message
    except socket.error as e:
        print(f"Error receiving message: {e}")
        return None

# Method for sending messages to the client
def send_message(client_socket, message):
    try:
        client_socket.send(message.encode())
    except socket.error as e:
        print(f"Error sending message: {e}")

# Method for the server
def server():
    
    # Get the IP address and port number from the user
    host_input = input("Enter IP address (press enter for localhost): ").strip()
    if host_input == '':
        host = '127.0.0.1'
    else:
        host = host_input

    port_input = input("Enter port number (press enter for default port): ").strip()
    if port_input == '':
        port = 12345
    else:
        port = port_input

    try:
        port = int(port)  # Convert port to integer

        # Validate port number
        if not (0 < port < 65536):
            print("Port number must be between 1 and 65535.")
            return

        # Validate IP address if it's not the default
        if host != '127.0.0.1':
            try:
                socket.inet_aton(host)
            except socket.error:
                print("Invalid IP address")
                return

        # Get the username from the user
        username = input("Enter your username: ")

        # Connect to the client
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Server is waiting for connection and a message from the client...")

        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}. Type in 'end' to exit. When your entered username comes up with a ':' you have been prompted to enter your message to send back to the client.")

        # Send and receive messages
        while True:
            message = receive_message(client_socket)
            if message.endswith('end'):
                print("Client has ended the connection.")
                break
            else:
                print(message)
                if message.lower() == 'end':
                    send_message(client_socket, 'end')
                    break
                reply = input(f"{username}: ")
                send_message(client_socket, (f"{username}: {reply}"))
                if reply.lower() == 'end':
                    break

    # Handle exceptions
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except KeyboardInterrupt:
        print("\nServer interrupted.")
    except ValueError:
        print("Invalid port number")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()


if __name__ == "__main__":
    server()
