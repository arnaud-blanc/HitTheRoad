import streamlit as st
import table
import pandas as pd


title = "Hit The Road"
sidebar_name = "Contexte & Data"



# Import des premières données des tables 
caracteristiques_head = pd.read_csv("../data/caracteristiques_head.csv")
lieux_head = pd.read_csv("../data/lieux_head.csv")
usagers_head = pd.read_csv("../data/usagers_head.csv")
vehicules_head = pd.read_csv("../data/vehicules_head.csv")

def run():

  st.image("assets/Hit the Road mini.gif")
  
  st.title(title)

  st.markdown("---")
  
  st.markdown("## Contexte")

  st.markdown(
      """
      Le projet Hit The Road consiste à prédire la gravité des accidents de la route en France. Dans cette analyse, un accident est considéré comme grave si au moins une des personnes impliquées est blessée, hospitalisée ou tuée. 
      Les données utilisées sont issues du site gouvernemental [data.gouv.fr](https://www.data.gouv.fr/en/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/), et produites par le [Ministère de l'Intérieur et des Outre-Mer](https://www.data.gouv.fr/en/organizations/ministere-de-linterieur-et-des-outre-mer/) et proviennent des bases de données annuelles des accidents corporels de la circulation routière.

      """
  )
  
  st.markdown("---")
  st.markdown("## Data")
  
  st.markdown(
      """
      Les premières lignes des fichiers de l'année 2021 sont présentées ci-dessous pour exemple.
      """
  )

  file_name = st.radio("Fichiers", ["Caractéristiques", "Lieux", "Véhicules", "Usagers"], 0, label_visibility = 'collapsed')
  
  if file_name == "Caractéristiques":
      st.write(caracteristiques_head)
  elif file_name == "Lieux":
      st.write(lieux_head)
  elif file_name == "Usagers":
      st.write(usagers_head)
  elif file_name == "Véhicules":
      st.write(vehicules_head)
      


  

  with st.expander(label="variables employées dans les modèles"):
    tab1, tab2 = st.tabs(["variables par importance décroissante", "définitions des variables"])
    with tab1:
      st.table(table.df)
    with tab2:
      st.table(table.df2)
      
      
  col1, col2 = st.columns([10, 1])
  
  with col1:
    st.info("Télécharger la description des bases de données annuelles des accidents corporels de la circulation routière :", icon="ℹ️")
  
  with col2:
    with open("assets/description-des-bases-de-donnees-onisr-annees-2005-a-2020.pdf", "rb") as file:
      btn=st.download_button(
      label=":arrow_down:",
      data=file,
      file_name="description-des-bases-de-donnees-onisr-annees-2005-a-2020.pdf",
      mime="application/octet-stream"
  )
  st.markdown("---")
    