import pandas as pd
import os
import streamlit as st

def charger_donnees():
    try:
        # Chemin relatif depuis le dossier app
        fichier_csv = os.path.join('data', 'final', 'base_vin_final.csv')
        if not os.path.exists(fichier_csv):
            # Essai avec le chemin absolu
            fichier_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'final', 'base_vin_final.csv')
        
        if not os.path.exists(fichier_csv):
            raise FileNotFoundError(f"Le fichier {fichier_csv} n'a pas été trouvé")
            
        df = pd.read_csv(fichier_csv)
        df['bio'] = df['bio'].apply(lambda x: 1 if pd.notna(x) and 'Certifié Eurofeuille' in str(x) else 0)
        
        # Gestion des visuels
        if 'visuel' not in df.columns:
            df['visuel'] = "https://www.vinatis.com/1-detail_default/default-wine.png"
        else:
            df['visuel'] = df['visuel'].apply(
                lambda x: f"https://www.vinatis.com/{x}" if pd.notna(x) and not str(x).startswith('http') else x
            )
        
        # Conversion des types
        for col in df.columns:
            if col != 'prix':
                df[col] = df[col].astype(str)
        df['prix'] = pd.to_numeric(df['prix'], errors='coerce')
        
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {str(e)}")
        return pd.DataFrame()

def filtrer_vins(df, nom, pays, couleur, bio, prix_min, prix_max, accords_selectionnes):
    """Filtre la base des vins selon les critères utilisateurs."""
    resultats = df.copy()
    if nom != "Tous":
        resultats = resultats[resultats['nom'] == nom]
    if pays != "Tous":
        resultats = resultats[resultats['pays'] == pays]
    if couleur != "Tous":
        resultats = resultats[resultats['couleur'] == couleur]
    if bio:
        resultats = resultats[resultats['bio'] == 1]
    resultats = resultats[(resultats['prix'] >= prix_min) & (resultats['prix'] <= prix_max)]
    if accords_selectionnes:
        mask = resultats['accords'].apply(
            lambda x: any(accord in str(x) for accord in accords_selectionnes)
        )
        resultats = resultats[mask]
    return resultats
