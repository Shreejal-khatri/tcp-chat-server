import socket
HOST = "0.0.0.0"
PORT = 5000

#TCP using IPv4. 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Server being staged live at port 5000
server_socket.bind((HOST, PORT))

#Ready for connection and can handle 1 connection 
server_socket.listen(1)

#blocking call
conn, addr = server_socket.accept()

#Read up to 1024 bytes from the client
data = conn.recv(1024)

#data is in bytes so decode() turns bytes into a string
print(f"Recievd: {data.decode()}")

conn.close()
server_socket.close()