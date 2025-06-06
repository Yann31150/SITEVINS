import streamlit as st
from utils.display_utils import afficher_recommandations

def page_recommandation(df):
    st.title("🍷 Système de recommandation")

    # On vérifie si un vin est sélectionné dans la session
    selected_wine = st.session_state.get("selected_wine", None)

    if selected_wine is not None:
        # Afficher les recommandations associées à ce vin
        afficher_recommandations(selected_wine, df)
    else:
        st.info("Veuillez d'abord sélectionner un vin depuis les résultats de recherche pour afficher ses recommandations.")
        if st.button("Retour à la recherche"):
            st.session_state.page = "Filtrage des vins"
            st.rerun()
