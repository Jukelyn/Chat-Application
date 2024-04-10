import socket

# Method for receiving messages from the server
def receive_message(server_socket):
    try:
        message = server_socket.recv(1024).decode()
        return message
    except socket.error as e:
        print(f"Error receiving message: {e}")
        return None

# Method for sending messages to the server
def send_message(server_socket, message):
    try:
        server_socket.send(message.encode())
    except socket.error as e:
        print(f"Error sending message: {e}")

# Method for the client
def client():

    # Get the IP address and port number from the user
    host_input = input("Enter server IP address (press enter for default host): ").strip()
    if host_input == '':
        host = '127.0.0.1'
    else:
        host = host_input

    # Get the port number from the user
    port_input = input("Enter port number (press enter for default port): ").strip()
    if port_input == '':
        port = 12345
    else:
        port = port_input
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

    try:
        # Connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, int(port)))
        print("Connected to the server. Type in 'end' to exit. When your entered username comes up with a ':' you have been prompted to enter your message to send back to the server.")

        # Send and receive messages
        while True:
            message = input(f"{username}:  ")
            send_message(client_socket, (f"{username}: {message}"))
            if message.lower() == 'end':
                break

            reply = receive_message(client_socket)
            if reply.endswith('end'):
                print("Server has ended the connection.")
                break
            else:
                print(reply)

    # Handle exceptions
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except KeyboardInterrupt:
        print("\nClient interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()

if __name__ == "__main__":
    client()
