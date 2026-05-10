import streamlit as st
import requests
import pandas as pd

# إعداد الصفحة لتكون عريضة واحترافية
st.set_page_config(page_title="منصة أنس الرياضية", page_icon="⚽", layout="wide")

# الكود (المفتاح) الخاص بك الذي أرسلته
API_KEY = "4f74f8c769e012d50f70c0fe7e344070"

# تصميم القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("🥇 محلل أنس الذكي")
    st.info("Instagram: 06cb4")
    st.write("---")
    menu = st.radio("اختار القسم:", ["الرئيسية", "مباريات مباشرة 🔴", "ترتيب الدوريات"])

# محتوى الصفحة بناءً على الاختيار
if menu == "الرئيسية":
    st.title("🏟️ أهلاً بك في منصة أنس للتحليل")
    st.header(f"المحلل أنس (06cb4) يرحب بكم")
    st.success("الموقع الآن مربوط ببيانات حية ومباشرة (API Active)")
    st.balloons()

elif menu == "مباريات مباشرة 🔴":
    st.title("⏱️ نتائج المباريات الجارية الآن")
    
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data['response']:
            for match in data['response']:
                home = match['teams']['home']['name']
                away = match['teams']['away']['name']
                league = match['league']['name']
                score_home = match['goals']['home']
                score_away = match['goals']['away']
                time = match['fixture']['status']['elapsed']
                
                # عرض المباراة بشكل مرتب
                st.info(f"🏆 {league} | الدقيقة: {time}'")
                st.subheader(f"{home}  {score_home} - {score_away}  {away}")
                st.write("---")
        else:
            st.warning("لا توجد مباريات مباشرة في هذه اللحظة. شيك وقت المباريات!")
    except:
        st.error("أكو مشكلة بالاتصال بالبيانات، تأكد من أن الـ API Key فعال.")

elif menu == "ترتيب الدوريات":
    st.title("📊 جداول الترتيب")
    st.write("قريباً سيتم إضافة جداول جميع الدوريات الكبرى هنا.")

# كود لإخفاء علامات شركة Streamlit ليظهر الموقع كأنه تطبيق خاص بك
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
