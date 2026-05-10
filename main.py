import streamlit as st
import requests
import pandas as pd

# إعدادات الصفحة (تخليها تشبه المواقع الاحترافية)
st.set_page_config(page_title="مركز تحليل المباريات الذكي", layout="wide")

API_KEY = "4f74f8c769e012d50f70c0fe7e344070"

st.title("⚽ مركز المباريات المباشر (AI)")
st.sidebar.header("لوحة التحكم")

def get_data():
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': 'v3.football.api-sports.io'}
    return requests.get(url, headers=headers).json()

data = get_data()
matches = data.get('response', [])

if not matches:
    st.info("🏟️ لا توجد مباريات مباشرة حالياً. سيتم التحديث تلقائياً عند البدء.")
else:
    for m in matches:
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 2])
            
            with col1:
                st.subheader(m['teams']['home']['name'])
                st.image(m['teams']['home']['logo'], width=60)
            
            with col2:
                st.header(f"{m['goals']['home']} - {m['goals']['away']}")
                st.write(f"⏱️ دقيقة: {m['fixture']['status']['elapsed']}'")
            
            with col3:
                st.subheader(m['teams']['away']['name'])
                st.image(m['teams']['away']['logo'], width=60)
            
            # قسم التحليل الذكي (خوارزمية بسيطة)
            st.markdown("---")
            st.info("🤖 تحليل AI: الفريق " + (m['teams']['home']['name'] if m['goals']['home'] > m['goals']['away'] else m['teams']['away']['name']) + " يسيطر حالياً.")
