from socket import socket, AF_INET, SOCK_STREAM
import threading

buffer_size = 1024  # 1MB
host = "127.0.0.1"
port = 12345
exit_code = "exit!"

# Event to signal shutdown both threads when exit_code is enter
shutdown_event = threading.Event()


def receive_msg(sock: socket):
    while not shutdown_event.is_set():
        try:
            data = sock.recv(buffer_size).decode()
            if data:
                print(f'[FROM CLIENT]: {data}')
                if data.lower() == exit_code:
                    print('Exit code received. Shutting down server...')
                    shutdown_event.set()
                    break
            else:
                break
        except Exception as e:
            print(f'Error receiving data: {e}')
            shutdown_event.set()
            break


def send_msg(sock: socket):
    while not shutdown_event.is_set():
        msg = input()
        if msg.lower() == exit_code:
            print("Exit code sent. Shutting down server...")
            sock.sendall(msg.encode())
            shutdown_event.set()
            break
        sock.sendall(msg.encode())


def start_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))

    client_sock = None

    try:
        # only allow 1 conn
        server_socket.listen(1)
        print(f'Server listening on {host}:{port}')

        client_sock, client_addr = server_socket.accept()
        print(f'Client {client_addr[0]}:{client_addr[1]} connected')

        # threads for non-blocking appraoch
        receive_thread = threading.Thread(target=receive_msg, args=(client_sock,))
        send_thread = threading.Thread(target=send_msg, args=(client_sock,))

        # once a client connects: main thread [server] starts two threads
        # one that listen for incoming events
        # one for sending messages back
        receive_thread.start()
        send_thread.start()

        # main thread [server] waits for the thread to finish
        # allowing both threads to run concurrently without shutting down
        receive_thread.join()
        send_thread.join()

    except KeyboardInterrupt:
        print('\nKeyboard interrupt received. Shutting down server...')
        shutdown_event.set()

    finally:
        if client_sock:
            client_sock.close()
        server_socket.close()
        print('Server shut down')


if __name__ == "__main__":
    start_server()