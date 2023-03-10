class AB:
    def __init__(self, racine = None, gauche=None, droite=None):
        self.racine = [racine]
        self.gauche = gauche
        self.droite = droite

    def estVide(self):
        return self.racine is None

    def taille(self):
        if self.estVide():
            return 0
        else:
            return 1 + (self.gauche.taille() if self.gauche is not None else 0) + \
                (self.droite.taille() if self.droite is not None else 0)

    def prefixe(self):
        print(self.racine) if self.racine is not None else print("")
        self.gauche.prefixe() if self.gauche is not None else print("")           
        self.droite.prefixe() if self.droite is not None else print("")           
        

    def __str__(self) -> str:
        return str(self.racine) + " " + str(self.gauche) + " " + str(self.droite)

    def infixe(self):
        if self.estVide():
            return "Vide"
        else:
            result = []
            if self.gauche is not None:
                result += self.gauche.infixe()
            result += [self.racine[0]]
            if self.droite is not None:
                result += self.droite.infixe()
            return result

    def postfixe(self):
        if self.estVide():
            return "Vide"
        else:
            result = []
            if self.gauche is not None:
                result += self.gauche.postfixe()
            if self.droite is not None:
                result += self.droite.postfixe()
            result += [self.racine[0]]
            return result

    def hauteur(self):
        if self.estVide():
            return 0
        else:
            hauteur_gauche = self.gauche.hauteur() if self.gauche else 0
            hauteur_droite = self.droite.hauteur() if self.droite else 0
            return 1 + max(hauteur_gauche, hauteur_droite)

    def estABR(self):
        if self.estVide():
            return False
        elif self.gauche is None and self.droite is None:
            return False
        elif self.gauche is None:
            return self.droite.estABR() and self.racine[0] < self.droite.racine[0]
        elif self.droite is None:
            return self.gauche.estABR() and self.racine[0] > self.gauche.racine[0]
        else:
            return self.gauche.estABR() and self.droite.estABR() and self.racine[0] > self.gauche.max() and self.racine[0] < self.droite.min()

    def max(self):
        if self.droite is None:
            return self.racine[0]
        else:
            return self.droite.max()

    def min(self):
        if self.gauche is None:
            return self.racine[0]
        else:
            return self.gauche.min()
        
    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            delta = 0
            gauche = self.gauche.hauteur() if self.gauche is not None else -1
            droite = self.droite.hauteur() if self.droite is not None else -1
            delta = gauche - droite
            if delta > 1 or delta < -1:
                return False
            else:
                gauche = self.gauche.estEquilibre() if self.gauche is not None else True
                droite = self.droite.estEquilibre() if self.droite is not None else True
                return True and gauche and droite
            
A1 = AB()
A2 = AB(5)
A3 = AB(3)
A2.gauche = A3

# print(A2)

Atest = AB(10, AB(5, AB(3), AB(8)), AB(12))

# print("A1 est vide ? ", A1.estVide())
# print("A2 est vide ? ", A2.estVide())
# print("A3 est vide ? ", A3.estVide())
# print("Atest est vide ? ", Atest.estVide())

# print("Taille de Atest : ", Atest.taille())

A = AB(4, AB(2, AB(1), AB(3)), AB(6, AB(5), AB(7)))
A3 = AB(4, AB(2, AB(1), AB(5)), AB(6, AB(5), AB(7)))

A = AB(13, AB(2, AB(4), AB(5)), AB(3, AB(6), AB(7)))

print(Atest.prefixe())
# print(A.estEquilibre())  # True

# print(A.estABR())
# print(A2.estABR())
# print(A.infixe())
