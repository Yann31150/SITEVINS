import streamlit as st
import sys
import os
import zipfile
import requests

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

def download_file_from_google_drive(id, destination):
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id': id}, stream=True)
    token = None
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Chemin où tu veux extraire les images
extract_path = "public/images"
zip_path = "public/images.zip"
google_drive_id = "1EQQmNfHT9TdBqhBBcdv3T0Mb6FubXa9d"  # Ton ID Google Drive

# Télécharge et décompresse si ce n'est pas déjà fait
if not os.path.exists(extract_path):
    os.makedirs(extract_path, exist_ok=True)
if not os.path.exists(os.path.join(extract_path, "00001.png")):
    if not os.path.exists(zip_path):
        download_file_from_google_drive(google_drive_id, zip_path)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

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
