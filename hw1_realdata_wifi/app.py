import streamlit as st
import pandas as pd
import sqlite3
import time

# Page config
st.set_page_config(page_title="AIoT Real-Time Dashboard", page_icon="📡", layout="wide")

DB_NAME = 'aiotdb.db'

def load_data():
    try:
        conn = sqlite3.connect(DB_NAME)
        # Select last 100 records
        query = "SELECT * FROM sensors ORDER BY timestamp DESC LIMIT 100"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except sqlite3.OperationalError:
        return pd.DataFrame()

st.title("📡 AIoT Real-Time Dashboard - ESP32 Data")

df = load_data()

if not df.empty:
    latest_data = df.iloc[0]
    
    # KPI Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Latest Temperature (°C)", value=f"{latest_data['temperature']:.1f}")
    with col2:
        st.metric(label="Latest Humidity (%)", value=f"{latest_data['humidity']:.1f}")
    with col3:
        st.metric(label="Last Update", value=latest_data['timestamp'])

    # Line charts
    st.subheader("Sensor Trends")
    chart_col1, chart_col2 = st.columns(2)
    
    # Sort chronological for charts (oldest to newest)
    chart_df = df.sort_values("timestamp")
    
    with chart_col1:
        st.write("Temperature (°C) over time")
        st.line_chart(chart_df, x="timestamp", y="temperature", color="#FF5733")
        
    with chart_col2:
        st.write("Humidity (%) over time")
        st.line_chart(chart_df, x="timestamp", y="humidity", color="#33C1FF")

    # Raw Data Table
    st.subheader("Raw Sensor Data")
    st.dataframe(df, use_container_width=True)

else:
    st.warning("No data found in database. Waiting for real ESP32 to send data...")

# Auto refresh every 5 seconds
time.sleep(5)
st.rerun()
