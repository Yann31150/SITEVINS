# 🍷 BouteillIA - Plateforme de recommandation de vins

Bienvenue sur **BouteillIA**, une application web interactive qui vous accompagne dans la découverte et la recommandation de vins grâce à l’intelligence artificielle et la data science.

## 🚀 Fonctionnalités

- **Exploration détaillée du catalogue** : Consultez des fiches vins complètes avec image, description, accords mets & vins, etc.
- **Filtrage multicritères** : Trouvez le vin idéal selon le nom, le pays, la couleur, le prix, les accords culinaires ou le label bio.
- **Recommandations personnalisées** : Recevez des suggestions de vins similaires selon vos choix.
- **KPI et visualisations** : Statistiques rapides sur la diversité de la base.

## 📁 Structure du projet

/ton_projet/
│
├── app.py
├── base_vin_final.csv
├── utils/
│     ├── __init__.py
│     ├── data_utils.py
│     ├── display_utils.py
│     └── style_utils.py
├── pages/
│     ├── __init__.py
│     ├── accueil.py
│     ├── filtrage.py
│     ├── resultats.py
│     └── recommandation.py
└── ...


## ⚙️ Prérequis

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- pandas
- pillow (PIL)
- requests

Pour installer les dépendances nécessaires :

```bash
pip install streamlit pandas pillow requests

#Lancement de l’application
#Placez votre base de données dans le fichier base_vin_final.csv à la racine du projet.



#Dans un terminal, exécutez :

streamlit run app.py
