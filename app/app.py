import streamlit as st
from utils.style_utils import injecter_css
from utils.data_utils import charger_donnees
from pages.accueil import page_presentation
from pages.filtrage import page_recherche
from pages.resultats import page_resultats
from pages.recommandation import page_recommandation

def main():
    st.set_page_config(page_title="BouteillIA", page_icon="🍷", layout="wide")
    injecter_css()
    df = charger_donnees()
    if "page" not in st.session_state:
        st.session_state["page"] = "Présentation et KPI"
    with st.sidebar:
        st.title("🍷 Navigation")
        st.image("images/logo.png")
        page = st.radio(
            "Choisissez une page",
            ["Présentation et KPI", "Filtrage des vins", "Résultats", "Recommandation"],
            index=["Présentation et KPI", "Filtrage des vins", "Résultats", "Recommandation"].index(st.session_state["page"])
        )
        if st.session_state["page"] != page:
            st.session_state.page = page

    if page == "Présentation et KPI":
        page_presentation(df)
    elif page == "Filtrage des vins":
        page_recherche(df)
    elif page == "Résultats":
        page_resultats(df)
    elif page == "Recommandation":
        page_recommandation(df)

    # Pour gérer redirection automatique après recherche
    if st.session_state.get("page") == "Résultats" and page != "Résultats":
        page_resultats(df)

if __name__ == "__main__":
    main()
