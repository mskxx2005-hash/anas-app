# --- صفحة المباريات (تحديث القناص) ---
import streamlit as st
import requests

# إعدادات الواجهة
st.set_page_config(page_title="AI Football Center", layout="wide")

# الربط الرسمي (API) - هذا ما يغدر بيك
API_KEY = "4f74f8c769e012d50f70c0fe7e344070"
headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': 'v3.football.api-sports.io'}

if 'page' not in st.session_state: st.session_state.page = 'home'
def change_page(p): st.session_state.page = p

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚽ مركز تحليل كرة القدم</h1>", unsafe_allow_html=True)
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📅 مباريات اليوم المباشرة", use_container_width=True): change_page('matches')
    with col2:
        if st.button("🔴 غرفة التحليل الذكي", use_container_width=True): change_page('live')
    st.write("---")
    st.markdown("<p style='text-align: center;'>📸 Instagram: <b>06cb4</b></p>", unsafe_allow_html=True)

# --- صفحة المباريات (بالطريقة الرسمية المضمونة) ---
elif st.session_state.page == 'matches':
    if st.button("⬅️ عودة"): change_page('home')
    st.header("🏟️ مباريات جارية الآن")
    
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    res = requests.get(url, headers=headers).json()
    matches = res.get('response', [])
    
    if not matches:
        st.info("حالياً ماكو مباريات لايف، هاي قائمة بأهم مباريات اليوم:")
        # نجيب مباريات اليوم العادية إذا ماكو لايف
        from datetime import datetime
        url_today = f"https://v3.football.api-sports.io/fixtures?date={datetime.now().strftime('%Y-%m-%d')}"
        res = requests.get(url_today, headers=headers).json()
        matches = res.get('response', [])

    for m in matches[:15]:
        home = m['teams']['home']['name']
        away = m['teams']['away']['name']
        score_h = m['goals']['home'] if m['goals']['home'] is not None else 0
        score_a = m['goals']['away'] if m['goals']['away'] is not None else 0
        status = m['fixture']['status']['elapsed']
        
        st.markdown(f"""
        <div style="background:#1e1e1e; padding:15px; border-radius:10px; margin-bottom:10px; border-right: 5px solid #4CAF50;">
            <small style="color:#28a745;">الدقيقة: {status}'</small><br>
            <div style="display: flex; justify-content: space-between;">
                <span><b>{home}</b></span>
                <span style="color:#4CAF50;">{score_h} - {score_a}</span>
                <span><b>{away}</b></span>
            </div>
        </div>
        """, unsafe_allow_html=True)
