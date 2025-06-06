# BouteillIA — Plateforme de recommandation de vins

Bienvenue sur **BouteillIA**, un projet data science et web qui propose une expérience de découverte et de recommandation de vins, de la récupération des données jusqu’à la recommandation par intelligence artificielle.

---

## Table des matières

- [Présentation du projet](#présentation-du-projet)
- [Arborescence du projet](#arborescence-du-projet)
- [Pipeline de données](#pipeline-de-données)
- [Lancement de l'application web](#lancement-de-lapplication-web)
- [Dépendances](#dépendances)
- [Contribuer](#contribuer)
- [Auteurs](#auteurs)

---

## Présentation du projet

**BouteillIA** a pour objectif de :
- Scraper et centraliser une base de données de vins,
- Nettoyer et enrichir les données pour l'analyse,
- Appliquer des modèles de machine learning pour la recommandation,
- Offrir une interface web intuitive permettant d’explorer, filtrer et obtenir des suggestions de vins.

---

## Arborescence du projet

/ton_projet_viticulture/
│
├── data/
│ ├── raw/
│ │ ├── scraping_wines.ipynb
│ │ └── vins_bruts_150pages.csv
│ ├── processed/
│ │ ├── flattening.ipynb
│ │ ├── vins_aplatis.csv
│ │ ├── cleaning_ml.ipynb
│ │ └── vins_ml_ready.csv
│ └── final/
│ ├── ml_model.ipynb
│ └── base_vin_final.csv
│
├── app/
│ ├── app.py
│ ├── utils/
│ │ ├── init.py
│ │ ├── data_utils.py
│ │ ├── display_utils.py
│ │ └── style_utils.py
│ └── pages/
│ ├── init.py
│ ├── accueil.py
│ ├── filtrage.py
│ ├── resultats.py
│ └── recommandation.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Pipeline de données

Le projet suit plusieurs étapes, **du scraping au site web** :

1. **Scraping**
    - `data/raw/scraping_wines.ipynb` : Notebook qui collecte les informations des vins sur les sites marchands et les sauvegarde dans `vins_bruts_150pages.csv`.

2. **Aplatissement**
    - `data/processed/flattening.ipynb` : Nettoie les colonnes complexes et génère `vins_aplatis.csv`.

3. **Nettoyage et préparation ML**
    - `data/processed/cleaning_ml.ipynb` : Met en forme les données pour le machine learning (`vins_ml_ready.csv`).

4. **Machine Learning / Enrichissement**
    - `data/final/ml_model.ipynb` : Modélisation, enrichissement et recommandations. Génère le fichier `base_vin_final.csv` utilisé par le site.

5. **Application Streamlit**
    - Le fichier final est utilisé par le site web : interface de filtrage, recherche, affichage détaillé et recommandations.

---

## Lancement de l’application web

1. **Installation des dépendances**

```bash
pip install -r requirements.txt


#Lancement de l’application
cd app
streamlit run app.py
