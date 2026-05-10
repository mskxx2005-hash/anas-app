import streamlit as st

st.set_page_config(page_title="منصة أنس الرياضية", page_icon="⚽", layout="wide")

# القائمة الجانبية (Sidebar) مثل الصور اللي ردتها
with st.sidebar:
    st.title("القائمة الرئيسية")
    st.info("Instagram: 06cb4")
    st.write("---")
    choice = st.radio("انتقل إلى:", ["الرئيسية", "تحليل المباريات", "النتائج المباشرة"])

# محتوى الصفحة
if choice == "الرئيسية":
    st.title("🏟️ منصة المحلل أنس (06cb4)")
    st.header("أهلاً بك في موقعي الخاص")
    st.balloons()

elif choice == "تحليل المباريات":
    st.title("⚽ تحليل المباريات الذكي")
    match = st.text_input("اكتب المباراة لتحليلها:")
    if st.button("ابدأ التحليل"):
        st.success(f"جاري تحليل {match}.. انتظر النتائج يا بطل")

# كود لإخفاء الإعلانات والخرابيط
hide_st_style = """<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
