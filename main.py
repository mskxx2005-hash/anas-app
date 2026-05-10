import streamlit as st

st.set_page_config(page_title="محلل أنس الرياضي", page_icon="⚽")

st.title("🏟️ منصة المحلل أنس لتحليل المباريات")
st.markdown("---")

# خانة إدخال المباراة
st.subheader("🏁 حلل مباراتك القادمة")
match = st.text_input("اكتب المباراة (مثلاً: ريال مدريد - مانشستر سيتي):")

if st.button("بدء التحليل الذكي"):
    if match:
        st.write(f"🔍 جاري سحب البيانات لمباراة: **{match}**...")
        st.info("توقع أنس: المباراة ستكون هجومية، ونسبة الفوز للأرض 45%")
        st.balloons()
    else:
        st.warning("يا بطل، اكتب اسم المباراة أولاً!")

st.sidebar.header("📊 إحصائيات الدوريات")
st.sidebar.write("الدوري الإنجليزي - متصدر")
st.sidebar.write("الدوري الإسباني - متصدر")

st.success("✅ الموقع شغال وجاهز يا أنس البطل!")
