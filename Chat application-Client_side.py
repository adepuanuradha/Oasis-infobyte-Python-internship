 import socket
import threading

# Client configuration
HOST = '127.0.0.1'  # localhost
PORT = 5500

# Create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            # Receive message from server
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break
            print(msg)
        except Exception as e:
            print(f'Error receiving message: {str(e)}')
            break

def send_message():
    while True:
        msg = input()
        try:
            # Send message to server
            client.send(msg.encode('utf-8'))
        except Exception as e:
            print(f'Error sending message: {str(e)}')
            break

if __name__ == "__main__":
    # Create threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_message)
    send_thread.start()
