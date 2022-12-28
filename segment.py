#la classe point
class point:
    #constucteur de la classe point
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    #la methode toStoring() pour la classe point 
    def __str__(self):
        return f"({self.x}, {self.y}"

#la classe segment 
class segment:
    #constructeur de la classe segment
    def __init__(self, x1=0.0, y1=0.0, x2= 0.0, y2=0.0):
        self.orig = point(x1,y1)
        self.extrem = point(x2,y2)

    #la methode toStoring() pour la classe segment
    def __str__(self):
        return f"segment de {self.orig} à {self.extrem}"
    
print("----------------------------")
#une instance de la classe point
point = point(1,4)

#L'affichage de l'instance 
print("le point", point)

print("----------------------------")

#une instance de la classe segement

segment = segment(1,2,3,4)

#l'affichage de l'instance 
print(segment)
