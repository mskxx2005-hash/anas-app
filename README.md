import streamlit as st

st.set_page_config(page_title="منصة أنس الرياضية", page_icon="⚽", layout="wide")

with st.sidebar:
    st.title("القائمة الرئيسية")
    st.info("Instagram: 06cb4")
    st.write("---")
    choice = st.radio("انتقل إلى:", ["الرئيسية", "تحليل المباريات"])

if choice == "الرئيسية":
    st.title("🏟️ منصة المحلل أنس (06cb4)")
    st.header("أهلاً بك في موقعي الخاص يا بطل")
    st.balloons()

elif choice == "تحليل المباريات":
    st.title("⚽ قسم التحليل الذكي")
    match = st.text_input("اكتب المباراة:")
    if st.button("بدء التحليل"):
        st.success(f"جاري تحليل {match}...")

hide_style = """<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>"""
st.markdown(hide_style, unsafe_allow_html=True)
