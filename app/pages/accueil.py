import streamlit as st
import sys
import os

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.visualisation import plot_bio_by_country, plot_couleurs_et_type, plot_bio_vs_total_pays

def page_presentation(df):
    st.title("🍷 BouteillIA")
    st.subheader("Bienvenue")

    # Création de trois colonnes pour centrer l'image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("app/images/imagecentre.png", width=500)

    # Pavé 1 : Titre, sous-titre, logo
    st.markdown("""
        <div style="text-align:center; margin-top: -30px; margin-bottom: 20px;">
            <h1 style="color:#a83232;">🍷 BouteillIA</h1>
            <h3 style="font-style: italic; color: #555;">
                Votre sommelier digital, à la carte
            </h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Pavé 2 : Contexte & graphique Bio + Total
    with st.container():
        st.markdown("""
            <div style="background:#f8f1e7; padding:18px 14px; border-radius:18px; margin-bottom:14px;">
                <b>📉 Marché du vin&nbsp;: une profonde mutation</b><br>
                • <b>-70 %</b> de consommation depuis 1960.<br>
                • <b>11 %</b> des Français consomment du vin chaque jour (2022, vs 50 % en 1980).<br>
                • <b>-2,4 %</b> de volume consommé en 2024 (24,4M hl).<br>
                • <b>Bio</b> : <b>21,7 %</b> des surfaces, +250 % depuis 2010.<br><br>
                Aujourd'hui, les jeunes privilégient la qualité, l'originalité, les recommandations digitales et le bio.
            </div>
        """, unsafe_allow_html=True)
        plot_bio_vs_total_pays(df, mobile=True)

    # Pavé 3 : Fonctionnalités + graphique Couleurs et Type produit
    with st.container():
        st.markdown("""
            <div style=\"background:#eaf6ef; padding:18px 14px; border-radius:18px; margin-bottom:14px;\">
                <b>⚡️ Nos atouts</b>
                <ul style=\"margin:8px 0 0 0;\">
                    <li>Base de <b>5000+ vins français</b> et internationaux</li>
                    <li>Recommandation personnalisée par IA (KNN, analyse des profils)</li>
                    <li>Bio systématiquement valorisé dans les suggestions</li>
                    <li>Analyse des avis clients et des goûts, <i>sentiment analysis</i></li>
                    <li>Interface claire, adaptée aux <b>néophytes comme aux connaisseurs</b></li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        plot_couleurs_et_type(df, mobile=True)

    # Pavé 4 : Appel à l'action + stats dynamiques + graphique pays
    st.markdown("""
        <div style="background:#f7e2ea; padding:20px 14px; border-radius:18px; text-align:center;">
            <h4 style="margin-top:0;">🥂 Votre prochaine dégustation commence ici !</h4>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Vins référencés", len(df))
    with col2:
        st.metric("Pays couverts", len(df['pays'].unique()))

    st.markdown("</div>", unsafe_allow_html=True)
    

    # Gros bouton d'accès avec navigation Streamlit
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Explorer les vins 🍇", key="go_filtrage", help="Aller à la page de filtrage des vins", use_container_width=True):
            st.session_state["page"] = "Votre choix"
            st.rerun()