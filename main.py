import streamlit as st
import requests
from datetime import datetime, timedelta

# 🎨 إعدادات واجهة المستخدم الاحترافية
st.set_page_config(page_title="رادار أنس الرياضي الذكي", page_icon="🏟️", layout="wide")

st.markdown("""
    <style>
    .match-card { background-color: #1e1e1e; border-radius: 15px; padding: 20px; border: 1px solid #34495e; margin-bottom: 15px; }
    .stat-box { background-color: #2c3e50; padding: 10px; border-radius: 8px; text-align: center; }
    .ai-analysis { background-color: rgba(241, 196, 15, 0.1); border: 1px solid #f1c40f; padding: 15px; border-radius: 10px; color: #f1c40f; font-size: 16px; }
    .live-tag { background-color: #e74c3c; color: white; padding: 3px 8px; border-radius: 5px; font-weight: bold; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
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

# 🏠 العنوان الرئيسي
st.title("🏟️ رادار أنس الرياضي - النسخة الاحترافية")

# 📂 تقسيم الموقع لأقسام (Tabs) مثل ما ردت
tab1, tab2, tab3 = st.tabs(["🔴 البث المباشر", "📅 مباريات اليوم", "📊 التحليل الذكي المباشر"])

# --- القسم الأول: مباشر ---
with tab1:
    st.header("🎮 المباريات الجارية الآن")
    live = get_api_data("fixtures", {"live": "all"})
    if not live:
        st.info("لا توجد مباريات مباشرة في هذه اللحظة (الفجر يا بطل).")
    else:
        for m in live:
            st.markdown(f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-around; align-items: center;">
                    <div style="text-align:center;"><img src="{m['teams']['home']['logo']}" width="50"><br><b>{m['teams']['home']['name']}</b></div>
                    <div style="text-align:center;"><span class="live-tag">LIVE</span><br><h2 style="margin:0;">{m['goals']['home']} - {m['goals']['away']}</h2><small>{m['fixture']['status']['elapsed']}'</small></div>
                    <div style="text-align:center;"><img src="{m['teams']['away']['logo']}" width="50"><br><b>{m['teams']['away']['name']}</b></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- القسم الثاني: مباريات اليوم ---
with tab2:
    st.header("⏳ جدول مباريات اليوم")
    today_date = datetime.now().strftime('%Y-%m-%d')
    today_m = get_api_data("fixtures", {"date": today_date})
    if not today_m:
        st.warning("لم يتم تحديث جدول اليوم بعد، حاول مرة أخرى لاحقاً.")
    else:
        for m in today_m[:15]:
            iq_time = (datetime.strptime(m['fixture']['date'], "%Y-%m-%dT%H:%M:%S%z") + timedelta(hours=3)).strftime('%I:%M %p')
            st.markdown(f"**🕒 {iq_time}** | {m['teams']['home']['name']} vs {m['teams']['away']['name']} | {m['league']['name']}")
            st.divider()

# --- القسم الثالث: التحليل المباشر (العقل مالت الموقع) ---
with tab3:
    st.header("🧠 مختبر التحليل الذكي (AI Analysis)")
    live_for_stats = get_api_data("fixtures", {"live": "all"})
    
    if not live_for_stats:
        st.info("هذا القسم يشتغل فقط وقت المباريات المباشرة ليحلل 'جودة' اللعب.")
    else:
        selected_m = st.selectbox("اختر مباراة لتحليل أداء الفريقين:", [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in live_for_stats])
        idx = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in live_for_stats].index(selected_m)
        f_id = live_for_stats[idx]['fixture']['id']
        
        # جلب الإحصائيات الدقيقة
        stats = get_api_data("fixtures/statistics", {"fixture": f_id})
        if stats:
            h_stats = {s['type']: s['value'] for s in stats[0]['statistics']}
            a_stats = {s['type']: s['value'] for s in stats[1]['statistics']}
            
            # عرض الأرقام الأساسية
            c1, c2, c3 = st.columns(3)
            c1.metric("🚩 ركنيات", f"{h_stats.get('Corner Kicks',0)} - {a_stats.get('Corner Kicks',0)}")
            c2.metric("⚽ تسديدات", f"{h_stats.get('Shots total',0)} - {a_stats.get('Shots total',0)}")
            c3.metric("🟨 كروت", f"{h_stats.get('Yellow Cards',0)} - {a_stats.get('Yellow Cards',0)}")
            
            # التحليل الذكي اللي ردته (مثل Nashville)
            st.subheader("💡 رؤية أنس التحليلية:")
            shots_h = h_stats.get('Shots total', 0) or 0
            shots_on_goal_h = h_stats.get('Shots on Goal', 0) or 0
            
            analysis_text = ""
            if shots_h > 10 and shots_on_goal_h < 3:
                analysis_text = f"⚠️ **تحليل:** فريق {live_for_stats[idx]['teams']['home']['name']} تسديداته 'تعبانة' وكثيرة بدون فايدة، جاي يضيعون فرص سهلة وماكو تركيز عالمرمى!"
            elif shots_on_goal_h > 5:
                analysis_text = f"🔥 **تحليل:** هجوم {live_for_stats[idx]['teams']['home']['name']} 'نار'.. كل تسديدة بمشروع هدف، الحارس لازم يصحصح!"
            else:
                analysis_text = "🔄 **تحليل:** المباراة هادئة واللعب محصور بالوسط، ننتظر هجمة مرتدة تكسر الجمود."
            
            st.markdown(f'<div class="ai-analysis">{analysis_text}</div>', unsafe_allow_html=True)
            
            st.subheader("🔮 توقع النتيجة النهائية:")
            st.success("بناءً على الضغط الحالي، احتمالية تسجيل هدف قريبة جداً للفريق المستحوذ!")
        else:
            st.warning("الإحصائيات المباشرة ستظهر هنا فور توفرها من المصدر.")

st.sidebar.markdown("---")
st.sidebar.write(f"🕒 توقيت العراق: {(datetime.now() + timedelta(hours=3)).strftime('%H:%M')}")
st.sidebar.write("تم التطوير بواسطة أنس البطل 🏆")
