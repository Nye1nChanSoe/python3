from socket import socket, AF_INET, SOCK_STREAM
import threading

buffer_size = 1024  # 1MB
host = "127.0.0.1"
port = 12345
exit_code = "exit!"

shutdown_event = threading.Event()


def receive_msg(sock: socket):
    while not shutdown_event.is_set():
        try:
            data = sock.recv(buffer_size).decode()
            if data:
                print(f'{data}')
            else:
                break
        except Exception as e:
            print(f'Error receiving data: {e}')
            shutdown_event.set()
            break


def send_msg(sock: socket):
    while not shutdown_event.is_set():
        try:
            msg = input()
            if msg.lower() == exit_code:
                print("Exit code sent. Disconnecting from server...")
                sock.sendall(msg.encode())
                shutdown_event.set()
                break
            sock.sendall(msg.encode())
        except Exception as e:
            print(f"Error sending data: {e}")
            shutdown_event.set()
            break


def start_client():
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect((host, port))
    print(f'Connected to server at {host}:{port}')
    print(f'[INFO]: Type "exit!" to disconnect from the server')
    # Prompt the user to enter their name
    name = input("Enter your name: ")
    client_sock.sendall(name.encode())  # Send the name to the server

    try:
        # Start threads for sending and receiving messages
        receive_thread = threading.Thread(target=receive_msg, args=(client_sock,))
        send_thread = threading.Thread(target=send_msg, args=(client_sock,))

        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()

    except KeyboardInterrupt:
        print('\nKeyboard interrupt received. Shutting down client...')
        shutdown_event.set()

    finally:
        client_sock.close()
        print('Client shut down')


if __name__ == "__main__":
    start_client()
