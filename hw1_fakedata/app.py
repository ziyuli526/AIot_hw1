import streamlit as st
import sqlite3
import pandas as pd

DB_FILE = "aiotdb.db"

st.set_page_config(page_title="AIoT Dashboard", layout="wide")
st.title("AIoT Sensor Dashboard")

def load_data():
    try:
        conn = sqlite3.connect(DB_FILE)
        query = "SELECT timestamp, temperature, humidity, ip_address, rssi FROM sensors ORDER BY timestamp DESC LIMIT 100"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        return pd.DataFrame()

df = load_data()

if not df.empty:
    # Top metrics
    latest = df.iloc[0]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Latest Temperature", f"{latest['temperature']} °C")
    col2.metric("Latest Humidity", f"{latest['humidity']} %")
    col3.metric("Last Update", latest['timestamp'])
    
    st.markdown("---")
    
    # Process data for charts
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    chart_df = df.sort_values('timestamp').set_index('timestamp')
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Temperature History")
        st.line_chart(chart_df['temperature'], color="#ff4b4b")
        
    with col2:
        st.subheader("Humidity History")
        st.line_chart(chart_df['humidity'], color="#0068c9")
        
    st.markdown("---")
    st.subheader("Recent Data Table")
    st.dataframe(df.head(20), use_container_width=True)
    
    # Auto-refresh button
    if st.button("Refresh Data"):
        st.rerun()
else:
    st.info("No data available yet. Waiting for ESP32 simulator...")
