import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_bio_by_country(df, mobile=False):
    # Filtrer uniquement les vins bio
    df_bio = df[df['bio'].notna() & (df['bio'] != '0')]
    bio_counts = df_bio['pays'].value_counts()
    top_bio = bio_counts.head(5)
    # Taille adaptée pour mobile et fond harmonisé
    if mobile:
        fig, ax = plt.subplots(figsize=(3.5, 2.5), facecolor="#f8f1e7")
    else:
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="#f8f1e7")
    ax.set_facecolor("#f8f1e7")
    sns.barplot(x=top_bio.values, y=top_bio.index, ax=ax, palette="viridis")
    ax.set_title("Top 5 des pays producteurs de vin bio", fontsize=10)
    ax.set_xlabel("Nombre de vins bio", fontsize=9)
    ax.set_ylabel("Pays", fontsize=9)
    ax.tick_params(axis='both', labelsize=8)
    for i, v in enumerate(top_bio.values):
        ax.text(v + 2, i, str(v), color='black', va='center', fontsize=8)
    plt.tight_layout(pad=0.5)
    for spine in ax.spines.values():
        spine.set_visible(False)
    st.pyplot(fig)

def plot_couleurs_et_type(df, mobile=False):
    # Filtrer les minorités (moins de 2% du total)
    couleur_counts = df['couleur'].value_counts(normalize=True)
    couleur_major = couleur_counts[couleur_counts > 0.02]
    couleur_data = df[df['couleur'].isin(couleur_major.index)]
    couleur_counts = couleur_data['couleur'].value_counts()

    type_counts = df['type_produit'].value_counts(normalize=True)
    type_major = type_counts[type_counts > 0.02]
    type_data = df[df['type_produit'].isin(type_major.index)]
    type_counts = type_data['type_produit'].value_counts()

    if mobile:
        fig, axes = plt.subplots(1, 2, figsize=(7, 2.5), facecolor="#eaf6ef")
    else:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor="#eaf6ef")
    for ax in axes:
        ax.set_facecolor("#eaf6ef")

    # Couleurs
    couleur_counts.plot(kind='pie', autopct='%1.1f%%', ax=axes[0], startangle=90, textprops={'fontsize': 8})
    axes[0].set_title("Couleurs de vin", fontsize=10)
    axes[0].set_ylabel("")
    axes[0].legend(loc='lower left', bbox_to_anchor=(0.0, -0.2), fontsize=7)
    # Type produit
    type_counts.plot(kind='pie', autopct='%1.1f%%', ax=axes[1], startangle=90, textprops={'fontsize': 8})
    axes[1].set_title("Types de produit", fontsize=10)
    axes[1].set_ylabel("")
    axes[1].legend(loc='lower left', bbox_to_anchor=(0.0, -0.2), fontsize=7)
    plt.tight_layout(pad=0.5)
    for ax in axes:
        for spine in ax.spines.values():
            spine.set_visible(False)
    st.pyplot(fig)

def plot_bio_vs_total_pays(df, mobile=False):
    # Top 5 pays producteurs de vin bio
    df_bio = df[df['bio'].notna() & (df['bio'] != '0')]
    bio_counts = df_bio['pays'].value_counts()
    top_bio = bio_counts.head(5)
    # Top 5 pays producteurs de vin (tous types)
    total_counts = df['pays'].value_counts()
    top_total = total_counts.head(5)
    # Taille adaptée pour mobile et fond harmonisé
    if mobile:
        fig, axes = plt.subplots(1, 2, figsize=(7, 2.5), facecolor="#f8f1e7")
    else:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor="#f8f1e7")
    for ax in axes:
        ax.set_facecolor("#f8f1e7")
    # Vin bio
    sns.barplot(x=top_bio.values, y=top_bio.index, ax=axes[0], palette="viridis")
    axes[0].set_title("Top 5 pays vin bio", fontsize=10)
    axes[0].set_xlabel("Nombre de vins bio", fontsize=9)
    axes[0].set_ylabel("Pays", fontsize=9)
    axes[0].tick_params(axis='both', labelsize=8)
    for i, v in enumerate(top_bio.values):
        axes[0].text(v + 2, i, str(v), color='black', va='center', fontsize=8)
    # Vin total
    sns.barplot(x=top_total.values, y=top_total.index, ax=axes[1], palette="Blues")
    axes[1].set_title("Top 5 pays tous vins", fontsize=10)
    axes[1].set_xlabel("Nombre de vins", fontsize=9)
    axes[1].set_ylabel("")
    axes[1].tick_params(axis='both', labelsize=8)
    for i, v in enumerate(top_total.values):
        axes[1].text(v + 2, i, str(v), color='black', va='center', fontsize=8)
    plt.tight_layout(pad=0.5)
    for ax in axes:
        for spine in ax.spines.values():
            spine.set_visible(False)
    st.pyplot(fig)
