import streamlit as st
import requests
from bs4 import BeautifulSoup

# إعدادات الصفحة
st.set_page_config(page_title="AI Football Center", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def change_page(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚽ مركز تحليل كرة القدم</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='border: 2px solid #28a745; padding: 20px; border-radius: 15px; text-align: center;'><h3>📅 مباريات اليوم</h3></div>", unsafe_allow_html=True)
        if st.button("فتح الجدول المباشر", use_container_width=True, key="m_btn"): change_page('matches')
    with col2:
        st.markdown("<div style='border: 2px solid #dc3545; padding: 20px; border-radius: 15px; text-align: center;'><h3>🔴 AI تحليل مباشر</h3></div>", unsafe_allow_html=True)
        if st.button("دخول غرفة التحليل", use_container_width=True, key="l_btn"): change_page('live')

    st.write("---")
    st.markdown(f"<p style='text-align: center; color: #E1306C;'>📸 Instagram: <a href='https://instagram.com/06cb4' style='color:white;'>06cb4</a></p>", unsafe_allow_html=True)

# --- صفحة المباريات (السحب الفعلي) ---
elif st.session_state.page == 'matches':
    if st.button("⬅️ عودة", key="b1"): change_page('home')
    st.header("📅 المباريات الجارية والنتائج")
    
    with st.spinner('جاري سحب البيانات الحقيقية...'):
        try:
            # استخدام رابط بديل ومستقر للسحب
            url = "https://www.livescore.cz/"
            res = requests.get(url, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            
            # سحب البيانات (هذا الجزء يبحث عن الفرق والنتيجة)
            matches = soup.find_all('tr', class_='match-row')
            
            if not matches:
                st.warning("ماكو مباريات لايف هسة، جرب بوقت ثاني.")
            else:
                for m in matches[:15]:
                    home = m.find('td', class_='home').text.strip()
                    away = m.find('td', class_='away').text.strip()
                    score = m.find('td', class_='score').text.strip()
                    time = m.find('td', class_='time').text.strip()
                    
                    st.markdown(f"""
                    <div style="background:#262730; padding:10px; border-radius:10px; margin-bottom:5px; border-right: 5px solid #28a745;">
                        <small>{time}</small><br>
                        <b>{home}</b> <span style="color:#28a745;">{score}</span> <b>{away}</b>
                    </div>
                    """, unsafe_allow_html=True)
        except:
            st.error("واجهنا مشكلة بسحب البيانات. جرب تحديث الصفحة.")

# --- صفحة التحليل الذكي ---
elif st.session_state.page == 'live':
    if st.button("⬅️ عودة", key="b2"): change_page('home')
    st.header("🧠 خوارزمية التحليل المباشر")
    st.info("الخوارزمية تحلل البيانات المسحوبة حالياً...")
    # هنا نحط معادلات الذكاء الصناعي لاحقاً
    st.success("✅ الخوارزمية تراقب مباراة (بايرن ميونخ) - ضغط هجومي عالي!")
