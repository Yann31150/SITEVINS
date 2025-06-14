import streamlit as st

def injecter_css():
    st.markdown("""
    <style>
        [data-testid=stSidebarNav] {
            display:none;
        }
        /* Variables de couleurs */
        :root {
            --wine-red: #722F37;
            --wine-burgundy: #4E1609;
            --wine-gold: #C1A87D;
            --wine-cream: #F2E8DC;
        }

        /* Masquer les éléments Streamlit par défaut */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        .stApp > header {background-color: transparent;}
        .stApp > footer {background-color: transparent;}

        /* Style de la sidebar */
        .sidebar .sidebar-content {
            background-color: var(--wine-burgundy);
            color: var(--wine-cream);
        }
        .sidebar .sidebar-content .stRadio > div {
            color: var(--wine-cream);
        }
        .sidebar .sidebar-content .stRadio > div > div {
            color: var(--wine-cream);
        }

        /* Style des titres */
        h1 { 
            color: var(--wine-red); 
            font-family: 'Playfair Display', serif;
            font-size: 2.5em;
            margin-bottom: 1em;
        }
        h2 { 
            color: var(--wine-burgundy);
            font-family: 'Playfair Display', serif;
            font-size: 2em;
            margin-bottom: 0.8em;
        }
        h3 { 
            color: var(--wine-burgundy);
            font-family: 'Playfair Display', serif;
            font-size: 1.5em;
            margin-bottom: 0.6em;
        }

        /* Style du texte principal */
        .main-text { 
            color: #333; 
            font-size: 18px; 
            line-height: 1.6; 
            margin: 20px 0;
        }

        /* Style des boutons */
        .stButton > button {
            background-color: var(--wine-red);
            color: var(--wine-cream);
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: var(--wine-burgundy);
            color: var(--wine-cream);
        }

        /* Style des conteneurs */
        .logo-container { 
            text-align: center; 
            padding: 20px;
        }

        /* Style des cartes de vin */
        .vin-card {
            background-color: var(--wine-cream);
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)
