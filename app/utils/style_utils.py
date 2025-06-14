import streamlit as st

def injecter_css():
    st.markdown("""
    <style>
        [data-testid=stSidebarNav] {
            display:none;
        }
        :root {
            --wine-red: #722F37;
            --wine-burgundy: #4E1609;
            --wine-gold: #C1A87D;
            --wine-cream: #F2E8DC;
        }
        .sidebar .sidebar-content {
            background-color: var(--wine-burgundy);
            color: var(--wine-cream);
        }
        h1 { color: var(--wine-red); font-family: 'Playfair Display', serif; }
        .main-text { color: #333; font-size: 18px; line-height: 1.6; margin: 20px 0; }
        .logo-container { text-align: center; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)
