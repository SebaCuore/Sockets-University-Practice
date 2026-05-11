import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server_addr = ("localhost", 5005) 

client.sendto(b"Hola servidor UDP", server_addr) 
data, _ = client.recvfrom(1024) 
print("Respuesta:", data.decode())