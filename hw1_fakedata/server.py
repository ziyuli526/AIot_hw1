from flask import Flask, request, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DB_FILE = "aiotdb.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
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

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Server is running"})

@app.route('/sensor', methods=['POST'])
def receive_data():
    try:
        data = request.json
        temp = data.get('temperature')
        hum = data.get('humidity')
        ip = data.get('ip_address', 'unknown')
        rssi = data.get('rssi', 0)
        
        if temp is None or hum is None:
            return jsonify({"error": "Missing temperature or humidity"}), 400
            
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''
            INSERT INTO sensors (temperature, humidity, ip_address, rssi)
            VALUES (?, ?, ?, ?)
        ''', (temp, hum, ip, rssi))
        conn.commit()
        conn.close()
        
        return jsonify({"status": "success", "message": "Data inserted"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
