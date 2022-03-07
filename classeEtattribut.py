
class Humain :
    """
    classe des etres humain
    """

    humains_crees = 0
    def __init__(self, c_prenom, c_age) -> None:
        print("Creation d'objet.............")
        self.prenom = c_prenom
        self.age = c_age
        Humain.humains_crees +=1
    # def __init__(self) -> None:
    #     print("Creation d'objet.............")
    #     self.prenom = "Medoune"
    #     self.age = 23


print("Lancement du programme..............")

h1 = Humain("Medoune", 23)
print("Prenom de h1->{}".format(h1.prenom))
print("Age de h1->{}".format(h1.age))
print("Humain cree->{}".format(Humain.humains_crees))

# h1.prenom = "Thomas"
# print("Prenom de h1->{}".format(h1.prenom))

h2 = Humain("Albert", 17)
print("Prenom de h2->{}".format(h2.prenom))
print("Age de h2->{}".format(h2.age))
print("Humain cree->{}".format(Humain.humains_crees))