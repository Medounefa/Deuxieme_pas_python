
# classe mere
class Vehicule:

    def __init__(self, nom_voiture, quantite_essence) -> None:
        self.nom = nom_voiture
        self.quantite = quantite_essence
    
    def se_deplacer(self) :
        print("La vehicule {} se deplace......".format(self.nom))
    
    
# classe fille
class Voiture(Vehicule):
    def __init__(self, nom_vehicule, essence, puissance) -> None:
        Vehicule.__init__(self, nom_vehicule, essence)
        self.puissance = puissance
    def se_deplacer(self):
        print("Je roule........")

class Avion(Vehicule) :
    def __init__(self, nom, essence, marchandise) -> None:
      Vehicule.__init__(self, nom,essence) 
      self.marchandise = marchandise
    def se_deplacer(self):
        print("Je survole sur les airs")

# Programme principlae
voiture1 = Voiture("Toyota Supra", 90, 420)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")

Av1 = Avion("F22 Raptor", 2400, "Missiles")
Av1.se_deplacer()

