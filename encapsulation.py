class Humain :
    """ Cette classe represente un humain"""
    def __init__(self, nom, age) -> None:
        print("Creation humain...............")
        self.nom = nom
        self._age = age
    def _getage(self) :
        try :
            return self._age
        except AttributeError:
                print("age n existe pas")
    def _setage(self, nouvelle_age) :
        if nouvelle_age < 0 :
           self._age = 0
        else :
          self._age = nouvelle_age
    def _delage(self) :
        del self._age

    age = property(_getage, _setage, _delage, "Je suis l'age de l'humain")

h1 = Humain("Medoune", 23)

help(Humain.age)

# print(h1.age)
# del h1.age  
# print(h1.age)

