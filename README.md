# BouteillIA — Plateforme de recommandation de vins

Bienvenue sur **BouteillIA**, une application web de data science dédiée à la découverte, l'exploration et la recommandation intelligente de vins.

---

## Table des matières

- [Présentation du projet](#présentation-du-projet)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Arborescence du projet](#arborescence-du-projet)
- [Pipeline de données](#pipeline-de-données)
- [Lancement de l'application web](#lancement-de-lapplication-web)
- [Dépendances](#dépendances)
- [Contribuer](#contribuer)

---

## Présentation du projet

**BouteillIA** vise à offrir une expérience complète autour du vin :
- Collecte et centralisation de données sur des milliers de vins (scraping, enrichissement),
- Nettoyage, structuration et préparation des données pour l'analyse et la recommandation,
- Application de modèles de machine learning pour suggérer des vins adaptés aux goûts et critères de l'utilisateur,
- Interface web moderne, responsive et intuitive pour explorer, filtrer, visualiser et obtenir des recommandations personnalisées.

---

## Fonctionnalités principales

- **Accueil** :
  - Statistiques clés sur le marché du vin (bio, consommation, etc.)
  - Visualisations interactives : top pays producteurs de vin bio, répartition des couleurs, types de produits…
- **Votre choix** :
  - Recherche multi-critères (nom, pays, couleur, prix, accords mets-vins, bio…)
  - Sélection dynamique des fourchettes de prix et des accords
- **Résultats détaillés** :
  - Affichage des vins correspondant à la recherche, avec visuels, infos détaillées, badges bio
  - Affichage des images locales uniquement (dossier `data/final/images/`)
  - Accès rapide aux recommandations personnalisées pour chaque vin
- **Recommandation IA** :
  - Suggestions de vins similaires ou complémentaires, basées sur l'analyse des profils et des préférences
- **Design responsive** :
  - Expérience optimisée pour desktop et mobile (graphiques adaptés, navigation fluide)

---

## Arborescence du projet

```
SITEVINS/
├── app/
│   ├── app.py
│   ├── images/
│   │   ├── logo.png
│   │   └── imagecentre.png
│   ├── pages/
│   │   ├── accueil.py
│   │   ├── filtrage.py
│   │   ├── resultats.py
│   │   └── recommandation.py
│   └── utils/
│       ├── data_utils.py
│       ├── display_utils.py
│       ├── style_utils.py
│       └── visualisation.py
├── data/
│   ├── raw/
│   │   ├── scrapping.ipynb
│   │   ├── scrappingimages.ipynb
│   │   └── vins_vinatis_150_pages.csv
│   ├── process/
│   │   ├── etape_1_pour_applatir.ipynb
│   │   ├── etape_2_travail_sur_base.ipynb

│   │   └── vins_vinatis_flat_complet.csv
│   └── final/
│       ├── etape_3_ML_sur_base_vin_av_poids.ipynb
│       ├── consol_pourcsv.ipynb
│       ├── base_vin_final.csv
│       ├── base_vin_final_temps.csv
│       ├── concept_fichier final.ipynb
│       ├── URLimages.csv
│       └── images/        # images de bouteilles (scrapping local)
│           ├── 04439.png
│           ├── 04438.png
│           ├── ...
│           └── 04340.png
├── requirement.txt
├── .gitignore
└── README.md
```

---

## Pipeline de données

1. **Scraping**
    - `data/raw/scrapping.ipynb` : collecte des données sur les vins (site Vinatis, etc.)
2. **Scraping des images**
    - `data/raw/scrappingimages.ipynb` : récupération automatique des images de bouteilles de vin à partir des URLs collectées lors du scraping principal. Les images sont téléchargées et stockées localement dans le dossier `data/final/images/`.
    - Ces images sont ensuite utilisées par l'application web pour illustrer les résultats et recommandations, garantissant un affichage rapide et sans dépendance à des ressources externes.
3. **Préparation & nettoyage**
    - `data/process/etape_1_pour_applatir.ipynb`, `etape_2_travail_sur_base.ipynb` : nettoyage, aplatissement, enrichissement
4. **Machine Learning & enrichissement**
    - `data/final/etape_3_ML_sur_base_vin_av_poids.ipynb` : modélisation, scoring, génération de la base finale
5. **Application web**
    - Utilisation de `data/final/base_vin_final.csv` pour alimenter l'interface Streamlit
    - Les images sont recherchées uniquement en local dans `data/final/images/`

---

## Lancement de l'application web

1. **Installer les dépendances**

```bash
pip install -r requirement.txt
```

2. **Lancer l'application**

```bash
python -m streamlit run app/app.py
```

3. **Accéder à l'interface**

Ouvrez votre navigateur à l'adresse indiquée (par défaut http://localhost:8501)

---

## Dépendances principales

- pandas
- numpy
- streamlit
- scikit-learn
- requests
- Pillow
- jupyter
- beautifulsoup4
- matplotlib
- seaborn

---

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour proposer des améliorations, corriger des bugs ou enrichir la base de données.

---

## Auteurs

- Projet initié et développé par l'équipe BouteillIA.
- Contact : Yann, Jean & Michel 
