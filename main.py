from datascience import DataScience
import numpy as np
import pandas as pd
from pathlib import Path
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

def produits_exo():

    file = os.path.join("data", "produits.csv")
    produits = pd.read_csv(file, sep=',')
    file = os.path.join("data", "commande.csv")
    commande = pd.read_csv(file, sep=',')
    print(produits.head())
    print(commande.head())
    df = commande.groupby('id')[['nombre']].sum()
    df.reset_index(inplace=True)
    df = df.sort_values(by='nombre', ascending=False)
    print(df.iloc[0])

    df = produits.merge(df, on='id', how='left')
    print(df.head())
    df['ca'] = df['prix'] * df['nombre']
    df = df.sort_values(by='ca', ascending=True)
    print(df.iloc[0])



def notes_exo():

    file = os.path.join("data", "notes.csv")
    notes = pd.read_csv(file, sep=',')
    print(notes.head(-20))
    print(notes.drop_duplicates(['matiere']))
    df = notes.loc[notes['matiere'] == 'Mathématiques', 'note'].mean()
    print(round(df, 2))
    df = notes.groupby('nom')[['note']].mean()
    df.reset_index(inplace=True)
    print(df.keys())
    df = df.loc[df['note'] < 10, 'nom']
    print(len(df))
    df = notes.loc[((notes['matiere'] == 'Mathématiques') | (notes['matiere'] == 'Physique-Chimie')) & (
                notes['note'] >= 15), 'nom']


def loan_exo():
    tests_data_science = DataScience()
    tests_data_science.test_np5()

def loan_exo_plot():

    file = os.path.join("data", "prets_final.csv")
    prets = pd.read_csv(file)
    print(prets.head())
    print(prets.keys())
    print(prets.shape[0])

    # proportion de prêt par type de prêt.
    df1 = prets.groupby('type').size()
    df1 = df1.reset_index()
    df1.columns = ['type', 'nombre']
    print(df1)
    # plt.pie(x=df1['nombre'], labels=df1['type'], autopct='%.2f%%')
    # plt.show()

    # bénéfice mensuel réalisé en fonction du revenu du client
    df1 = prets.groupby('identifiant')[['revenu', 'benefices']].sum().reset_index()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(df1['revenu'],df1['benefices'], s=60, alpha=0.5, c='red', marker='P')
    ax.set_xlabel('revenus', fontsize=10)
    ax.set_ylabel('benefices', fontsize=10)
    ax.set_title('bénéfices mensuel réalisé en fonction du revenu du client', fontsize=12)
    # plt.show()

    # La distribution des bénéfices réalisés
    df1 = prets.groupby('ville')[['benefices']].sum().reset_index()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(x=df1['benefices'], labels=df1['ville'], autopct='%.0f%%')
    ax.set_title('distribution des bénéfices réalisés', fontsize=12)
    plt.show()

def ca_graph():
    ca = pd.read_csv('data/CA.csv')
    ca['date'] = pd.to_datetime(ca['date'])
    print(ca.head())

    plt.rcdefaults()

    rgb_color = [51, 51, 51] #color in RGB format
    rgb_decimal_1 = [x / 255.0 for x in rgb_color] #RGB color in "decimals"

    rgb_color = [41, 41, 41] #color in RGB format
    rgb_decimal_2 = [x / 255.0 for x in rgb_color] #RGB color in decimal format

    params = {'text.color': 'white', 'xtick.color': 'white', 'ytick.color': 'white', 'figure.facecolor': rgb_decimal_1,
              'axes.facecolor': rgb_decimal_2, 'font.family': 'Ink Free'}
    plt.rcParams.update(params)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(ca['date'], ca['immobilier'])
    ax.plot(ca['date'], ca['automobile'])
    ax.plot(ca['date'], ca['consommation'])


    ax.set_title("Bénéfices mensuels nets sur l'année 2021, par type de prêt", fontsize=14)
    ax.set_ylabel("Benefice net (€)")


    plt.show()


if __name__ == '__main__':
    ca_graph()
