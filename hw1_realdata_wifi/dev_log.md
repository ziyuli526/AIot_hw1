# Development Log - Real ESP32 AIoT System

## Overview
This development log tracks the progress of building a local Python-based AIoT system designed to receive, store, and visualize real-time data from a real ESP32 hardware device equipped with a DHT11 sensor.

## Milestones Achieved

### 1. Environment Setup
- Initialized the Python virtual environment (`.venv`).
- Created `requirements.txt` incorporating necessary dependencies like `Flask`, `Streamlit`, `pandas`, and others.
- Installed dependencies to ensure a consistent development environment.

### 2. Backend API Development (`server.py`)
- Built a Flask API server to listen for HTTP POST requests from the ESP32 on port `5000`.
- Implemented an endpoint (`/sensor`) that accepts JSON or Form Data containing `temperature`, `humidity`, `rssi`, and `ip_address`.
- Created a mechanism to parse and validate incoming payload data.
- Built a `/health` endpoint for quick health checks of the server.

### 3. Database Integration (`aiotdb.db`)
- Designed an SQLite3 database schema. 
- Integrated automatic table creation via `server.py` upon startup.
- Configured logging of incoming sensor data into the `sensors` table with an auto-incrementing `id` and an automatic `timestamp`.

### 4. Interactive Dashboard Development (`app.py`)
- Designed a frontend Streamlit application running on port `8501`.
- Built KPI cards to display the latest temperature, humidity, and RSSI readings.
- Added dynamic line charts to track historical data trends for temperature and humidity.
- Configured an auto-refresh cycle (every 5 seconds) to reflect the real-time nature of the AIoT data.
- Added a raw data table view for deeper inspection.

### 5. Hardware Integration & Testing
- Developed ESP32 sketch code (in `sketch_mar28a`) to connect to the local WiFi and collect data from the DHT11 sensor via GPIO 2.
- Implemented the HTTP POST routine to periodically send payload over WiFi to the local server.
- Validated system robustness and uninterrupted data flow from hardware to the database and finally to the interactive dashboard.

## Next Steps
- Further optimize the Streamlit dashboard performance and explore custom UI styling.
- Add simple authentication or validation for the Flask API to secure data entry.
- Implement data export functionality (e.g., download as CSV) from the dashboard.
- Test broader network accessibility if needed.
