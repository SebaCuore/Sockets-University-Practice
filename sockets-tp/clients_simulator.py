import socket
import json
from sensor import Sensor

def tcp_alert(json_alert_data):
    clientTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    clientTcp.connect(("localhost", 6000)) 

    data = json.dumps(json_alert_data)
    b = data.encode()
    clientTcp.sendall(b)
    data = clientTcp.recv(1024)
    print("Respuesta:", data.decode())
    clientTcp.close()

Sensors = [
    Sensor(id="SENSOR_01", temperature=25, vibration=0.5, pressure=1.0, status='OK'),
    Sensor(id="SENSOR_02", temperature=30, vibration=0.7, pressure=1.2, status='OK'),
]

clientUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("localhost", 5005) 

active = True
while active:
    for sensor in Sensors:
        sensor.update_metrics()
        if sensor.temperature > 80:
            tcp_alert(sensor.get_alert("temperature", sensor.temperature))
            continue
        elif sensor.pressure > 150:
            tcp_alert(sensor.get_alert("pressure", sensor.pressure))
            continue
        elif sensor.vibration > 8:
            tcp_alert(sensor.get_alert("vibration", sensor.vibration))
            continue
        data = json.dumps(sensor.get_data())
        b = data.encode()
        clientUdp.sendto(b, server_addr) 
        data, _ = clientUdp.recvfrom(1024) 
        print("Respuesta:", data.decode())
    print("next?")
    if input().lower() == 'n':
        active = False