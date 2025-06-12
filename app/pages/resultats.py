import streamlit as st
from utils.display_utils import afficher_infos_vin, afficher_recommandations

def page_resultats(df):
    st.title("🍷 BouteillIA")
    st.header("Résultats de la recherche")
    
    if 'resultats' in st.session_state and not st.session_state.resultats.empty:
        resultats = st.session_state.resultats
        st.write(f"Nombre de vins trouvés : {len(resultats)}")
        for _, vin in resultats.iterrows():
            st.markdown("---")
            afficher_infos_vin(vin, df=df)
    else:
        st.info("Aucun résultat à afficher. Veuillez effectuer une recherche.")
        if st.button("Retour à la recherche"):
            st.session_state.page = "Filtrage des vins"
            st.rerun()
