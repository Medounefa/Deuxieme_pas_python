
"""
Fonction utile

   isinstance (<objet> <classe>) : verifie qu'un objet est de la classe renseigne
   issubclass(<classe_fille> <classe_mere>) : verifie qu' une classe est fille d'une autre
"""

class Animal :
    def __init__(self, nom) :
        self.nom = nom

    def manger(self):
        print(self.nom, "mange......")


class Reptile (Animal) :
    def __init__(self, nomR, regime_alimentaire) :
        Animal.__init__(self, nomR)
        self.regime = regime_alimentaire

    def manger(self):
        print("Le reptile mange....")

# code principale

lezard = Reptile("Lezard", "grenouille")
# print(isinstance(lezard, Animal))
# lezard.manger()

# if(isinstance(lezard, Reptile)) :
#     print("Lezard est un animal")

if(issubclass(Reptile ,Animal)) :
    print("Reptile Herite Animal")





































# # classe mere 1

# class objetJeu :
#     pass

# # classe mere

# class Arme :
#     pass

# # classe fille

# class Fusil(objetJeu, Arme) :
#     pass

# # ============================================================================

# class Etudiant :
#     pass

# class Enseignant :
#     pass

# class Doctorant(Etudiant, Enseignant) :
#     pass