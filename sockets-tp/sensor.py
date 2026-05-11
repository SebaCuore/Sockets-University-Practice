import json
import random

class Sensor: 
    def __init__(self, id, temperature, vibration, pressure, status):
        self.id = id
        if temperature < 0:
            raise ValueError("Temperature must be 0 or higher.")
        self.temperature = temperature
        
        if pressure < 0:
            raise ValueError("Pressure must be 0 or higher.")
        self.pressure = pressure

        if vibration < 0:
            raise ValueError("Vibration must be 0 or higher.")
        self.vibration = vibration

        if status not in ['OK', 'ALERT']:
            raise ValueError("Status must be 'OK' or 'ALERT'.")
        self.status = status

    def get_data(self):
        return{
            'sensor_id': self.id,
            'temperature': self.temperature,
            'vibration': self.vibration,
            'pressure': self.pressure,
            'status': self.status
        }
    
    def get_alert(self, metric, value):
        return {
            'type': "ALERT",
            'sensor_id': self.id,
            'metric': metric,
            'value': value,
            'priority': 'high' if metric == 'temperature' else 'medium' if metric == 'pressure' else 'low'
        }
    
    def update_metrics(self):
        self.temperature = random.gauss(75, 2.0)
        self.vibration = random.uniform(0.1, 9.9)
        self.pressure = random.gauss(110, 20.0)
