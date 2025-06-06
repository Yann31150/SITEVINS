import pandas as pd

def charger_donnees(fichier_csv="base_vin_final.csv"):
    """Charge les données des vins depuis un CSV et les prépare."""
    df = pd.read_csv(fichier_csv)
    df['bio'] = df['bio'].apply(lambda x: 1 if pd.notna(x) and 'Certifié Eurofeuille' in str(x) else 0)
    if 'visuel' not in df.columns:
        df['visuel'] = "https://www.vinatis.com/1-detail_default/default-wine.png"
    else:
        df['visuel'] = df['visuel'].apply(
            lambda x: f"https://www.vinatis.com/{x}" if pd.notna(x) and not str(x).startswith('http') else x
        )
    for col in df.columns:
        if col != 'prix':
            df[col] = df[col].astype(str)
    df['prix'] = pd.to_numeric(df['prix'], errors='coerce')
    return df

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
