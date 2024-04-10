import socket

def receive_message(server_socket):
    try:
        message = server_socket.recv(1024).decode()
        return message
    except socket.error as e:
        print(f"Error receiving message: {e}")
        return None

def send_message(server_socket, message):
    try:
        server_socket.send(message.encode())
    except socket.error as e:
        print(f"Error sending message: {e}")

def client():
    host_input = input("Enter server IP address: ").strip()
    if host_input == '':
        host = '127.0.0.1'
    else:
        host = host_input


    port_input = input("Enter port number (press enter for default port): ").strip()
    if port_input == '':
        port = 12345
    else:
        port = port_input

    username = input("Enter your username: ")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, int(port)))
        print("Connected to the server. Type in 'end' to exit. When your entered username comes up with a ':' you have been prompted to enter your message to send back to the server.")

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
