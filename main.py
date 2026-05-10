import streamlit as st
import requests

# إعدادات واجهة موقع خوارزميات
st.set_page_config(page_title="موقع خوارزميات", page_icon="⚽", layout="wide")
st.title("⚽ موقع خوارزميات - البث المباشر والتحليل")
st.markdown("---")

# المفتاح السري مالتك
API_KEY = "170d93f214msh2b139c9f91f8f55p1c9f1fjsn974e38b403a0"

def get_analysis(home, away, home_score, away_score):
    # خوارزمية تحليل ذكية بسيطة بناءً على النتيجة
    if home_score == away_score:
        return f"الخوارزمية: مباراة متكافئة جداً بين {home} و {away}، الحذر الدفاعي سيد الموقف."
    elif int(home_score) > int(away_score):
        return f"الخوارزمية: {home} يفرض أسلوبه هجومياً، ثغرات واضحة في دفاعات {away}."
    else:
        return f"الخوارزمية: {away} متفوق تكتيكياً ويستغل الفرص بشكل مثالي أمام مرمى {home}."

# جلب البيانات من السيرفر
url = "https://free-api-live-football-data.p.rapidapi.com/football-fixtures-live"
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

try:
    with st.spinner('جارِ تحديث المباريات المباشرة والتحليل...'):
        response = requests.get(url, headers=headers)
        data = response.json()

    if data.get('status') == 'success' and 'data' in data:
        st.header("🔴 المباريات المباشرة الآن")
        
        # عرض كل مباراة في بطاقة (Card) مرتبة
        for match in data['data']:
            home = match['home_team']['name']
            away = match['away_team']['name']
            h_score = match['home_score']
            a_score = match['away_score']
            minute = match.get('minute', '--')

            with st.container():
                col1, col2, col3 = st.columns([2, 1, 2])
                with col1:
                    st.subheader(home)
                with col2:
                    st.title(f"{h_score} - {a_score}")
                    st.write(f"⏱ الدقيقة: {minute}")
                with col3:
                    st.subheader(away)
                
                # إضافة التحليل الخوارزمي لكل مباراة
                st.info(get_analysis(home, away, h_score, a_score))
                st.markdown("---")
    else:
        st.warning("حالياً لا توجد مباريات مباشرة مسجلة في السيرفر.")

except:
    st.error("عذراً، واجهنا مشكلة في جلب البيانات المباشرة. جرب تحديث الصفحة.")

st.sidebar.markdown("### عن خوارزميات")
st.sidebar.info("هذا الموقع يحلل البيانات المباشرة باستخدام ذكاء اصطناعي بسيط ليعطيك أفضل رؤية للمباراة.")
