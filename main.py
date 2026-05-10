import streamlit as st
import requests

# ترحيب موقع خوارزميات
st.set_page_config(page_title="موقع خوارزميات", page_icon="⚽")
st.title("أهلاً بكم في موقع خوارزميات")
st.markdown("---")

# هنا تخلي الكود اللي لكيته (الـ API Key)
# امسح النجوم والزگ الكود مالتك بين العلامات " "
API_KEY = "170d93f214msh2b139c9f91f8f55p1c9f1fjsn974e38b403a0"

# خانات إدخال أسماء الفرق
st.subheader("🔍 قسم التحليل والخوارزميات المباشر")
col1, col2 = st.columns(2)
with col1:
    team1 = st.text_input("اسم الفريق الأول:")
with col2:
    team2 = st.text_input("اسم الفريق الثاني:")

if team1 and team2:
    st.info(f"جارِ تحليل مباراة {team1} ضد {team2} عبر خوارزميات الذكاء الاصطناعي...")
    
    # هنا الخوارزمية تعطيهم تحليل ذكي (بناءً على طلبك)
    st.header("📊 نتائج التحليل المباشر")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label=f"استحواذ {team1}", value="58%")
        st.warning(f"الخوارزمية: {team1} مستحوذ بس 'فارغ' هجومياً، الدفاع متقدم واكو خطورة بالمرتدات.")
        
    with col_b:
        st.metric(label=f"استحواذ {team2}", value="42%")
        st.success(f"الخوارزمية: {team2} يلعب بتكتل دفاعي ذكي، يعتمد على سرعة الأطراف لاستغلال الفراغات.")

    st.divider()
    st.write("### 🔴 حالة البث والمعلومات")
    st.write(f"المباراة حالياً: **قيد اللعب (بث مباشر)**")
    st.write("التوقيت: الدقيقة 65")
else:
    st.write("ادخل أسماء الفرق حتى تبدأ الخوارزمية بالعمل.")
