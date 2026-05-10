import streamlit as st
import requests
from datetime import datetime, timedelta

# 🎨 إعدادات الصفحة الاحترافية
st.set_page_config(page_title="منصة أنس الرياضية PRO", page_icon="🏟️", layout="wide")

# 🖥️ تصميم مخصص CSS
st.markdown("""
    <style>
    .match-card { border: 2px solid #34495e; border-radius: 15px; padding: 20px; background-color: #1a1a1a; margin-bottom: 20px; }
    .live-badge { background-color: #e74c3c; padding: 5px 10px; border-radius: 10px; font-weight: bold; color: white; }
    .upcoming-badge { background-color: #f1c40f; padding: 5px 10px; border-radius: 10px; font-weight: bold; color: #1a1a1a; }
    .team-name { font-size: 18px; font-weight: bold; color: white; }
    </style>
    """, unsafe_allow_html=True)

# استدعاء المفتاح السري
API_KEY = st.secrets["FOOTBALL_API_KEY"]
HOST = "v3.football.api-sports.io"

def fetch_data(endpoint, params=None):
    headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': HOST}
    try:
        response = requests.get(f"https://{HOST}/{endpoint}", headers=headers, params=params)
        return response.json().get('response', [])
    except: return []

st.title("🏟️ محلل أنس الرياضي الذكي")

# 1. جلب المباريات المباشرة أولاً
live_matches = fetch_data("fixtures", {"live": "all"})

if live_matches:
    st.header("🔴 مباشر الآن")
    for m in live_matches:
        with st.container():
            st.markdown(f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-around; align-items: center; text-align: center;">
                    <div><img src="{m['teams']['home']['logo']}" width="60"><br><span class="team-name">{m['teams']['home']['name']}</span></div>
                    <div><span style="font-size:30px;">{m['goals']['home']} - {m['goals']['away']}</span><br><span class="live-badge">{m['fixture']['status']['elapsed']}'</span></div>
                    <div><img src="{m['teams']['away']['logo']}" width="60"><br><span class="team-name">{m['teams']['away']['name']}</span></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
else:
    # 2. إذا ماكو مباشر، نجيب جدول مباريات اليوم
    st.info("لا توجد مباريات مباشرة حالياً، إليك جدول مباريات اليوم:")
    today = datetime.now().strftime('%Y-%m-%d')
    today_matches = fetch_data("fixtures", {"date": today})
    
    if today_matches:
        for m in today_matches[:10]: # عرض أول 10 مباريات لليوم
            utc_dt = datetime.strptime(m['fixture']['date'], "%Y-%m-%dT%H:%M:%S%z")
            iq_time = (utc_dt + timedelta(hours=3)).strftime('%I:%M %p')
            st.markdown(f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="team-name">{m['teams']['home']['name']}</span>
                    <span class="upcoming-badge">🕒 {iq_time}</span>
                    <span class="team-name">{m['teams']['away']['name']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("لا توجد مباريات مسجلة لليوم حالياً.")

st.sidebar.write(f"🕒 توقيت العراق: {(datetime.now() + timedelta(hours=3)).strftime('%H:%M')}")
st.sidebar.write("تم التطوير بواسطة أنس البطل 🏆")
