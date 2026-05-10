import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="AI Football Center", layout="wide")

# --- إدارة التنقل (Navigation Logic) ---
# إذا كانت هذه أول مرة يفتح فيها الموقع، اجعل الصفحة الرئيسية هي الافتراضية
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# وظيفة لتغيير الصفحة
def change_page(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية (Home Page) ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚽ مرحبا بكم في كرة القدم</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # توزيع الكروت بشكل مربعات (مثل صورتك)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='border: 2px solid green; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2>📅 مباريات اليوم</h2>
            <p>جدول كامل بجميع مباريات اليوم في الدوريات الكبرى</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("فتح قسم مباريات اليوم", use_container_width=True):
            change_page('matches')

    with col2:
        st.markdown("""
        <div style='border: 2px solid red; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2>🔴 AI مباشر + تحليل</h2>
            <p>تغطية حية مع خوارزميات ذكية لتحليل الأداء فوراً</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("الدخول للبث والتحليل", use_container_width=True):
            change_page('live')

    st.write(" ") # مسافة
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div style='border: 2px solid blue; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2>📊 الخوارزميات الذكية</h2>
            <p>تحليل الأرقام، الاستحواذ، وتوقعات النتائج</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("استعراض الإحصائيات", use_container_width=True):
            change_page('stats')

    with col4:
        st.markdown("""
        <div style='border: 2px solid orange; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2>⚙️ الإعدادات</h2>
            <p>ضبط مفاتيح الـ API وإعدادات الموقع</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("ضبط الإعدادات", use_container_width=True):
            change_page('settings')

# --- صفحة مباريات اليوم ---
elif st.session_state.page == 'matches':
    if st.button("⬅️ العودة للرئيسية"): change_page('home')
    st.header("📅 جدول مباريات اليوم")
    st.info("هنا تظهر قائمة المباريات القادمة...")
    # هنا نحط كود جلب بيانات المباريات لاحقاً

# --- صفحة المباشر والتحليل ---
elif st.session_state.page == 'live':
    if st.button("⬅️ العودة للرئيسية"): change_page('home')
    st.header("🔴 البث المباشر والتحليل الخوارزمي")
    st.warning("🤖 خوارزمية AI: جاري تحليل أحداث المباراة الحالية...")
    # تصميم واجهة المباشر اللي سويناها قبل شوية

# --- صفحة الإحصائيات ---
elif st.session_state.page == 'stats':
    if st.button("⬅️ العودة للرئيسية"): change_page('home')
    st.header("📊 ركن الخوارزميات المتقدمة")
    st.write("إحصائيات الاستحواذ والضغط العالي تظهر هنا.")

# --- صفحة الإعدادات ---
elif st.session_state.page == 'settings':
    if st.button("⬅️ العودة للرئيسية"): change_page('home')
    st.header("⚙️ الإعدادات")
    st.text_input("أدخل مفتاح API الخاص بك:", value="4f74f8c769e012d50f70c0fe7e344070")
