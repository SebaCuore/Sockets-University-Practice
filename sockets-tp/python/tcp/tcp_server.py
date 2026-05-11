import socket 
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(("localhost", 6000)) 
server.listen(1) 
print("Servidor TCP escuchando en puerto 6000...") 

separador = "-" * 65
print(separador)
print(f"{'TYPE':<15}{'SENSOR':<10}{'METRIC':<12}{'VALUE':<15}{'PRIORITY':<10}")
print(separador)

while True: 
    conn, addr = server.accept() 

    while True: 
        data = conn.recv(1024) 
        if not data: 
            break 
        message = json.loads(data.decode())
        
        print(f"{message['type']:<15}{message['sensor_id']:<10}{message['metric']:<12}{round(message['value'], 2):<15}{message['priority']:<10}")
        conn.sendall(b"Alerta TCP recibida correctamente") 
    conn.close()