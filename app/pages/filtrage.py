import streamlit as st
from utils.data_utils import filtrer_vins

def page_recherche(df):
    st.title("🍷 BouteillIA")
    st.header("Recherche de vins")
    
    # Filtres de recherche
    col1, col2 = st.columns(2)
    with col1:
        pays_list = ["Tous"] + sorted([str(x) for x in df['pays'].dropna().unique()])
        couleur_list = ["Tous"] + sorted([str(x) for x in df['couleur'].dropna().unique()])
        nom_list = ["Tous"] + sorted([str(x) for x in df['nom'].dropna().unique()])
        
        recherche_nom = st.selectbox("Rechercher un vin par son nom", nom_list)
        pays = st.selectbox("Pays", pays_list)
        couleur = st.selectbox("Couleur du vin", couleur_list)
        
        all_accords = []
        for accords in df['accords'].dropna():
            accords_list = accords.replace('[', '').replace(']', '').replace("'", '').split(', ')
            all_accords.extend(accords_list)
        selected_accords = st.multiselect(
            "Accords mets et vins",
            options=sorted(list(set(all_accords))),
            help="Sélectionnez un ou plusieurs accords mets et vins"
        )
        bio = st.checkbox("Vins bio uniquement")

    prix_min = float(df['prix'].min())
    prix_max = float(df['prix'].max())
    prix_range = st.slider(
        "Prix (€)",
        min_value=prix_min,
        max_value=prix_max,
        value=(prix_min, prix_max),
        step=1.0,
        help="Sélectionnez une fourchette de prix"
    )
    prix_min, prix_max = prix_range

    # Recherche
    if st.button("Rechercher"):
        resultats = filtrer_vins(
            df, recherche_nom, pays, couleur, bio, prix_min, prix_max, selected_accords
        )
        st.session_state.resultats = resultats
        st.session_state.page = "Résultats"
        st.rerun()
