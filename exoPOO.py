from datetime import date

class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse

    def __str__(self):
        return f"Client: {self.nom}, {self.adresse}"

    def contacter(self):
        print(f"Contacter le client {self.nom} à l'adresse {self.adresse}")


class Commande:
    num_commande = 0

    def __init__(self, client, produits, prix = 0):
        self.client = client
        self.produits = produits
        self.prix = prix
        Commande.num_commande += 1
        self.num = Commande.num_commande

    def get_client(self):
        return self.client

    def set_client(self, client):
        self.client = client

    def get_produits(self):
        return self.produits

    def set_produits(self, produits):
        self.produits = produits

    def get_prix(self):
        return self.prix

    def set_prix(self, prix):
        self.prix = prix

    def calculTVA(self):
        return self.prix * 0.196

    def __str__(self):
        return f"Commande n°{self.num}\n{self.client}\nProduits: {', '.join(self.produits)}\nPrix: {self.prix} €\n\n"

    def __add__(self, autre_commande):
        num = max(self.num, autre_commande.num) + 1
        produits = self.produits + autre_commande.produits
        prix = self.prix + autre_commande.prix
        return Commande(self.client, produits, prix)

class CommandeAcquittee(Commande):
    def __init__(self, client, produits, prix = 0, date_paiement = date.today()):
        super().__init__(client, produits, prix, date_paiement)
        self.date_paiement = date_paiement

    def acquitter(self):
        return CommandeAcquittee(self.client, self.produits, self.prix)


client1 = Client("Alice", "1 rue des Fleurs")
client2 = Client("Bob", "2 rue des Arbres")

commande1 = Commande(client1, ["pain", "lait", "beurre"], 10.50)
commande2 = Commande(client2, ["pâtes", "sauce tomate"], 7.20)

# print(commande1)
# print(commande2)

commande3 = commande1 + commande2
print(commande3)

commande4 = CommandeAcquittee(client1, ["croissants", "café"], 5.60, "2020-12-25")
commande4.acquitter()
print(client1.contacter())