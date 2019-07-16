
class Persona:

    edad=0


    def __init__(self, un_nombre):  #es un metodo para crear las propiedades del objeto 

        self.mi_nombre= un_nombre   #self hace referencia al objeto en si y le asignamos un nombre al objeto
        print("hola naci, me llamo", self.mi_nombre) #imprimimos hola naci, me llamo 

    def cumple(self):               #creamos una funcion para agregarle un cumpleanhos al objeto(persona)
        self.edad = self.edad +1    #creamos una ecuacion para que nuestro objeto(persona) cumpla 1 anho
   

pepe= Persona("pepito")             #damos el nombre a nuestro objeto(persona)
pepa= Persona("pepita")
print(pepe.edad)                    #imprimimos el nombre y la edad de nuestro objeto(persona)
print(pepe.mi_nombre)

pepe.cumple()                       
print(pepe.edad)







