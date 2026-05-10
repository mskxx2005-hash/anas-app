import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="AI Football Center", layout="wide")

# --- إدارة التنقل (Navigation Logic) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def change_page(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية (Home Page) ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚽ مرحبا بكم في كرة القدم</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # الكروت المتسلسلة (بدون الإعدادات)
    # الكارت الأول: مباريات اليوم
    st.markdown("""
    <div style='border: 2px solid #28a745; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 10px;'>
        <h2 style='margin:0;'>📅 مباريات اليوم</h2>
        <p style='color: #666;'>جدول كامل بجميع مباريات اليوم في الدوريات الكبرى</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("فتح قسم مباريات اليوم", use_container_width=True):
        change_page('matches')

    # الكارت الثاني: مباشر + تحليل
    st.markdown("""
    <div style='border: 2px solid #dc3545; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 10px;'>
        <h2 style='margin:0;'>🔴 AI مباشر + تحليل</h2>
        <p style='color: #666;'>تغطية حية مع خوارزميات ذكية لتحليل الأداء فوراً</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("الدخول للبث والتحليل", use_container_width=True):
        change_page('live')

    # الكارت الثالث: الخوارزميات
    st.markdown("""
    <div style='border: 2px solid #007bff; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 10px;'>
        <h2 style='margin:0;'>📊 الخوارزميات الذكية</h2>
        <p style='color: #666;'>تحليل الأرقام، الاستحواذ، وتوقعات النتائج</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("استعراض الإحصائيات", use_container_width=True):
        change_page('stats')

    # إضافة يوزر الانستا في الأسفل
    st.write("---")
    st.markdown("<p style='text-align: center; color: #E1306C;'>📸 Instagram: <b>06cb4</b></p>", unsafe_allow_html=True)

# --- صفحات المحتوى (تظهر فقط عند الدخول إليها) ---

elif st.session_state.page == 'matches':
    if st.button("⬅️ العودة للرئيسية"): change_page('home')
    st.header("📅 جدول مباريات اليوم")
    st.info("سيتم عرض قائمة المباريات هنا فور ربط البيانات...")

elif st.session_state.page == 'live':
    if st.button("⬅️ العودة للرئيسية"): change_page('home')
    st.header("🔴 البث المباشر والتحليل الخوارزمي")
    st.warning("🤖 جاري تشغيل الخوارزميات لتحليل أحداث المباراة...")

elif st.session_state.page == 'stats':
    if st.button("⬅️ العودة للرئيسية"): change_page('home')
    st.header("📊 ركن الخوارزميات المتقدمة")
    st.write("هنا تظهر إحصائيات الاستحواذ والضغط العالي.")
import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_live_data_from_link():
    # هذا الرابط كمثال لموقع يعطي نتائج مباشرة
    url = "https://www.livescore.cz/" 
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        matches_list = []
        
        # هنا الكود يدور على جدول المباريات بداخل الرابط
        # ملاحظة: تقسيمات الـ HTML تختلف من موقع لثاني
        table = soup.find('table', class_='match-table')
        
        if table:
            rows = table.find_all('tr')
            for row in rows[:10]: # ناخذ أول 10 مباريات
                teams = row.find_all('td', class_='team')
                score = row.find('td', class_='score')
                
                if teams and score:
                    matches_list.append({
                        "match": f"{teams[0].text} vs {teams[1].text}",
                        "score": score.text
                    })
        return matches_list
    except:
        return [{"match": "خطأ في سحب البيانات من الرابط", "score": "-"}]

# طريقة العرض في خانة "مباريات اليوم"
st.header("📊 بيانات حقيقية مسحوبة من المواقع")

if st.button("تحديث البيانات من الروابط"):
    results = get_live_data_from_link()
    for res in results:
        st.write(f"⚽ {res['match']} | النتيجة: {res['score']}")
