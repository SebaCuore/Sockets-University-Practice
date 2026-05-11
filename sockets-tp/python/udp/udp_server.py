import socket 
import json

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server.bind(("localhost", 5005)) 
print("Servidor UDP escuchando en puerto 5005...") 

separador = "-" * 65
print(separador)
print(f"{'SENSOR':<15}{'TEMP':<10}{'PRESSURE':<12}{'VIBRATION':<15}{'STATUS':<10}")
print(separador)

while True: 
    data, addr = server.recvfrom(1024) 
    message = json.loads(data.decode())

    print(f"{message['sensor_id']:<15}{round(message['temperature'], 0):<10}{round(message['pressure'], 0):<12}{round(message['vibration'], 2):<15}{message['status']:<10}")

    server.sendto(b"Mensaje recibido", addr)

