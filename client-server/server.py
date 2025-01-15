from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import threading

buffer_size = 1024  # 1MB
host = "127.0.0.1"
port = 12345
exit_code = "exit!"

shutdown_event = threading.Event()
clients = {}  # Dictionary to store clients {name: socket}
lock = threading.Lock()  # Lock to synchronize access to the clients dictionary

connected_msg = "CONNECT"
disconnected_msg = "DISCONNECT"


def broadcast_message(sender_name, message):
    """Broadcast a message to all connected clients except the sender."""
    with lock:
        for name, client in clients.items():
            if name != sender_name:  # Don't send the message back to the sender
                try:
                    if message == connected_msg:
                        client.sendall(f'[{sender_name}] is connected ~'.encode())
                    elif message == disconnected_msg:
                        client.sendall(f'[{sender_name}] is disconnected ~'.encode())
                    else:
                        client.sendall(f'<{sender_name}>: {message}'.encode())
                except Exception as e:
                    print(f"Error broadcasting message to {name}: {e}")
                    del clients[name]


def handle_client(sock, addr):
    """Handle communication with a single client."""
    try:
        # First message from the client is their name
        name = sock.recv(buffer_size).decode().strip()
        with lock:
            clients[name] = sock
        print(f'Client "{name}" connected from {addr[0]}:{addr[1]}')
        broadcast_message(name, connected_msg)

        while not shutdown_event.is_set():
            data = sock.recv(buffer_size).decode()
            if data:
                print(f'[{name}]: {data}')
                if data.lower() == exit_code:
                    print(f'Exit code received from "{name}". Disconnecting...')
                    broadcast_message(name, disconnected_msg)
                    break
                broadcast_message(name, data)
            else:
                break
    except Exception as e:
        print(f"Error handling client {addr[0]}:{addr[1]}: {e}")
    finally:
        with lock:
            if name in clients:
                del clients[name]
        sock.close()
        print(f'"{name}" disconnected')


def start_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    # Allow reuse of the address and port
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((host, port))

    try:
        server_socket.listen(5)
        print(f'Server listening on {host}:{port}')

        while not shutdown_event.is_set():
            client_sock, client_addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
            client_thread.start()

    except KeyboardInterrupt:
        print('\nKeyboard interrupt received. Shutting down server...')
        shutdown_event.set()

    finally:
        server_socket.close()
        print('Server shut down')


if __name__ == "__main__":
    start_server()
