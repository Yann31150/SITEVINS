import streamlit as st

def page_presentation(df):
    st.title("🍷 BouteillIA")
    st.subheader("Bienvenue")
    st.markdown("""
    <div class="logo-container">
        <img src="chemin_vers_votre_logo.png" alt="Logo Viticulture" style="max-width: 300px;">
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-text">
        <h2>Notre Projet</h2>
        <p>
        Bienvenue dans notre projet dédié à l'univers passionnant de la viticulture. 
        Notre équipe a développé une plateforme innovante combinant expertise viticole 
        et intelligence artificielle pour vous offrir une expérience unique de découverte 
        et de recommandation de vins.
        </p>
        <h2>Notre Équipe</h2>
        <p>
        Notre équipe est composée de passionnés de data science et d'œnologie, 
        réunissant leurs compétences pour créer un outil intelligent de recommandation 
        de vins. Nous utilisons des algorithmes de machine learning sophistiqués pour 
        analyser les caractéristiques des vins et proposer des recommandations personnalisées.
        </p>
        <h2>Fonctionnalités Principales</h2>
        <ul>
            <li>Exploration détaillée de notre base de données de vins</li>
            <li>Système de filtrage avancé</li>
            <li>Recommandations personnalisées basées sur l'intelligence artificielle</li>
            <li>Visualisation interactive des données</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Statistiques
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nombre de vins", len(df))
    with col2:
        st.metric("Pays représentés", len(df['pays'].unique()))
