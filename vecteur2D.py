#exercice1

class vecteur2D:
    #constructeur de la classe Vecteur2D 
    def __init__(self, x=0 , y=0):
         self.x = x
         self.y = y

     # La methode toString() pour python 
    def __str__(self):
        return f"({self.x}, {self.y})"

    # la methode afficher()
    def afficher(self):
        return"(" + str(self.x) + ", "+ str(self.y) +")" 

    #Methode de surcharge d'addition de deux vecteurs du plan
    def __add__(self, vecteur2D):
        return vecteur2D(self.x + vecteur2D.x, self.y + vecteur2D.y)


#Un vecteur 2D sans parametre
vect1 = vecteur2D()

# un vecteur 2D avec ses deux parametres 
vect2 = vecteur2D(2,4)

# affichage des vecteurs comme tuple
print(vect1)
print(vect2)

#Affichage  des vecteursavec la méthode afficher()
print(vect1.afficher())

#ma somme de deux vecteurs du plan 
vect3 = vect1 + vect2

#l'affichage de la somme de deux vecteurs du plan 

print(vect3.afficher())




#instanciation d'un vecteur2D sans paramètre
vecteur1 = vecteur2D()
print(vecteur1.x, vecteur1.y)


#instanciation d'un vecteur2D avec ses 2 paramètres

vecteur2 = vecteur2D(3,4)
print(vecteur2.x ,vecteur2.y)
print(vecteur1, vecteur2)