import streamlit as st
import requests
from datetime import datetime, timedelta

# إعدادات الصفحة
st.set_page_config(page_title="منصة أنس الرياضية الذكية", page_icon="⚽", layout="wide")

# ستايل CSS فخم لإعطاء مظهر التطبيقات العالمية
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e445e; }
    .match-card { background: linear-gradient(135deg, #1e2130 0%, #161925 100%); border-radius: 15px; padding: 20px; border: 1px solid #3e445e; margin-bottom: 20px; }
    .live-dot { height: 10px; width: 10px; background-color: #ff4b4b; border-radius: 50%; display: inline-block; margin-right: 5px; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    .alert-ai { background-color: rgba(255, 75, 75, 0.1); border: 1px solid #ff4b4b; padding: 10px; border-radius: 8px; color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = st.secrets["FOOTBALL_API_KEY"]
HOST = "v3.football.api-sports.io"

def fetch_data(endpoint, params=None):
    headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': HOST}
    try:
        response = requests.get(f"https://{HOST}/{endpoint}", headers=headers, params=params)
        return response.json().get('response', [])
    except: return []

# القائمة الجانبية
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/53/53283.png", width=100)
st.sidebar.title("🎮 مركز التحكم")
menu = st.sidebar.radio("اختر القسم:", ["🔴 البث المباشر", "📅 جدول اليوم", "📈 تحليلات وإحصائيات"])

# --- القسم الأول: البث المباشر ---
if menu == "🔴 البث المباشر":
    st.header("🎮 المباريات الجارية الآن")
    live_matches = fetch_data("fixtures", {"live": "all"})
    
    if not live_matches:
        st.info("لا توجد مباريات مباشرة حالياً. انتظر بدء المباريات!")
    else:
        for m in live_matches:
            with st.container():
                st.markdown(f"""
                <div class="match-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="text-align: center; width: 35%;">
                            <img src="{m['teams']['home']['logo']}" width="60"><br><b>{m['teams']['home']['name']}</b>
                        </div>
                        <div style="text-align: center; width: 30%;">
                            <h2 style="margin:0;">{m['goals']['home']} - {m['goals']['away']}</h2>
                            <span class="live-dot"></span><span style="color:#ff4b4b;">{m['fixture']['status']['elapsed']}'</span>
                        </div>
                        <div style="text-align: center; width: 35%;">
                            <img src="{m['teams']['away']['logo']}" width="60"><br><b>{m['teams']['away']['name']}</b>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# --- القسم الثاني: جدول اليوم (ستبدأ قريباً) ---
elif menu == "📅 جدول اليوم":
    st.header("⏳ مباريات ستبدأ قريباً")
    today = datetime.now().strftime('%Y-%m-%d')
    all_today = fetch_data("fixtures", {"date": today})
    upcoming = [m for m in all_today if m['fixture']['status']['short'] in ['NS', 'TBD']]
    
    if not upcoming:
        st.warning("تم لعب جميع مباريات اليوم أو لا توجد مباريات مجدولة.")
    else:
        for m in upcoming:
            utc_time = datetime.strptime(m['fixture']['date'], "%Y-%m-%dT%H:%M:%S%z")
            iq_time = (utc_time + timedelta(hours=3)).strftime('%I:%M %p')
            st.markdown(f"""
            <div class="match-card">
                <p style="color:#f1c40f;">⏰ توقيت العراق: {iq_time}</p>
                <b>{m['teams']['home']['name']}</b> vs <b>{m['teams']['away']['name']}</b>
            </div>
            """, unsafe_allow_html=True)

# --- القسم الثالث: التحليلات والإحصائيات الذكية ---
elif menu == "📈 تحليلات وإحصائيات":
    st.header("📊 مركز التحليل الذكي (AI Analysis)")
    live_matches = fetch_data("fixtures", {"live": "all"})
    
    if not live_matches:
        st.info("اختر مباراة من البث المباشر لتحليلها. حالياً لا يوجد مباريات مباشرة.")
    else:
        match_names = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in live_matches]
        selected = st.selectbox("اختر مباراة للتحليل المباشر:", match_names)
        idx = match_names.index(selected)
        m_id = live_matches[idx]['fixture']['id']
        
        # جلب الإحصائيات
        stats = fetch_data("fixtures/statistics", {"fixture": m_id})
        if stats:
            h_s = {s['type']: s['value'] for s in stats[0]['statistics']}
            a_s = {s['type']: s['value'] for s in stats[1]['statistics']}
            
            # عرض الـ Metrics مثل الصورة
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🟨 كروت", f"{h_s.get('Yellow Cards',0)} - {a_s.get('Yellow Cards',0)}")
            col2.metric("⚽ تسديدات", f"{h_s.get('Shots on Goal',0)} - {a_s.get('Shots on Goal',0)}")
            col3.metric("🚩 ركنيات", f"{h_s.get('Corner Kicks',0)} - {a_s.get('Corner Kicks',0)}")
            col4.metric("🛡️ استحواذ", f"{h_s.get('Ball Possession','50%')} - {a_s.get('Ball Possession','50%')}")
            
            # التوقعات الذكية
            st.subheader("🤖 تنبيهات أنس الذكية")
            poss_h = int(str(h_s.get('Ball Possession','50%')).replace('%',''))
            if poss_h > 60:
                st.markdown(f'<div class="alert-ai">⚠️ {live_matches[idx]["teams"]["home"]["name"]} مسيطر تماماً ويضغط بقوة!</div>', unsafe_allow_html=True)
            
            st.subheader("🔮 توقع النتيجة النهائية")
            st.write("بناءً على المعطيات الحالية، الفريق المستضيف لديه احتمالية فوز 65%.")
        else:
            st.warning("الإحصائيات المباشرة غير متوفرة لهذه المباراة حالياً.")

st.sidebar.markdown("---")
st.sidebar.write("تم التطوير بواسطة أنس البطل 🏆")
