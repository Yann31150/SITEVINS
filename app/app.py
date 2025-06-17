import streamlit as st
import sys
import os

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.style_utils import injecter_css
from utils.data_utils import charger_donnees
from pages.accueil import page_presentation
from pages.filtrage import page_recherche
from pages.resultats import page_resultats
from pages.recommandation import page_recommandation

# Configuration de la page
st.set_page_config(
    page_title="BouteillIA",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Masquer le menu hamburger et le footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
    </style>
""", unsafe_allow_html=True)

def main():
    injecter_css()
    df = charger_donnees()
    pages = ["Accueil", "Votre choix", "Résultats", "Recommandation"]
    if "page" not in st.session_state or st.session_state["page"] not in pages:
        st.session_state["page"] = "Accueil"
    with st.sidebar:
        st.title("🍷 Navigation")
        st.image("app/images/logo.png")
        page = st.radio(
            "Choisissez une page",
            pages,
            index=pages.index(st.session_state["page"])
        )
        if st.session_state["page"] != page:
            st.session_state.page = page

    # Affichage de la page correspondante
    if st.session_state.page == "Accueil":
        page_presentation(df)
    elif st.session_state.page == "Votre choix":
        page_recherche(df)
    elif st.session_state.page == "Résultats":
        page_resultats(df)
    elif st.session_state.page == "Recommandation":
        page_recommandation(df)

    # Pour gérer redirection automatique après recherche
    if st.session_state.get("page") == "Résultats" and page != "Résultats":
        page_resultats(df)

if __name__ == "__main__":
    main()
