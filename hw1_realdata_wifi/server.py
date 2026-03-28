from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)
DB_NAME = 'aiotdb.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS sensors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        temperature REAL,
        humidity REAL,
        ip_address TEXT,
        rssi INTEGER
    )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/sensor', methods=['POST'])
def receive_sensor_data():
    try:
        # Check if json or form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        temperature = data.get('temperature')
        humidity = data.get('humidity')
        rssi = data.get('rssi')
        
        # Get real client IP. In some setups, this might be a proxy IP if not configured correctly, 
        # but for local wifi esp32 -> flask, remote_addr is fine.
        ip_address = request.remote_addr

        if temperature is not None and humidity is not None:
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()
            c.execute('''
                INSERT INTO sensors (temperature, humidity, ip_address, rssi)
                VALUES (?, ?, ?, ?)
            ''', (float(temperature), float(humidity), ip_address, int(rssi) if rssi else None))
            conn.commit()
            conn.close()
            return jsonify({"status": "success", "message": "Data stored successfully"}), 201
        else:
            return jsonify({"status": "error", "message": "Missing temperature or humidity data"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run on all interfaces to receive requests from network (ESP32)
    app.run(host='0.0.0.0', port=5000, debug=False)
