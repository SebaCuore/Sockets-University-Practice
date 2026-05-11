# Distributed Industrial Monitoring System (UDP/TCP Sockets)

This project implements an industrial simulation system for real-time telemetry supervision and critical alerts. [cite_start]It was developed as a practical case study for the **Data Networks** course, demonstrating distributed process communication using Python's socket interface[cite: 19, 20].

## 🚀 Project Overview
[cite_start]The system simulates an advanced manufacturing environment where multiple sensors report operational variables to a central server[cite: 21]. [cite_start]The architecture strategically separates network responsibilities based on **Transport Layer** requirements[cite: 22]:

* [cite_start]**Periodic Telemetry (UDP):** Sensors continuously transmit temperature, pressure, and vibration data[cite: 22]. [cite_start]The **UDP (SOCK_DGRAM)** protocol is used to prioritize speed and low latency for non-critical data streams[cite: 23].
* **Critical Alert Management (TCP):** When a metric exceeds a predefined safety threshold (e.g., Temp > 80°C), the system switches to **TCP (SOCK_STREAM)**[cite: 24, 403]. [cite_start]This ensures a reliable, connection-oriented, and guaranteed delivery channel for reporting critical incidents[cite: 25, 458].


## 🛠️ Technical Features
* [cite_start]**Object-Oriented Programming (OOP):** A `Sensor` class encapsulates the business logic, data validation, and measurement simulation[cite: 26, 285].
* **Statistical Simulation:** Integration of the `random` library using **Gaussian (Normal)** distributions for temperature/pressure and **Uniform** distributions for vibration to replicate real-world industrial noise[cite: 27, 407, 408].
* [cite_start]**JSON Data Exchange:** Messages are serialized into JSON format, ensuring a clear and scalable data structure for both telemetry and alerts[cite: 28, 240, 256].
* [cite_start]**Real-time Dashboard:** The servers utilize Python's f-string alignment features to create a formatted console dashboard that displays multi-sensor data in an organized table[cite: 29, 341, 358].

## 📂 Project Structure
```plaintext
├── sensor.py              # Sensor logic and statistical data generation
├── clients_simulator.py   # Orchestrator: manages UDP telemetry and TCP alert triggers
├── udp_server.py          # Receiver for high-frequency periodic telemetry
└── tcp_server.py          # Receiver for critical alerts (Persistent listening loop)