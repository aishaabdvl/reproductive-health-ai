import streamlit as st
import datetime

st.set_page_config(
    page_title="Luna - Reproductive Health AI",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
    
    /* BOLD pink/lavender sunset background - very visible! */
    .main {
        background: 
            linear-gradient(135deg, 
                #FFD6E8 0%,
                #FFCCE5 15%,
                #FFC2E2 25%, 
                #E8D5F2 40%,
                #DCCEF2 55%,
                #D5E8F5 70%,
                #E6D9F2 85%,
                #F7C6D0 100%
            );
        background-attachment: fixed;
        font-family: 'Inter', sans-serif;
        position: relative;
        min-height: 100vh;
    }
    
    /* Large decorative symbols */
    .main::before {
        content: '✧';
        position: fixed;
        top: 8%;
        right: 5%;
        font-size: 4rem;
        opacity: 0.3;
        animation: float 6s ease-in-out infinite;
        z-index: 0;
        color: #F28BA8;
    }
    
    .main::after {
        content: '♡';
        position: fixed;
        bottom: 10%;
        left: 5%;
        font-size: 4.5rem;
        opacity: 0.3;
        animation: float 7s ease-in-out infinite reverse;
        z-index: 0;
        color: #B58DB6;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
    }
    
    /* Pink/purple overlay effect */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(ellipse at top, rgba(247, 198, 208, 0.4) 0%, transparent 60%),
            radial-gradient(ellipse at bottom right, rgba(230, 217, 242, 0.4) 0%, transparent 50%),
            radial-gradient(ellipse at bottom left, rgba(255, 154, 139, 0.3) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    /* HUGE hero header */
    .hero-section {
        text-align: center;
        padding: 100px 40px 80px;
        margin-bottom: 80px;
        position: relative;
        z-index: 1;
    }
    
    .luna-hero {
        font-family: 'Playfair Display', serif;
        font-size: 8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #B58DB6 0%, #F28BA8 50%, #FF9A8B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        letter-spacing: -4px;
        line-height: 1;
    }
    
    .hero-tagline {
        font-size: 2.8rem;
        font-weight: 600;
        color: #6B5B6E;
        letter-spacing: -1.5px;
        margin-top: 10px;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 400;
        color: #6B5B6E;
        margin-top: 30px;
        max-width: 750px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.7;
    }
    
    /* Apple-style showcase cards - less white, more pink */
    .showcase-card {
        background: rgba(255, 240, 245, 0.7);
        backdrop-filter: blur(30px);
        padding: 70px;
        border-radius: 32px;
        border: 1px solid rgba(242, 139, 168, 0.4);
        box-shadow: 0 20px 60px rgba(181, 141, 182, 0.2);
        margin: 50px 0;
        position: relative;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 1;
    }
    
    .showcase-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 30px 80px rgba(181, 141, 182, 0.3);
        background: rgba(255, 230, 240, 0.75);
    }
    
    .showcase-number {
        font-size: 9rem;
        font-weight: 700;
        background: linear-gradient(135deg, rgba(242, 139, 168, 0.2), rgba(181, 141, 182, 0.2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: absolute;
        top: -30px;
        right: 50px;
    }
    
    .showcase-emoji {
        font-size: 5rem;
        margin-bottom: 30px;
        display: inline-block;
        color: #F28BA8;
    }
    
    .showcase-title {
        font-size: 3.2rem;
        font-weight: 700;
        color: #6B5B6E;
        margin-bottom: 30px;
        letter-spacing: -2px;
    }
    
    .showcase-description {
        font-size: 1.35rem;
        line-height: 1.9;
        color: #6B5B6E;
    }
    
    /* Feature tiles - pink tinted */
    .feature-tile {
        background: rgba(255, 235, 245, 0.65);
        backdrop-filter: blur(20px);
        padding: 50px;
        border-radius: 24px;
        border: 1px solid rgba(247, 198, 208, 0.5);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        height: 100%;
        z-index: 1;
    }
    
    .feature-tile::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #F28BA8, #B58DB6, #9FC9C3);
        transform: scaleX(0);
        transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .feature-tile:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(181, 141, 182, 0.25);
        border-color: #F28BA8;
        background: rgba(255, 225, 240, 0.7);
    }
    
    .feature-tile:hover::after {
        transform: scaleX(1);
    }
    
    .feature-icon {
        font-size: 4rem;
        margin-bottom: 24px;
        color: #F28BA8;
    }
    
    .feature-title {
        font-size: 1.6rem;
        font-weight: 600;
        color: #6B5B6E;
        margin-bottom: 16px;
    }
    
    .feature-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #6B5B6E;
    }
    
    /* CTA section - pink/lavender */
    .cta-section {
        background: linear-gradient(135deg, rgba(242, 139, 168, 0.3), rgba(181, 141, 182, 0.3));
        backdrop-filter: blur(30px);
        padding: 90px 70px;
        border-radius: 40px;
        text-align: center;
        margin: 90px 0;
        border: 1px solid rgba(247, 198, 208, 0.5);
        box-shadow: 0 30px 70px rgba(181, 141, 182, 0.25);
        position: relative;
        z-index: 1;
    }
    
    .cta-title {
        font-size: 3.8rem;
        font-weight: 700;
        color: #6B5B6E;
        margin-bottom: 24px;
        letter-spacing: -2px;
    }
    
    .cta-subtitle {
        font-size: 1.5rem;
        color: #6B5B6E;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #F28BA8, #B58DB6);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 22px 60px;
        font-size: 1.2rem;
        font-weight: 600;
        box-shadow: 0 10px 35px rgba(242, 139, 168, 0.4);
        transition: all 0.4s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 45px rgba(242, 139, 168, 0.5);
    }
    
    /* Sidebar - pink gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, 
            rgba(255, 220, 240, 0.95) 0%,
            rgba(245, 215, 245, 0.95) 50%,
            rgba(235, 225, 255, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(247, 198, 208, 0.5);
    }
    
    /* Inputs - pink tinted */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select, 
    .stTextArea>div>div>textarea,
    .stDateInput>div>div>input {
        border-radius: 16px;
        border: 1.5px solid #E6D9F2;
        background: rgba(255, 245, 250, 0.9);
        padding: 18px 24px;
        font-size: 1.05rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus,
    .stSelectbox>div>div>select:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #F28BA8;
        box-shadow: 0 0 0 4px rgba(242, 139, 168, 0.25);
        transform: translateY(-2px);
        background: rgba(255, 240, 245, 0.95);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #B58DB6;
        font-weight: 700;
        font-size: 2.4rem;
    }
    
    /* Radio */
    .stRadio > label {
        padding: 18px 22px;
        border-radius: 14px;
        transition: all 0.25s ease;
        color: #6B5B6E;
        font-weight: 500;
    }
    
    .stRadio > label:hover {
        background: rgba(247, 198, 208, 0.35);
    }
    
    /* Success/Info */
    .stSuccess {
        background: linear-gradient(135deg, rgba(159, 201, 195, 0.3), rgba(159, 201, 195, 0.25));
        border: 1.5px solid #9FC9C3;
        border-radius: 16px;
        padding: 22px 30px;
    }
    
    .stInfo {
        background: linear-gradient(135deg, rgba(207, 224, 245, 0.35), rgba(221, 234, 246, 0.3));
        border: 1.5px solid #CFE0F5;
        border-radius: 16px;
        padding: 22px 30px;
    }
    
    /* Typography */
    h1, h2, h3 {
        font-weight: 700;
        color: #6B5B6E;
    }
    
    p {
        color: #6B5B6E;
        line-height: 1.7;
    }
    
    /* Hide branding */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Scrollbar - pink */
    ::-webkit-scrollbar {width: 10px;}
    ::-webkit-scrollbar-track {background: rgba(255, 220, 240, 0.5);}
    ::-webkit-scrollbar-thumb {background: linear-gradient(180deg, #F28BA8, #B58DB6); border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

# Hero
st.markdown('''
    <div class="hero-section">
        <div class="luna-hero">Luna</div>
        <div class="hero-tagline">Your Reproductive Health AI</div>
        <div class="hero-subtitle">
            Understand your body. Track patterns. Make informed decisions.<br>
            All powered by AI that cares about your health.
        </div>
    </div>
''', unsafe_allow_html=True)

# Showcases
st.markdown("""
<div class="showcase-card">
    <span class="showcase-number">01</span>
    <div class="showcase-emoji">✧</div>
    <h2 class="showcase-title">Smart. Personal. Insightful.</h2>
    <p class="showcase-description">
        Luna learns from your unique patterns, adapting to your body's rhythm. 
        Track symptoms, moods, and cycles with an AI that understands you're not just data—you're a person.
    </p>
</div>

<div class="showcase-card">
    <span class="showcase-number">02</span>
    <div class="showcase-emoji">♡</div>
    <h2 class="showcase-title">Evidence-Based Intelligence</h2>
    <p class="showcase-description">
        Powered by medical research and machine learning, Luna identifies patterns that matter. 
        Get insights on PCOS, endometriosis, and hormonal health—all backed by science.
    </p>
</div>

<div class="showcase-card">
    <span class="showcase-number">03</span>
    <div class="showcase-emoji">✦</div>
    <h2 class="showcase-title">Your Health Companion</h2>
    <p class="showcase-description">
        Chat with Luna anytime. Ask questions, learn about your body, and prepare for doctor visits. 
        Get compassionate, judgment-free health education whenever you need it.
    </p>
</div>
""", unsafe_allow_html=True)

# Features
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="feature-tile">
        <div class="feature-icon">✧</div>
        <h3 class="feature-title">Track Everything</h3>
        <p class="feature-text">Log symptoms, moods, cycles—Luna finds the connections you might miss</p>
    </div>
    
    <div class="feature-tile">
        <div class="feature-icon">✦</div>
        <h3 class="feature-title">Beautiful Insights</h3>
        <p class="feature-text">Visualize your health journey with clear, elegant charts</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-tile">
        <div class="feature-icon">♡</div>
        <h3 class="feature-title">Private & Secure</h3>
        <p class="feature-text">Your health data stays yours, protected and confidential always</p>
    </div>
    
    <div class="feature-tile">
        <div class="feature-icon">⋆</div>
        <h3 class="feature-title">Empowering</h3>
        <p class="feature-text">Knowledge is power—advocate for yourself with confidence</p>
    </div>
    """, unsafe_allow_html=True)

# CTA
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Ready to begin your journey?</h2>
    <p class="cta-subtitle">Start tracking today and unlock personalized insights about your health</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 40px 25px; margin-bottom: 40px; 
                    background: rgba(255, 230, 245, 0.75); backdrop-filter: blur(20px);
                    border-radius: 20px; border: 1px solid rgba(247, 198, 208, 0.6);">
            <h2 style="color: #B58DB6; font-size: 1.8rem; font-weight: 700;">Navigation</h2>
        </div>
    """, unsafe_allow_html=True)
    
    page = st.radio("Select:", ["Home", "Symptom Tracker", "Risk Assessment", "Chat with Luna", "Dashboard"], label_visibility="collapsed")
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; padding: 25px; margin: 25px 0;
                    background: rgba(255, 230, 245, 0.75); backdrop-filter: blur(20px);
                    border-radius: 20px; border: 1px solid rgba(247, 198, 208, 0.6);">
            <p style="color: #B58DB6; font-weight: 600; font-size: 1.1rem; margin-bottom: 25px;">Your Progress</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Days", "0")
    with col2:
        st.metric("Insights", "0")
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    st.info("✧ Start tracking to unlock personalized insights")

# Pages
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

if "Home" in page:
    st.markdown("""
        <div style="text-align: center; padding: 80px 50px; 
                    background: rgba(255, 235, 245, 0.7); backdrop-filter: blur(30px);
                    border-radius: 32px; border: 1px solid rgba(247, 198, 208, 0.5);
                    box-shadow: 0 20px 60px rgba(181, 141, 182, 0.2);">
            <p style="font-size: 1.6rem; color: #B58DB6; font-weight: 600; margin-bottom: 18px;">Luna is ready</p>
            <p style="font-size: 1.2rem; color: #6B5B6E;">Select a feature from the sidebar to begin</p>
        </div>
    """, unsafe_allow_html=True)
    
elif "Tracker" in page:
    st.markdown('<h2 style="color: #B58DB6; font-size: 3.2rem; text-align: center; margin-bottom: 60px; font-weight: 700;">Symptom Tracker</h2>', unsafe_allow_html=True)
    
    st.markdown('<div style="background: rgba(255, 240, 248, 0.75); backdrop-filter: blur(40px); padding: 60px; border-radius: 32px; border: 1px solid rgba(242, 139, 168, 0.4); box-shadow: 0 20px 60px rgba(181, 141, 182, 0.2);">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        date = st.date_input("✧ Date", datetime.date.today())
    with col2:
        mood = st.selectbox("♡ Mood", ["Excellent", "Good", "Neutral", "Poor", "Difficult"])
    with col3:
        energy = st.selectbox("✦ Energy", ["High", "Moderate", "Low", "Very Low"])
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    symptoms = st.multiselect("Select your symptoms", ["Cramps", "Bloating", "Headache", "Fatigue", "Mood changes", "Breast tenderness", "Acne", "Back pain", "Nausea", "Heavy flow", "Irregular cycle", "Other"])
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    notes = st.text_area("Additional notes (optional)", height=140)
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Save Entry", type="primary", use_container_width=True):
            st.balloons()
            st.success("✧ Entry saved! Luna is learning your patterns.")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
elif "Risk" in page:
    st.markdown('<h2 style="color: #B58DB6; font-size: 3.2rem; text-align: center; margin-bottom: 60px; font-weight: 700;">Risk Assessment</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background: rgba(255, 240, 248, 0.75); backdrop-filter: blur(40px); padding: 60px; border-radius: 32px; border: 1px solid rgba(242, 139, 168, 0.4); box-shadow: 0 20px 60px rgba(181, 141, 182, 0.2);">
            <h3 style="color: #F28BA8; margin-bottom: 30px; font-weight: 700; font-size: 1.9rem;">Coming Soon</h3>
            <p style="color: #6B5B6E; font-size: 1.2rem; line-height: 2;">
                AI-powered risk assessment will analyze your symptom patterns to identify potential health conditions.
            </p>
            <ul style="color: #6B5B6E; font-size: 1.15rem; line-height: 2.3; margin-top: 30px; padding-left: 35px;">
                <li>Evidence-based risk scores</li>
                <li>Pattern analysis and correlations</li>
                <li>Healthcare provider discussion points</li>
                <li>Personalized educational resources</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
elif "Chat" in page:
    st.markdown('<h2 style="color: #B58DB6; font-size: 3.2rem; text-align: center; margin-bottom: 60px; font-weight: 700;">Chat with Luna</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background: rgba(255, 240, 248, 0.75); backdrop-filter: blur(40px); padding: 60px; border-radius: 32px; border: 1px solid rgba(242, 139, 168, 0.4); box-shadow: 0 20px 60px rgba(181, 141, 182, 0.2);">
            <h3 style="color: #F28BA8; margin-bottom: 30px; font-weight: 700; font-size: 1.9rem;">Coming Soon</h3>
            <p style="color: #6B5B6E; font-size: 1.2rem; line-height: 2;">
                An AI-powered conversational interface for reproductive health education.
            </p>
            <ul style="color: #6B5B6E; font-size: 1.15rem; line-height: 2.3; margin-top: 30px; padding-left: 35px;">
                <li>Understand symptoms and conditions</li>
                <li>Prepare questions for appointments</li>
                <li>Learn at your own pace</li>
                <li>Access trusted health information</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="Ask Luna anything...", key="chat_input")
    
elif "Dashboard" in page:
    st.markdown('<h2 style="color: #B58DB6; font-size: 3.2rem; text-align: center; margin-bottom: 60px; font-weight: 700;">Health Dashboard</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Entries", "0")
    with col2:
        st.metric("Current Streak", "0 days")
    with col3:
        st.metric("Avg Cycle", "N/A")
    with col4:
        st.metric("Insights", "0")
    
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background: rgba(255, 240, 248, 0.75); backdrop-filter: blur(40px); padding: 60px; border-radius: 32px; border: 1px solid rgba(242, 139, 168, 0.4); box-shadow: 0 20px 60px rgba(181, 141, 182, 0.2); text-align: center;">
            <p style="color: #B58DB6; font-size: 1.35rem; font-weight: 600; line-height: 2;">
                Start tracking your symptoms to unlock your personalized dashboard with beautiful visualizations and insights
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div style='height: 90px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 60px; background: rgba(255, 235, 245, 0.7); backdrop-filter: blur(30px); border-radius: 32px; border: 1px solid rgba(247, 198, 208, 0.5); box-shadow: 0 20px 60px rgba(181, 141, 182, 0.2);">
    <p style="color: #B58DB6; font-size: 1.2rem; margin-bottom: 25px; font-weight: 600;">Important Disclaimer</p>
    <p style="color: #6B5B6E; font-size: 1.1rem; line-height: 2; max-width: 800px; margin: 0 auto;">
        Luna is an educational tool designed to empower you with knowledge. 
        It is not a substitute for professional medical advice, diagnosis, or treatment. 
        Always consult qualified healthcare providers about your health.
    </p>
    <p style="font-size: 1rem; color: #8B7A8E; margin-top: 40px;">© 2026 Luna — Reproductive Health AI</p>
</div>
""", unsafe_allow_html=True)