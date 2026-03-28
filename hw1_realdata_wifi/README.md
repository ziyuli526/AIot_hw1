# AIoT Real-Time Sensor Dashboard

This project is a local Python-based AIoT system designed to receive, store, and visualize real-time data from a real ESP32 hardware device equipped with a DHT11 sensor.

## Project Structure

- `server.py`: A Flask API backend that listens for incoming HTTP POST requests from the ESP32 and stores the structured sensor data (Temperature, Humidity, RSSI, and IP address) into a local SQLite3 database (`aiotdb.db`).
- `app.py`: A Streamlit interactive web dashboard that reads from the SQLite database to display key metrics (KPI cards), dynamic line charts for temperature and humidity trends, and a raw data table. It automatically refreshes every 5 seconds.
- `requirements.txt`: Python package dependencies.
- `aiotdb.db`: SQLite database automatically created upon starting the server.

## Hardware Setup (ESP32)

Your ESP32 should be programmed to:
1. Connect to the same local WiFi network as the machine running this project.
2. Read data from the DHT11 sensor (connected to GPIO 2).
3. Send an HTTP POST request to `http://<YOUR_MACHINE_IP>:5000/sensor` every 5 seconds.

### Acceptable Payload Formats
The server accepts both JSON and Form Data with the following fields:
- `temperature`: (float) e.g., `24.5`
- `humidity`: (float) e.g., `60.2`
- `rssi`: (int, optional) e.g., `-50`

## Installation

1. Ensure you have Python 3.8+ installed.
2. (Optional but recommended) Create and activate a Virtual Environment.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

You need to run the API server and the Dashboard simultaneously in two separate terminal windows.

**1. Start the Flask API Server:**
```bash
python server.py
```
*The server will start on `0.0.0.0:5000`. Windows Firewall may prompt you to allow access; please grant it. You can verify the server is running by visiting `http://localhost:5000/health` (should return `{"status": "ok"}`).*

**2. Start the Streamlit Dashboard:**
```bash
streamlit run app.py
```
*The dashboard will automatically open in your browser at `http://localhost:8501`. If no data is showing, ensure your ESP32 is powered on and sending data to the correct IP address.*

## Database Schema

The SQLite database uses the following table schema for the `sensors` table:
```sql
CREATE TABLE IF NOT EXISTS sensors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperature REAL,
    humidity REAL,
    ip_address TEXT,
    rssi INTEGER
);
```
