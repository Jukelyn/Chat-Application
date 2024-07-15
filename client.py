"""
Socket is used as a low-level networking interface
"""
import socket

DEFAULT_IP = "127.0.0.1"
DEFAULT_PORT = 12345


def receive_message(server_socket):
    """
    Method for receiving messages from the server
    """

    try:
        message = server_socket.recv(1024).decode()
        return message
    except socket.error as e:
        print(f"Error receiving message: {e}")
        return None


def send_message(server_socket, message):
    """
    Method for sending messages to the server
    """

    try:
        server_socket.send(message.encode())
    except socket.error as e:
        print(f"Error sending message: {e}")


def get_host_ip():
    """
    Gets the host's IP address.
    If none is provided, defaults to 127.0.0.1 (localhost).
    """

    ip = input("Enter server IP address (press enter for default host): ")
    ip = ip.strip() or DEFAULT_IP  # Defaults to 127.0.0.1 if input is blank

    # Validate IP address if it's not the default
    if ip != '127.0.0.1':
        try:
            socket.inet_aton(ip)
        except socket.error:
            print("Invalid IP address")
            return None

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
            port = int(port_input)
            if port not in range(1, 65536):
                print("Port number must be between 1 and 65535.")
                continue  # Asks again
            else:
                return port
        except ValueError:
            print("You must enter a valid integer.")


def client():
    """
    Method for the client
    """

    host = get_host_ip()

    port = get_port()

    # Get the username from the user
    username = input("Enter your username: ")

    try:
        # Connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, int(port)))
        print(("\nConnected to the server. Type in 'end' to exit. "
               "When your entered username comes up with a ':' you "
               "have been prompted to enter your message to send back "
               "to the server."))

        # Send and receive messages
        while True:
            message = input(f"{username}: ")
            send_message(client_socket, (f"{username}: {message}"))
            if message.lower() == 'end':
                break

            reply = receive_message(client_socket)
            if reply.endswith('end'):
                print("Server has ended the connection.")
                break
            else:
                print(reply)

    # Exception handling
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except KeyboardInterrupt:
        print("\nClient interrupted.")
    except ValueError:
        print("Invalid port number")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An error occurred: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()


if __name__ == "__main__":
    client()
