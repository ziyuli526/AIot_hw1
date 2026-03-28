# AIoT Local Demo: DHT11 Sensor Simulation
<img width="2537" height="1178" alt="image" src="https://github.com/user-attachments/assets/e68fb21f-c3d5-4ecc-abf0-cd928933b466" />


This project is a fully local AIoT demonstration simulating an ESP32 micro-controller that sends DHT11 module data (temperature and humidity) to a backend server. The data is stored in a lightweight SQLite database and visualized in real-time using a digital dashboard.

**Local Website Link:** [http://localhost:8501](http://localhost:8501) (Ensure services are running)

## System Architecture

The project consists of three main components:
1. **ESP32 Simulator (`esp32_sim.py`)**: A Python script simulating an IoT end-device. It generates random temperature and humidity data every 5 seconds, emulating a DHT11 sensor, along with WiFi metadata (IP address and RSSI).
2. **Backend Server (`server.py`)**: A Flask-based REST API that receives HTTP POST requests from the simulator and securely stores the telemetry data into a local SQLite3 database (`aiotdb.db`).
3. **Frontend Dashboard (`app.py`)**: A Streamlit web application that queries the SQLite database to display key performance indicators (KPIs), raw data tables, and historical line charts.

## Prerequisites

- Python 3.9+
- Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ziyuli526/AIot_hw1.git
   cd AIot_hw1
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the full demonstration, you will need to open three separate terminal windows and ensure your virtual environment is activated in all of them.

### 1. Start the Backend Server
Run the Flask API server to listen for incoming sensor data:
```bash
python server.py
```
*The server will start on `http://127.0.0.1:5000`. You can verify it by visiting `http://127.0.0.1:5000/health`.*

### 2. Start the ESP32 Simulator
Run the simulator to begin pushing fake DHT11 data to the server:
```bash
python esp32_sim.py
```
*You should see output indicating successful HTTP 201 responses from the server.*

### 3. Start the Web Dashboard
Run the Streamlit application to visualize the data:
```bash
streamlit run app.py
```
*The dashboard will automatically open in your default browser at `http://localhost:8501`. Click "Refresh Data" to view the latest simulated telemetry.*

## File Overview
- `requirements.txt`: Python package dependencies.
- `server.py`: Flask backend setup and SQLite DB initialization.
- `esp32_sim.py`: Simulator script for DHT11 data generation.
- `app.py`: Streamlit frontend layout and data charting.
- `dev_log.md`: Development tracking logs.
