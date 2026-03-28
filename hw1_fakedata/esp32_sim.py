import requests
import time
import random

SERVER_URL = "http://127.0.0.1:5000/sensor"

def generate_dht11_data():
    # Simulate DHT11 ranges: Temp 20-35 C, Hum 40-70%
    temperature = round(random.uniform(20.0, 35.0), 1)
    humidity = round(random.uniform(40.0, 70.0), 1)
    return temperature, humidity

def simulate():
    print("Starting ESP32 Simulator...")
    while True:
        temp, hum = generate_dht11_data()
        payload = {
            "temperature": temp,
            "humidity": hum,
            "ip_address": "192.168.1.100",
            "rssi": random.randint(-80, -40)
        }
        
        try:
            print(f"Sending data: {payload}")
            response = requests.post(SERVER_URL, json=payload, timeout=5)
            print(f"Server response [{response.status_code}]: {response.text}")
        except Exception as e:
            print(f"Failed to send data: {e}")
            
        time.sleep(5)

if __name__ == "__main__":
    simulate()
