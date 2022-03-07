
class Humain :

    lieu_habitation = "Terre"

    def __init__(self, nom, age) -> None: #METHODE STANDARD
        """ classe qui definit un humain """
        self.nom = nom
        self.age = age
    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message)) 
    
    def changer_planete(cls, nouvelle_planete) : #methode de classe
        Humain.lieu_habitation = nouvelle_planete
    changer_planete = classmethod(changer_planete)

    def definition() :
        print("L'humain est un .................")
    definition =staticmethod(definition)

# Programme pricinpale
Humain.definition()

# h1 = Humain("Medoune", 23)

# print("Planette actuelle : {}".format(Humain.lieu_habitation))
# Humain.changer_planete("Mars") 
# print("Planette actuelle : {}".format(Humain.lieu_habitation))