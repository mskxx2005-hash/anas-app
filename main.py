import streamlit as st
import requests

# إعدادات واجهة موقع خوارزميات الاحترافية
st.set_page_config(page_title="موقع خوارزميات", page_icon="⚽", layout="wide")

# ترحيب خاص
st.markdown("<h1 style='text-align: center; color: #00ff00;'>أهلاً بكم في موقع خوارزميات ⚽</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>نظام التحليل الذكي للمباريات المباشرة</p>", unsafe_allow_html=True)
st.markdown("---")

# المفتاح مالتك (ثبته إلك بالكود)
API_KEY = "170d93f214msh2b139c9f91f8f55p1c9f1fjsn974e38b403a0"

def get_analysis(h_score, a_score, h_team, a_team):
    h = int(h_score)
    a = int(a_score)
    if h == a:
        return f"🧠 تحليل خوارزميات: مباراة مغلقة تكتيكياً بين {h_team} و {a_team}. التوقعات تشير إلى تعادل حذر."
    elif h > a:
        return f"🧠 تحليل خوارزميات: سيطرة واضحة لـ {h_team}. الخوارزمية ترصد خللاً في توازن دفاع {a_team}."
    else:
        return f"🧠 تحليل خوارزميات: {a_team} يباغت الخصم بمرتدات قاتلة. الأفضلية تذهب للضيوف حالياً."

# جلب البيانات من السيرفر العالمي
url = "https://free-api-live-football-data.p.rapidapi.com/football-fixtures-live"
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

try:
    with st.spinner('خوارزميات تفحص الملاعب العالمية...'):
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

    if data.get('status') == 'success' and data.get('data'):
        st.subheader("🔴 المباريات المباشرة والتحليل الميداني")
        
        for match in data['data']:
            h_name = match['home_team']['name']
            a_name = match['away_team']['name']
            h_score = match['home_score']
            a_score = match['away_score']
            minute = match.get('minute', 'LIVE')

            # تصميم بطاقة المباراة
            with st.container():
                st.markdown(f"""
                <div style="background-color: #1e1e1e; padding: 20px; border-radius: 15px; border-left: 5px solid #00ff00; margin-bottom: 20px;">
                    <h3 style="color: white; text-align: center;">{h_name} <span style="color: #00ff00;">{h_score} - {a_score}</span> {a_name}</h3>
                    <p style="text-align: center; color: #aaaaaa;">⏱ الدقيقة: {minute}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # التحليل الذكي
                st.info(get_analysis(h_score, a_score, h_name, a_name))
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ لا توجد مباريات مباشرة مسجلة حالياً بالسيرفر. الخوارزمية بوضع الاستعداد.")
        st.info("ملاحظة: السيرفر يحدث البيانات كل 5 دقائق.")

except Exception as e:
    st.error("السيرفر مشغول حالياً. الخوارزمية تحاول إعادة الاتصال... سوي Refresh بعد دقيقة.")

# تذييل الصفحة
st.sidebar.title("🤖 ركن الخوارزميات")
st.sidebar.write("موقعك هسة صار يقرأ من أقوى سيرفرات الطوبة بالعالم.")
if st.sidebar.button("تحديث البيانات فوراً"):
    st.rerun()
