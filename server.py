"""
Socket is used as a low-level networking interface
"""
import socket

DEFAULT_IP = "127.0.0.1"
DEFAULT_PORT = 12345


def receive_message(client_socket):
    """
    Method for receiving messages from the client
    """
    try:
        message = client_socket.recv(1024).decode()
        return message
    except socket.error as e:
        print(f"Error receiving message: {e}")
        return None


def send_message(client_socket, message):
    """
    Method for sending messages to the client
    """
    try:
        client_socket.send(message.encode())
    except socket.error as e:
        print(f"Error sending message: {e}")


def get_host_ip():
    """
    Gets the host's IP address.
    If none is provided, defaults to 127.0.0.1 (localhost).
    """

    ip = input("Enter server IP address (press enter for default host): ")
    ip = ip.strip() or DEFAULT_IP  # Defaults to 127.0.0.1 if input is blank

    return ip


def get_port() -> int:
    """
    Get's the port to use.
    If none is provided, defaults to 12345.
    """

    while True:  # Should keep asking until valid input
        port_input = input(
            "Enter port number (press enter for default port): ").strip()

        if not port_input:
            return DEFAULT_PORT  # Defaults to 12345 if input is blank

        # Validate inputted port number
        try:
            port: int = int(port_input)
            if port not in range(1, 65536):
                print("Port number must be between 1 and 65535.")
                continue  # Asks again
            else:
                return port
        except ValueError:
            print("You must enter a valid integer.")


def server():
    """
    Method for the server
    """

    host = get_host_ip()

    port = get_port()

    try:
        # Get the username from the user
        username = input("Enter your username: ")

        # Connect to the client
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Server is waiting for connection and a message "
              "from the client...")

        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}. Type in 'end' to exit."
              "When your entered username comes up with a ':' you have "
              "been prompted to enter your message to send back to the "
              "client.")

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

    # Exception handling
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except KeyboardInterrupt:
        print("\nServer interrupted.")
    except ValueError:
        print("Invalid port number")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()


if __name__ == "__main__":
    server()
