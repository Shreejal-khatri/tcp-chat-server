import socket
#run code in parallel
import threading

HOST = "0.0.0.0"
PORT = 5000

#all the connected clients and mapping username to client's IP 
clients = []
usernames = {} 

def broadcast(message, sender_conn): 
    for client in clients:
        #ensure message is not sent back to the sender
        if client != sender_conn: 
            try: 
                client.sendall(message.encode())
            except: 
                #ignoring broken connections
                pass

def handle_client(conn, addr): 
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    #default username is IP of the client
    usernames[conn] = f"{addr}" 

    #sends a welcome message to all clients
    conn.sendall("Welcome! Set your username with /nick YourName\n".encode())

    while True: 
        try: 
            #waiting for connection upto 1024 bytes from clients
            data = conn.recv(1024)
            if not data: 
                break
            
            message = data.decode().strip()

            #handling /nick command
            if message.startswith("/nick "):
                new_name = message[6:].strip()
                old_name = usernames[conn]
                usernames[conn] = new_name
                broadcast(f"[INFO] {old_name} is now known as {new_name}", conn)
                conn.sendall(f"[INFO] Your username is now {new_name}\n".encode())
                continue
            
            #normal messages
            sender_name = usernames.get(conn, str(addr))
            print(f"[{sender_name}] {message}")
            broadcast(f"{sender_name}: {message}", conn)
        
        #disconnect handling 
        except ConnectionResetError:
            break
    
    print(f"[DISCONNECTED] {usernames.get(conn, addr)}")
    broadcast(f"[INFO] {usernames.get(conn, addr)} has left the chat.", conn)
    clients.remove(conn)
    usernames.pop(conn, None)
    conn.close()

#server Loop
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"[LISTENING] Server Listening On {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()