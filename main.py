import streamlit as st
import requests
from datetime import datetime, timedelta

# 🎨 إعدادات الثيم الفخم (Dark Mode)
st.set_page_config(page_title="Anas Live Center", page_icon="⚽", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stat-card { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; text-align: center; margin-bottom: 10px; }
    .ai-alert-danger { background-color: rgba(231, 76, 60, 0.1); border-left: 5px solid #e74c3c; padding: 10px; border-radius: 5px; color: #ff6b6b; margin-top: 10px; }
    .ai-alert-success { background-color: rgba(46, 204, 113, 0.1); border-left: 5px solid #2ecc71; padding: 10px; border-radius: 5px; color: #2ecc71; margin-top: 10px; }
    .ai-alert-warning { background-color: rgba(241, 196, 15, 0.1); border-left: 5px solid #f1c40f; padding: 10px; border-radius: 5px; color: #f1c40f; margin-top: 10px; }
    .team-header { font-size: 24px; font-weight: bold; color: #ffffff; }
    .score-big { font-size: 40px; font-weight: bold; color: #ffffff; margin: 0 20px; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = st.secrets["FOOTBALL_API_KEY"]
HOST = "v3.football.api-sports.io"

def get_api_data(endpoint, params=None):
    headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': HOST}
    try:
        r = requests.get(f"https://{HOST}/{endpoint}", headers=headers, params=params)
        return r.json().get('response', [])
    except: return []

# --- القائمة الجانبية ---
st.sidebar.title("🛠️ لوحة التحكم")
page = st.sidebar.radio("انتقل إلى:", ["Live Center ⚽", "Today's Fixtures 📅", "Standings 🏆"])

if page == "Live Center ⚽":
    st.title("🏟️ Live Center")
    live_matches = get_api_data("fixtures", {"live": "all"})
    
    if not live_matches:
        st.info("لا توجد مباريات مباشرة الآن. انتظر وقت المباريات لترى التحليل الذكي!")
        # تجربة عرض (Demo) حتى تشوف الشكل
        st.write("---")
        st.subheader("👀 مثال لما سيظهر وقت المباراة:")
        col_t1, col_sc, col_t2 = st.columns([2,1,2])
        col_t1.markdown('<div style="text-align:right;" class="team-header">فريق أ</div>', unsafe_allow_html=True)
        col_sc.markdown('<div style="text-align:center;" class="score-big">2 - 1</div>', unsafe_allow_html=True)
        col_t2.markdown('<div style="text-align:left;" class="team-header">فريق ب</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ai-alert-warning">⚡ <b>AI Smart Alert:</b> فريق أ مسيطر على الكرة بنسبة 70% لكن تسديداته بعيدة عن المرمى!</div>', unsafe_allow_html=True)
    else:
        for m in live_matches:
            with st.expander(f"➔ {m['teams']['home']['name']} {m['goals']['home']} - {m['goals']['away']} {m['teams']['away']['name']}", expanded=True):
                # عرض الإحصائيات مثل صورة Replit
                stats = get_api_data("fixtures/statistics", {"fixture": m['fixture']['id']})
                if stats:
                    h_s = {s['type']: s['value'] for s in stats[0]['statistics']}
                    a_s = {s['type']: s['value'] for s in stats[1]['statistics']}
                    
                    c1, c2, c3, c4 = st.columns(4)
                    with c1: st.markdown(f'<div class="stat-card">🟡 كروت<br><b>{h_s.get("Yellow Cards",0)} - {a_s.get("Yellow Cards",0)}</b></div>', unsafe_allow_html=True)
                    with c2: st.markdown(f'<div class="stat-card">⚽ تسديدات<br><b>{h_s.get("Shots on Goal",0)} - {a_s.get("Shots on Goal",0)}</b></div>', unsafe_allow_html=True)
                    with c3: st.markdown(f'<div class="stat-card">🚩 ركنيات<br><b>{h_s.get("Corner Kicks",0)} - {a_s.get("Corner Kicks",0)}</b></div>', unsafe_allow_html=True)
                    with c4: st.markdown(f'<div class="stat-card">🛡️ أخطاء<br><b>{h_s.get("Fouls",0)} - {a_s.get("Fouls",0)}</b></div>', unsafe_allow_html=True)
                    
                    # 🧠 التحليل الذكي (الذكاء الاصطناعي مالتك)
                    st.subheader("🤖 AI Smart Alerts")
                    pos_h = int(str(h_s.get("Ball Possession", "50%")).replace('%',''))
                    shots_h = h_s.get("Shots total", 0) or 0
                    
                    if pos_h > 60 and h_s.get("Shots on Goal", 0) <= 1:
                        st.markdown(f'<div class="ai-alert-warning">⚠️ {m["teams"]["home"]["name"]} يستحوذ كثيراً ({pos_h}%) لكنه يعاني في اختراق الدفاع!</div>', unsafe_allow_html=True)
                    if a_s.get("Shots total", 0) > 10:
                        st.markdown(f'<div class="ai-alert-danger">🔥 {m["teams"]["away"]["name"]} خطر جداً بالمرتدات.. تسديدات مكثفة!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="ai-alert-success">✅ المباراة متوازنة تكتيكياً حتى الآن.</div>', unsafe_allow_html=True)

elif page == "Today's Fixtures 📅":
    st.title("📅 Today's Fixtures")
    today = datetime.now().strftime('%Y-%m-%d')
    fixtures = get_api_data("fixtures", {"date": today})
    if fixtures:
        for f in fixtures[:10]:
            st.write(f"⏰ {f['teams']['home']['name']} vs {f['teams']['away']['name']}")
    else:
        st.info("No fixtures scheduled for today.")

st.sidebar.markdown("---")
st.sidebar.write(f"🕒 توقيت العراق: {(datetime.now() + timedelta(hours=3)).strftime('%H:%M')}")
st.sidebar.write("Developed by Anas 🏆")
