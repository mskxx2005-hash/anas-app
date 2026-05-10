import streamlit as st
import requests

# إعدادات واجهة موقع خوارزميات
st.set_page_config(page_title="موقع خوارزميات", page_icon="⚽")
st.title("أهلاً بكم في موقع خوارزميات")
st.subheader("التحليل الذكي والمباشر للمباريات")
st.markdown("---")

# المفتاح السري اللي لقطته من الصورة
API_KEY = "170d93f214msh2b139c9f91f8f55p1c9f1fjsn974e38b403a0"

# خانة البحث
team_query = st.text_input("ابحث عن فريق (بالإنجليزي):", placeholder="مثلاً: Real Madrid")

if team_query:
    # رابط المباريات المباشرة
    url = "https://free-api-live-football-data.p.rapidapi.com/football-fixtures-live"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
    }

    try:
        with st.spinner('خوارزميات تبحث في النتائج الحقيقية...'):
            response = requests.get(url, headers=headers)
            data = response.json()

        found = False
        if data.get('status') == 'success' and 'data' in data:
            for match in data['data']:
                home = match['home_team']['name']
                away = match['away_team']['name']
                
                # إذا الفريق اللي بحثت عنه موجود بالمباريات المباشرة هسة
                if team_query.lower() in home.lower() or team_query.lower() in away.lower():
                    found = True
                    st.success(f"🔴 مباراة مباشرة: {home} vs {away}")
                    
                    col1, col2 = st.columns(2)
                    col1.metric(f"{home}", match['home_score'])
                    col2.metric(f"{away}", match['away_score'])

                    st.header("📊 تحليل خوارزميات الذكي")
                    st.info(f"المباراة في الدقيقة {match.get('minute', '??')}. الخوارزمية تشخص أداءً تكتيكياً عالياً.")
                    break

        if not found:
            st.warning(f"حالياً {team_query} ما عندهم مباراة مباشرة. الخوارزمية تگول: ارجع وقت المباراة صدگ!")
            
    except:
        st.error("اكو مشكلة بالربط، تأكد إنك مفعل الـ API بـ RapidAPI.")
else:
    st.info("اكتب اسم الفريق حتى تبدأ الخوارزمية بالتحليل المباشر.")
