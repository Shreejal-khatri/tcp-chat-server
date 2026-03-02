import socket 
HOST = "127.0.0.1"
PORT = 5000

#TCP using IPv4. 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = input("Enter a message: ")
client_socket.sendall(message.encode())

client_socket.close()