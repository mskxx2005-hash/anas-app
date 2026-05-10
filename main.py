import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="محلل أنس المجاني", page_icon="⚽", layout="wide")

# تصميم الـ Sidebar (مثل ما ردت)
with st.sidebar:
    st.title("🥇 منصة أنس الذكية")
    st.info("Instagram: 06cb4")
    st.write("---")
    menu = st.radio("القائمة:", ["الرئيسية", "نتائج حية (مجانية)", "تحليل أنس الخاص"])

# محتوى الصفحة
if menu == "الرئيسية":
    st.title("🏟️ أهلاً بك في عالم التحليل المجاني")
    st.header(f"المحلل أنس (06cb4) يرحب بكم")
    st.success("هذا الموقع يعمل ببيانات مجانية 100%")
    st.balloons()

elif menu == "نتائج حية (مجانية)":
    st.title("⏱️ نتائج المباريات اليوم")
    # هنا بيانات تجريبية مرتبة كأنها جاية من API
    data = {
        'المباراة': ['ريال مدريد vs برشلونة', 'مان سيتي vs ارسنال', 'ليفربول vs تشيلسي'],
        'الحالة': ['مباشر', 'قريباً', 'انتهت'],
        'النتيجة': ['2 - 1', '0 - 0', '3 - 2']
    }
    df = pd.DataFrame(data)
    st.table(df) # تطلع بشكل جدول مرتب مثل المواقع الكبيرة

elif menu == "تحليل أنس الخاص":
    st.title("🧠 قسم التوقعات الذكي")
    match = st.text_input("اكتب المباراة للتوقع:")
    if st.button("اعطني التوقع"):
        st.warning(f"تحليل أنس لـ {match}: نسبة الفوز 60% لصاحب الأرض، وتوقع أهداف غزيرة!")

# إخفاء إعلانات الشركة
hide_st_style = """<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
