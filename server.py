import socket
#run code in parallel
import threading

HOST = "0.0.0.0"
PORT = 5000

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print(f"[DISCONNECTED] {addr}")
                break

            message = data.decode()
            print(f"[{addr}] {message}")

        except ConnectionResetError:
            print(f"[ERROR] {addr} connection reset.")
            break

    conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"[LISTENING] Server listening on {HOST}:{PORT}")

#Keeps the server running
while True:
    #One thread Per Client
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()