import socket
import threading
from datetime import datetime
# Server configuration
HOST='127.0.0.1'  # Localhost
PORT=12345        # Port to listen on
def handle_client(client_socket,client_address):
    print(f"[NEW CONNECTION]{client_address}connected.")
    client_socket.send("Welcome to the Chat Server! Type your message...".encode('utf-8'))    
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message.lower()=='exit':
                print(f"[DISCONNECT]{client_address}disconnected gracefully.")
                break                
            # Get current timestamp
            timestamp=datetime.now().strftime("%H:%M")
            print(f"[{timestamp}]Client:{message}")            
            # Send a response back to the client
            server_reply=input(f"[{timestamp}]Server(You):")
            client_socket.send(server_reply.encode('utf-8'))           
            if server_reply.lower()=='exit':
                print("[SERVER SHUTDOWN]Closing connection.")
                break
        except ConnectionResetError:
            print(f"[ERROR] Connection lost with{client_address}")
            break
    client_socket.close()
def start_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen(1)
    print(f"[STARTING]Server is listening on {HOST}:{PORT}...") 
    # Accept one client connection for this simple beginner tier chat
    client_socket,client_address=server.accept()
    handle_client(client_socket,client_address)
if __name__=="__main__":
    start_server()