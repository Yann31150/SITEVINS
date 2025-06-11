import streamlit as st
import pandas as pd
from utils.data_utils import filtrer_vins

def page_recherche(df):
    st.title("🍷 BouteillIA")
    st.header("Recherche de vins")
    
    # Vérification du DataFrame
    if df is None or df.empty:
        st.error("Aucune donnée n'a pu être chargée. Veuillez vérifier que le fichier CSV est présent dans le dossier data/final.")
        return
    
    # Vérification des colonnes requises
    required_columns = ['pays', 'couleur', 'nom', 'prix', 'accords', 'bio']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        st.error(f"Le fichier CSV ne contient pas toutes les colonnes requises. Colonnes manquantes : {', '.join(missing_columns)}")
        return
    
    try:
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

        with col2:
            # Checkbox pour afficher uniquement les vins à plus de 500 €
            plus_de_500 = st.checkbox("Afficher uniquement les vins à plus de 500 €")

            if plus_de_500:
                prix_min = 500.01
                prix_max = float(df['prix'].max())
            else:
                prix_min = float(df['prix'].min())
                prix_max = min(float(df['prix'].max()), 500.0)

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
            
            if resultats.empty:
                st.warning("Aucun vin ne correspond à vos critères de recherche.")
            else:
                st.success(f"Nombre de vins trouvés : {len(resultats)}")
                st.session_state.resultats = resultats
                st.session_state.page = "Résultats"
                st.rerun()
                
    except Exception as e:
        st.error(f"Une erreur est survenue lors de l'affichage de la page : {str(e)}")
        st.error("Veuillez vérifier que le fichier CSV est correctement formaté.")