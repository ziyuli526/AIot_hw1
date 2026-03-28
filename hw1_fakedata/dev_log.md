# Development Log

## 2026-03-28
- **AIoT Demo Setup Completed**: 
  - Created a Python virtual environment (`venv`).
  - Set up `requirements.txt` with necessary dependencies (`flask`, `streamlit`, `requests`, `pandas`).
  - Created `server.py`: Flask backend with an SQLite database (`aiotdb.db`) configured to receive and store sensor data securely.
  - Created `esp32_sim.py`: ESP32 simulator sending generated DHT11 temperature and humidity data (along with mock IP and RSSI values) to the Flask backend every 5 seconds.
  - Created `app.py`: Streamlit frontend dashboard displaying the latest sensor metrics, line charts for temperature and humidity trends, and a raw data table.
  - **Status**: All services successfully launched and verified. Simulated data is actively being recorded, and the real-time web interface is accessible at `http://localhost:8501`.
