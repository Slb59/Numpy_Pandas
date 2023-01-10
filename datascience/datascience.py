import numpy as np
import pandas as pd


class DataScience:
    """ Exercices issus de la formation OCR
    https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science
    """

    def __init__(self):
        loan_url = 'https://raw.githubusercontent.com/benjaminmrl/data-4452741/main/prets.csv'
        self.loan_df = pd.read_csv(loan_url)
        self.max_rate = 35

        client1_url = 'https://raw.githubusercontent.com/benjaminmrl/data-4452741/main/clients.csv'
        self.clients_1 = pd.read_csv(client1_url)
        client2_url = 'https://raw.githubusercontent.com/benjaminmrl/data-4452741/main/clients_suite.csv'
        self.clients_2 = pd.read_csv(client2_url)

        self.init_df()

    def test_np5(self):
        pass

    def test_np4(self):
        print(self.loan_df.keys())
        profil_client = \
            self.loan_df.groupby('identifiant')[
                ['remboursement', 'taux_endettement', 'cout_total', 'benefices']].sum()
        profil_client.reset_index(inplace=True)
        print(profil_client.head())

        profil_client['risque'] = 'Non'
        profil_client.loc[profil_client['taux_endettement'] > self.max_rate, 'risque'] = 'Oui'
        client_risque = profil_client.loc[profil_client['risque'] == 'Oui', :]

        nb = client_risque.shape[0]
        print('Il y a', nb, 'clients qui ont dépassé le seuil autorisé')

        # benefices par agence
        profits = self.loan_df.groupby(['ville', 'type'])['benefices'].sum()
        print(profits)

        # bénéfices moyen réalisés par chaque agence, pour chaque type de prêt
        profits = self.loan_df.pivot_table(index='ville', columns='type', values='benefices', aggfunc='mean')
        print(profits)

    def init_df(self):

        # renommer taux en taux_interet
        self.loan_df.rename(columns={'taux': 'taux_interet'}, inplace=True)

        # calcul du taux d'endettement
        self.loan_df['taux_endettement'] = round(self.loan_df['remboursement'] / (self.loan_df['revenu']) * 100, 2)

        # calculer le cout total du pret
        self.loan_df['cout_total'] = self.loan_df['remboursement'] * self.loan_df['duree']

        # calculer les bénéfices mensuels réalisés
        self.loan_df['benefices'] = round(self.loan_df['cout_total'] * self.loan_df['taux_interet'] / 24 / 100, 2)

        self.loan_df['risque'] = 'Non'
        self.loan_df.loc[self.loan_df['taux_endettement'] > self.max_rate, 'risque'] = 'Oui'

        # dataframe de profils clients
        self.profil_clients = self.loan_df.groupby('identifiant')[
            ['remboursement', 'taux_endettement', 'cout_total', 'benefices']].sum()
        self.profil_clients.reset_index(inplace=True)


    def tests_np3(self):


        self.loan_df = self.loan_df.sort_values('benefices', ascending=False)

        # nombre de personnes ayant dépassé le taux max de 35%
        clients_risque = self.loan_df.loc[self.loan_df['taux_endettement'] > self.max_rate, :]
        print(clients_risque)
        nb = clients_risque.shape[0]
        print(len(clients_risque))
        print('Il y a', nb, 'clients qui ont dépassé le seuil autorisé')

        clients_risque_paris = self.loan_df.loc[
            (self.loan_df['taux_endettement'] > self.max_rate) & (self.loan_df['ville'] == 'PARIS')]
        print(clients_risque_paris)
        print(clients_risque_paris.shape[0])

        # Combien de prêts automobiles ont été accordés
        prets_automobile = self.loan_df.loc[self.loan_df['type'] == 'automobile', :]
        print(prets_automobile.shape[0])
        print(prets_automobile.head())

        # Quel est le coût total moyen de ces derniers
        mask = self.loan_df['type'] == 'automobile'
        print('coût total moyen: ' + str(self.loan_df.loc[mask, 'cout_total'].mean()))

        # bénéfice mensuel total réalisé par l’agence Toulousaine
        print(self.loan_df.keys())
        # benefices_toutlouse =
        print("bénéfice mensuel total réalisé par l’agence Toulousaine: " +
              str(self.loan_df.loc[self.loan_df['ville'] == 'TOULOUSE', 'benefices'].sum()))

    def tests_np2(self):
        data = np.arange(7)
        print(data)

        a = np.linspace(5, 10, 11)
        print(a)
        print(a[-3:-1])

        b = np.array([
            [[1, 2], [4, 5]],
            [[6, 7], [8, 9]],
            [[10, 11], [12, 13]]])
        print(b)

    def tests_np(self):
        hugo = [1800, 21, 0]
        richard = [1500, 54, 2]
        emilie = [2200, 28, 3]
        pierre = [3000, 37, 1]
        paul = [2172, 37, 2]
        deborah = [5000, 32, 0]
        yohann = [1400, 23, 0]
        anne = [1200, 25, 1]
        thibault = [1100, 19, 0]
        emmanuel = [1300, 31, 2]

        tableau = [hugo, richard, emilie, pierre, paul, deborah,
                   yohann, anne, thibault, emmanuel]

        print(tableau)
        data = np.array(tableau)
        print(data[4, :])
        m = data[4, 0] * 35 / 100
        print(m)

        louise = [1900, 31, 1]
        data = np.vstack((data, louise))
        print(data)

        revenus = data[:, 0]
        print(revenus)