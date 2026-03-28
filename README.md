# AIoT System Projects (Homework 1)

This repository contains two variations of a locally hosted AIoT (Artificial Intelligence of Things) demonstration system, built for Homework 1. Both projects feature a Flask-based backend server that stores sensor data (Temperature, Humidity, RSSI, and IP address) into a lightweight SQLite3 database (`aiotdb.db`), and a Streamlit-based web dashboard (`app.py`) for real-time data visualization.

## Directory Structure

### 1. [hw1_fakedata](./hw1_fakedata)
**Local AIoT Demo with Python Simulator**

This folder contains a fully software-based demonstration of the system. Rather than using physical hardware, this directory utilizes a Python script (`esp32_sim.py`) that acts as an ESP32 simulator. 
- It generates synthetic DHT11 sensor data (temperature and humidity) as well as simulated WiFi connection metrics.
- The simulator continuously pushes HTTP POST requests to the Flask server every 5 seconds.
- Ideal for testing the database setup, backend API logic, and frontend Streamlit dashboard independently of any physical hardware limits.

### 2. [hw1_realdata_wifi](./hw1_realdata_wifi)
**Real-Time Dashboard with Physical ESP32 Integration**

This folder is designed to interface with actual hardware. Instead of a Python simulator, the frontend dashboard and backend API interact with a physical ESP32 micro-controller over a local WiFi network.
- Requires an ESP32 programmed to read from a real DHT11 sensor via a GPIO pin.
- The physical device directly sends HTTP POST requests to the local Flask server endpoints.
- Provides a genuine end-to-end IoT tracking pipeline from a physical environment to a digital dashboard.

## Getting Started

To run either of these implementations, navigate into the respective folder and see the specific `README.md` provided within it.

1. Pick the version you want to run (e.g., `cd hw1_realdata_wifi`).
2. Create your virtual environment and install the required dependencies: `pip install -r requirements.txt`.
3. Start the Flask server: `python server.py`.
4. Start the Streamlit dashboard: `streamlit run app.py`.
5. Run the simulator script (`hw1_fakedata`) OR power up your programmed ESP32 (`hw1_realdata_wifi`).
