import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="لوحة تحكم كرة القدم", layout="wide")

# الترحيب
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚽ مرحبا بكم في كرة القدم</h1>", unsafe_allow_html=True)
st.write("---")

# --- تصميم المربعات (Dashboard Tiles) ---

# السطر الأول من المربعات
col1, col2 = st.columns(2)

with col1:
    # المربع الأول: مباريات اليوم
    st.markdown("""
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 15px; border: 2px solid #4CAF50; text-align: center;">
        <h2 style="color: white;">📅 مباريات اليوم</h2>
        <p style="color: #bbb;">جدول كامل بجميع مباريات اليوم في الدوريات الكبرى</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("فتح قسم مباريات اليوم", use_container_width=True):
        st.info("🏴󠁧󠁢󠁥󠁮󠁧󠁿 ليفربول vs سيتي | 🇪🇸 ريال مدريد vs أتلتيكو")

with col2:
    # المربع الثاني: بث مباشر وتحليل
    st.markdown("""
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 15px; border: 2px solid #ff4b4b; text-align: center;">
        <h2 style="color: white;">🔴 مباشر + تحليل AI</h2>
        <p style="color: #bbb;">تغطية حية مع خوارزميات ذكية لتحليل الأداء فوراً</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("الدخول للبث والتحليل", use_container_width=True):
        st.warning("🤖 الخوارزمية: ضغط عالي في مباراة بايرن الآن!")

st.write(" ") # مسافة بين السطور

# السطر الثاني من المربعات
col3, col4 = st.columns(2)

with col3:
    # المربع الثالث: إحصائيات وخوارزميات
    st.markdown("""
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 15px; border: 2px solid #00c0f2; text-align: center;">
        <h2 style="color: white;">📊 الخوارزميات الذكية</h2>
        <p style="color: #bbb;">تحليل الأرقام، الاستحواذ، وتوقعات النتائج</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("استعراض الإحصائيات", use_container_width=True):
        st.write("📈 نسبة دقة التوقعات اليوم: 88%")

with col4:
    # المربع الرابع: الإعدادات والـ API
    st.markdown("""
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 15px; border: 2px solid #f0ad4e; text-align: center;">
        <h2 style="color: white;">⚙️ الإعدادات</h2>
        <p style="color: #bbb;">تحكم بمفاتيح الـ API وإعدادات الموقع الخاص بك</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("ضبط الإعدادات", use_container_width=True):
        st.success("المفتاح الحالي فعال ✅")
