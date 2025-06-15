import streamlit as st
from utils.display_utils import afficher_recommandations

def page_recommandation(df):
    st.title("🍷 Système de recommandation")
    st.write(st.session_state.page)
    # On vérifie si un vin est sélectionné dans la session
    selected_wine = st.session_state.get("selected_wine", None)

    if selected_wine is not None:
        # Afficher les recommandations associées à ce vin
        afficher_recommandations(selected_wine, df)
        
        # # Bouton pour revenir aux résultats
        # if st.button("Retour aux résultats"):
        #     print("OKOKOKOKOKOKOK")
        #     st.session_state.page = "Résultats"
        #     st.session_state.show_recommendations = False
        #     st.rerun()
    else:
        st.info("Veuillez d'abord sélectionner un vin depuis les résultats de recherche pour afficher ses recommandations.")
        if st.button("Retour à la recherche"):
            st.session_state.page = "Filtrage des vins"
            st.rerun()
