import socket
from datetime import datetime
# Server configuration
HOST='127.0.0.1'
PORT=12345
def start_client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((HOST,PORT))
    except ConnectionRefusedError:
        print("[ERROR] Could not connect to the server. Is chat_server.py running?")
        return
    # Receive welcome message
    welcome_msg=client.recv(1024).decode('utf-8')
    print(f"[SERVER]:{welcome_msg}")
    while True:
        try:
            # Send message to server
            timestamp=datetime.now().strftime("%H:%M")
            message=input(f"[{timestamp}]Client(You):")
            client.send(message.encode('utf-8'))            
            if message.lower()=='exit':
                print("Disconnecting...")
                break                
            # Receive reply from server
            reply=client.recv(1024).decode('utf-8')
            if not reply or reply.lower()=='exit':
                print("[SERVER DISCONNECTED] Server closed the chat.")
                break                 
            timestamp=datetime.now().strftime("%H:%M")
            print(f"[{timestamp}]Server:{reply}")
        except ConnectionResetError:
            print("[ERROR] Lost connection to the server.")
            break
    client.close()
if __name__=="__main__":
    start_client()