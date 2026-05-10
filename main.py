import streamlit as st
import requests
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="AI Football Center", layout="wide")

API_KEY = "4f74f8c769e012d50f70c0fe7e344070"

st.title("⚽ مركز المباريات المباشر (AI)")
st.sidebar.header("لوحة التحكم")

def get_data():
    # لاحظ المسافات هنا، ضروري تكون موجودة حتى ما يطلع خطأ
    url = "https://v3.football.api-sports.io/fixtures?date=2026-05-10"
    headers = {
        'x-rapidapi-key': API_KEY, 
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# جلب البيانات
data = get_data()
matches = data.get('response', [])

if not matches:
    st.info("🏟️ لا توجد مباريات مسجلة لهذا التاريخ.")
else:
    for m in matches:
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 2])
            
            with col1:
                st.subheader(m['teams']['home']['name'])
                st.image(m['teams']['home']['logo'], width=60)
            
            with col2:
                home_goals = m['goals'].get('home', 0)
                away_goals = m['goals'].get('away', 0)
                st.header(f"{home_goals} - {away_goals}")
                status = m['fixture']['status']['long']
                st.write(f"⏱️ الحالة: {status}")
            
            with col3:
                st.subheader(m['teams']['away']['name'])
                st.image(m['teams']['away']['logo'], width=60)
            
            st.markdown("---")
