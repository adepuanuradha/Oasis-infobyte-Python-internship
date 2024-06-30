import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 5500

# Create a socket for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# List to keep track of client connections
clients = []

def handle_client(client_socket, addr):
    while True:
        try:
            # Receive message from client
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                # If no message, remove the client and close the connection
                clients.remove(client_socket)
                client_socket.close()
                break
            # Broadcast message to all connected clients
            print(f'Received message from {addr}: {msg}')
            broadcast(msg, client_socket)
        except Exception as e:
            print(f'Error handling client {addr}: {str(e)}')
            break

def broadcast(msg, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(msg.encode('utf-8'))
            except Exception as e:
                print(f'Error broadcasting message: {str(e)}')

def start_server():
    # Listen for incoming connections
    server.listen()
    print(f'Server is listening on {HOST}:{PORT}')

    while True:
        # Accept new connection
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f'Connection established with {addr}')

        # Create a thread to handle each client
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
