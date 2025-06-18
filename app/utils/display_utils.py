import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
import os

def afficher_badge_bio():
    st.markdown(
        '<span style="background-color: #4CAF50; color: white; padding: 5px 10px; border-radius: 15px;">Vin Bio</span>',
        unsafe_allow_html=True
    )

# def charger_image_depuis_url(url):
#     try:
#         if pd.isna(url) or url == 'nan':
#             return None
#         url = url.strip()
#         if not url.startswith('http'):
#             url = 'https://www.vinatis.com/' + url
#         response = requests.get(url, timeout=5)
#         if response.status_code == 200:
#             return Image.open(BytesIO(response.content))
#         else:
#             st.error(f"Erreur HTTP {response.status_code} pour l'URL: {url}")
#             return None
#     except Exception as e:
#         st.error(f"Erreur lors du chargement de l'image: {str(e)}")
#         return None

def afficher_infos_vin(vin, show_recommendations=False, df=None):
    # Affichage de l'image locale uniquement
    if 'NomFichier' in vin and pd.notna(vin['NomFichier']):
        local_path = os.path.join('data', 'final', 'images', str(vin['NomFichier']))
        if os.path.exists(local_path):
            st.image(local_path, width=300, caption=vin['nom'])
        else:
            st.warning("Image locale non trouvée pour ce vin")
    else:
        st.warning("Pas d'image locale disponible pour ce vin")

    st.markdown(f"### {vin['nom']} - {vin['prix']}€")
    st.write(f"**Pays:** {vin['pays']}")
    st.write(f"**Région:** {vin['region']}")
    st.write(f"**Couleur:** {vin['couleur']}")
    st.write(f"**Degré d'alcool:** {vin['deg_alcool']}%")
    if vin['bio'] == '1':
        afficher_badge_bio()
    if pd.notna(vin['accords']) and vin['accords'] != 'nan':
        accords = vin['accords'].replace('[', '').replace(']', '').replace("'", '')
        st.write(f"**Accords mets et vins:** {accords}")
    if pd.notna(vin['desc']) and vin['desc'] != 'nan':
        st.write(f"**Description:** {vin['desc']}")
    
    # Bouton toujours actif, même en mode recommandation
    if df is not None:
        if st.button(f"Voir les recommandations pour {vin['nom']}", key=f"reco_{vin['nom']}"):
            st.session_state.selected_wine = vin
            st.session_state.page = "Recommandation"
            st.write("Debug: Changement de page vers Recommandation")  # Message de débogage
            st.rerun()

def afficher_recommandations(selected_wine, df):
    # Bouton de retour en haut à droite
    col1, col2 = st.columns([6, 1])
    with col2:
        st.markdown("##")  # Espace pour l'alignement vertical
        if st.button("⬅️ Retour aux résultats", use_container_width=True):
            st.session_state.show_recommendations = False
            st.session_state.page = "Résultats"
            st.rerun()

    st.markdown("### 🍷 Vins recommandés")

    # Affichage des recommandations 2 par 2
    for i in range(1, 5, 2):  # i = 1, 3
        reco_col1 = f'reco{i}'
        reco_col2 = f'reco{i+1}'

        col1, col2 = st.columns(2)

        if reco_col1 in df.columns and pd.notna(selected_wine[reco_col1]):
            reco_wine_1 = df[df['nom'] == selected_wine[reco_col1]].iloc[0]
            with col1:
                st.markdown("---")
                afficher_infos_vin(reco_wine_1, show_recommendations=True, df=df)

        if reco_col2 in df.columns and pd.notna(selected_wine[reco_col2]):
            reco_wine_2 = df[df['nom'] == selected_wine[reco_col2]].iloc[0]
            with col2:
                st.markdown("---")
                afficher_infos_vin(reco_wine_2, show_recommendations=True, df=df)