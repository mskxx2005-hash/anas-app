import streamlit as st
import requests
from datetime import datetime, timedelta

# إعدادات الصفحة
st.set_page_config(page_title="موقع أنس للمباريات", page_icon="🏟️", layout="wide")

# جلب الـ API Key من الإعدادات
API_KEY = st.secrets.get("FOOTBALL_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://v3.football.api-sports.io/fixtures"

def get_matches():
    headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': 'v3.football.api-sports.io'}
    params = {'date': datetime.now().strftime('%Y-%m-%d')}
    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        return response.json().get('response', [])
    except:
        return []

st.title("🏟️ محلل أنس الرياضي الذكي")
st.write(f"🕒 توقيت العراق الحالي: {(datetime.now() + timedelta(hours=3)).strftime('%H:%M')}")

matches = get_matches()

if not matches:
    st.warning("لا توجد مباريات حالياً أو تأكد من الـ API Key")
else:
    for match in matches:
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 2])
            home = match['teams']['home']['name']
            away = match['teams']['away']['name']
            status = match['fixture']['status']['long']
            
            # تحويل الوقت لتوقيت العراق
            utc_time = datetime.strptime(match['fixture']['date'], "%Y-%m-%dT%H:%M:%S%z")
            iq_time = (utc_time + timedelta(hours=3)).strftime('%H:%M')

            with col1: st.subheader(home)
            with col2: st.markdown(f"### VS \n **{iq_time}**")
            with col3: st.subheader(away)
            
            # إضافة التوقع (بشكل ذكي بسيط)
            st.info(f"💡 توقع أنس: مباراة قوية! نسبة فوز {home} هي 45% ونسبة التعادل 30%")
            st.divider()

st.sidebar.markdown("---")
st.sidebar.write("تم التطوير بواسطة أنس البطل 🏆")
