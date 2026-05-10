import streamlit as st
import requests
from bs4 import BeautifulSoup

# إعدادات الصفحة
st.set_page_config(page_title="AI Football Center", layout="wide")

# إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def change_page(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚽ مرحبا بكم في عالم كرة القدم</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div style='border: 2px solid #28a745; padding: 20px; border-radius: 15px; text-align: center;'><h2>📅 مباريات اليوم</h2></div>", unsafe_allow_html=True)
        if st.button("فتح قسم مباريات اليوم", use_container_width=True, key="btn_matches"):
            change_page('matches')

    with col2:
        st.markdown("<div style='border: 2px solid #dc3545; padding: 20px; border-radius: 15px; text-align: center;'><h2>🔴 AI مباشر + تحليل</h2></div>", unsafe_allow_html=True)
        if st.button("الدخول للبث والتحليل", use_container_width=True, key="btn_live"):
            change_page('live')

    st.write(" ") 
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("<div style='border: 2px solid #007bff; padding: 20px; border-radius: 15px; text-align: center;'><h2>📊 الخوارزميات الذكية</h2></div>", unsafe_allow_html=True)
        if st.button("استعراض الإحصائيات", use_container_width=True, key="btn_stats"):
            change_page('stats')

    with col4:
        st.markdown(f"<div style='border: 2px solid #E1306C; padding: 20px; border-radius: 15px; text-align: center;'><h2>📸 Instagram</h2><p>06cb4</p></div>", unsafe_allow_html=True)
        st.link_button("زيارة حسابي", "https://instagram.com/06cb4", use_container_width=True)

# --- صفحة مباريات اليوم (سحب حقيقي) ---
elif st.session_state.page == 'matches':
    if st.button("⬅️ العودة للرئيسية", key="back_home_1"): 
        change_page('home')
    
    st.header("📅 جدول مباريات اليوم")
    st.info("🔄 جاري سحب البيانات المباشرة من الروابط...")

    try:
        url = "https://www.livescore.cz/"
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # هنا نعرض البيانات بشكل مبسط
        st.success("✅ تم الاتصال بمصدر البيانات")
        st.write("سيتم عرض قائمة المباريات المسحوبة هنا:")
        # ملاحظة: استخراج البيانات يعتمد على بنية الموقع المختار
    except:
        st.error("تعذر جلب البيانات، تأكد من ملف requirements.txt")

# --- صفحة المباشر ---
elif st.session_state.page == 'live':
    if st.button("⬅️ العودة للرئيسية", key="back_home_2"): 
        change_page('home')
    st.header("🔴 التحليل الذكي المباشر")
    st.warning("🧠 خوارزمية AI: جاري تحليل الضغط والاستحواذ للمباريات الجارية...")

# --- صفحة الإحصائيات ---
elif st.session_state.page == 'stats':
    if st.button("⬅️ العودة للرئيسية", key="back_home_3"): 
        change_page('home')
    st.header("📊 ركن الخوارزميات")
    st.write("إحصائيات متقدمة وتوقعات النتائج تظهر هنا.")
