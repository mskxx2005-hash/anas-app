import streamlit as st

# إعداد الصفحة لتكون عريضة وبشكل احترافي
st.set_page_config(page_title="منصة أنس الرياضية", page_icon="⚽", layout="wide")

# القائمة الجانبية (Sidebar) مثل اللي بالصور
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1165/1165187.png", width=100)
    st.title("القائمة الرئيسية")
    st.markdown(f"👤 **المطور: أنس**")
    st.info("Instagram: **06cb4**")
    st.write("---")
    
    # اختيار الأقسام
    choice = st.radio("انتقل إلى:", ["الرئيسية", "تحليل المباريات", "جدول الترتيب", "مركز النتائج المباشرة"])
    st.write("---")
    st.success("الموقع شغال 100%")

# محتوى الصفحة بناءً على الاختيار
if choice == "الرئيسية":
    st.title("🏟️ أهلاً بك في منصة أنس للتحليل")
    st.header(f"مرحباً بك يا بطل! تابع يوزري: 06cb4")
    st.markdown("""
    هذا الموقع مخصص لعشاق كرة القدم والتحليل الإحصائي. 
    استخدم القائمة الجانبية للتنقل بين أقسام الموقع بكل سهولة.
    """)
    st.balloons()

elif choice == "تحليل المباريات":
    st.title("⚽ قسم التحليل الذكي")
    match_name = st.text_input("أدخل المباراة المراد تحليلها (مثلاً: الكلاسيكو):")
    if st.button("بدء التحليل"):
        st.write(f"🔍 جاري تحليل مباراة **{match_name}** بالاعتماد على إحصائيات الموسم...")
        st.info("التوقع: مباراة مغلقة وتكتيكية عالية.")

elif choice == "جدول الترتيب":
    st.title("📊 جداول ترتيب الدوريات")
    st.write("قريباً سيتم ربط الموقع ببيانات حية للدوريات الكبرى.")

elif choice == "مركز النتائج المباشرة":
    st.title("⏱️ نتائج حية")
    st.write("هنا ستظهر النتائج فور حدوثها.")

# إخفاء العلامات الافتراضية ليكون الموقع نظيف
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
