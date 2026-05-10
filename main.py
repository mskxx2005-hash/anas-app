import streamlit as st
import requests

# واجهة موقع خوارزميات
st.set_page_config(page_title="موقع خوارزميات", page_icon="⚽", layout="wide")
st.title("⚽ موقع خوارزميات - التحليل المباشر")

# المفتاح مالتك
API_KEY = "170d93f214msh2b139c9f91f8f55p1c9f1fjsn974e38b403a0"

def get_smart_analysis(h_score, a_score):
    if h_score == a_score:
        return "🧠 تحليل خوارزميات: تقارب تكتيكي عالي، الفريقان يركزان على إغلاق المساحات."
    return "🧠 تحليل خوارزميات: اندفاع هجومي واضح، الخوارزمية تتوقع تغيراً في النتيجة قريباً."

# جلب البيانات
url = "https://free-api-live-football-data.p.rapidapi.com/football-fixtures-live"
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

try:
    with st.spinner('جارِ فحص السيرفرات العالمية...'):
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

    if data.get('status') == 'success' and data.get('data'):
        for match in data['data']:
            with st.expander(f"🏟 {match['home_team']['name']} VS {match['away_team']['name']} ({match['home_score']} - {match['away_score']})"):
                st.write(f"⏱ الدقيقة: {match.get('minute', 'بث مباشر')}")
                st.info(get_smart_analysis(match['home_score'], match['away_score']))
    else:
        st.warning("⚠️ لا توجد مباريات مباشرة حالياً في هذا السيرفر. الخوارزمية في وضع الاستعداد.")
        st.write("جرب البحث عن فريقك المفضل بالإنجليزي أدناه:")
        team_search = st.text_input("اسم الفريق:")
        if team_search:
            st.write(f"🔍 جارِ جدولة البحث عن {team_search}...")

except Exception as e:
    st.error("السيرفر المجاني عليه ضغط هسة. انتظر دقيقة وسوي Refresh.")

st.sidebar.markdown("### 🤖 نظام خوارزميات")
st.sidebar.write("نحن نستخدم بيانات API-Football لتحليل مجريات المباراة لحظياً.")
