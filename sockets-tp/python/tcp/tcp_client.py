import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(("localhost", 6000)) 
client.sendall(b"Hola servidor TCP") 

data = client.recv(1024) 
print("Respuesta:", data.decode()) 
client.close()