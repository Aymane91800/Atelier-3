#class rectangle

class rectangle:
    #constructeur de la classe rectangle 
    def __init__(self, longueur, largeur):
        self.name = "rectangle"
        self.longueur = longueur
        self.largeur = largeur

    #la methode de la surface 
    def surface(self):
        return self.longueur * self.largeur

    #la methode afficher
    def afficher(self):
        print ("{" + self.name +" , longueur: " + str(self.longueur) + " , largeur:" + str(self.largeur) + "}")

#la classe hérité de la classe rectangle 
class carre(rectangle):

    #constructeur de la classe carré
    def __init__(self, longueur):
        # constructeur de la classe parent
        super().__init__(longueur, longueur)
        self.name = "carré"

    #la méthode afficher (polymorphisme)
    def afficher(self):
        print("{" + self.name +", longueur: "+ str(self.longueur) + "}")

print("-------------------------------------")

# une instance de la classe rectangle

rect = rectangle(13,15)
rect.afficher()
print(rect.surface())
print("-------------------------------------")
 # une instance de la classe carré 
Carré= carre(16)
Carré.afficher()
print(Carré.surface())