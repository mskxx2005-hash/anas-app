import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Football AI Tools", layout="wide")

# --- القائمة الجانبية (The Sidebar Tools) ---
with st.sidebar:
    st.title("🛠️ الأدوات الذكية")
    st.write("اختر الأداة المطلوبة:")
    
    # صنع أزرار الاختيار (Navigation)
    tool_choice = st.radio(
        "الأقسام المتاحة:",
        ["🏠 الشاشة الرئيسية", "📅 مباريات اليوم", "🔴 البث المباشر والتحليل", "📊 خوارزميات الإحصائيات"]
    )
    
    st.write("---")
    st.info("الموقع يعمل بنظام AI لتحديث البيانات تلقائياً.")

# --- منطق التنقل بين الأدوات ---

if tool_choice == "🏠 الشاشة الرئيسية":
    st.markdown("<h1 style='text-align: center;'>⚽ مرحبا بكم في كرة القدم</h1>", unsafe_allow_html=True)
    st.write("استخدم القائمة الجانبية (Tools) للتنقل بين الأقسام.")

elif tool_choice == "📅 مباريات اليوم":
    st.header("📅 جدول مباريات اليوم")
    st.info("🏴󠁧󠁢󠁥󠁮󠁧󠁿 مانشستر سيتي vs ليفربول (ساعة 10:00)")
    st.info("🇪🇸 ريال مدريد vs برشلونة (ساعة 11:30)")

elif tool_choice == "🔴 البث المباشر والتحليل":
    st.header("🔴 مباشر الآن مع التحليل الذكي")
    # تصميم الواجهة للمباشر
    with st.container():
        col1, col2, col3 = st.columns([2, 1, 2])
        col1.subheader("بايرن ميونخ")
        col2.header("1 - 0")
        col3.subheader("باريس سان جيرمان")
        
    st.divider()
    st.warning("🤖 خوارزمية التحليل: ضغط عالي من بايرن (80%) وتراجع دفاعي لباريس.")

elif tool_choice == "📊 خوارزميات الإحصائيات":
    st.header("📊 ركن الإحصائيات والخوارزميات")
    st.write("هنا تظهر بيانات الاستحواذ، التسديدات، والتوقعات بدقة عالية.")
    # مثال لشريط إحصائي
    st.progress(65, text="نسبة الاستحواذ للفريق المستضيف")
