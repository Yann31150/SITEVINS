import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def afficher_badge_bio():
    st.markdown(
        '<span style="background-color: #4CAF50; color: white; padding: 5px 10px; border-radius: 15px;">Vin Bio</span>',
        unsafe_allow_html=True
    )

def charger_image_depuis_url(url):
    try:
        if pd.isna(url) or url == 'nan':
            return None
        url = url.strip()
        if not url.startswith('http'):
            url = 'https://www.vinatis.com/' + url
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            st.error(f"Erreur HTTP {response.status_code} pour l'URL: {url}")
            return None
    except Exception as e:
        st.error(f"Erreur lors du chargement de l'image: {str(e)}")
        return None

def afficher_infos_vin(vin, show_recommendations=False, df=None):
    if pd.notna(vin['visuel']) and vin['visuel'] != 'nan':
        image = charger_image_depuis_url(vin['visuel'])
        if image:
            st.image(image, width=300, caption=vin['nom'])
        else:
            st.warning("Impossible de charger l'image")
    else:
        st.warning("Pas d'image disponible pour ce vin")

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
    if not show_recommendations and df is not None:
        if st.button(f"Voir les recommandations pour {vin['nom']}", key=f"reco_{vin['nom']}"):
            st.session_state.selected_wine = vin
            st.session_state.show_recommendations = True
            st.session_state.df = df
            st.rerun()

def afficher_recommandations(selected_wine, df):
    st.markdown("### 🍷 Vins recommandés")
    col1, col2 = st.columns(2)
    for i in range(1, 5):
        reco_col = 'reco' + str(i)
        if reco_col in df.columns and pd.notna(selected_wine[reco_col]):
            reco_wine = df[df['nom'] == selected_wine[reco_col]].iloc[0]
            with col1 if i % 2 == 1 else col2:
                st.markdown("---")
                afficher_infos_vin(reco_wine, show_recommendations=True, df=df)
    if st.button("Retour aux résultats"):
        st.session_state.show_recommendations = False
        st.rerun()
