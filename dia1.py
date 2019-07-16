#operacion aritmetica

print(2+2)
print(2/2)
print(30/5)
print(4*4)
#lo siguiente es una concatenacion de strings

print("hola mundo")
#imprimir un texto  4 veces
print("hola"*4)
print("hola"+"que tal")
#variables las variables son cajas donde se pueden cargar numeros letras etc
a=2
b=4
print(a*b)
c="nora"
d=5
print(c*d)
print(c,d)
print("hola","que tal")#la coma sirve para separar

#ej.crear una variable nombre y una variables edad
#con sus nombres y edades y despues imprimir
nombre="Nora"
edad="23anhos"
print("mi nombre es",nombre,"tengo",edad,)
#ej.1 crear una variable hobby con tu pasatiempo
#e imprimir
hobby="leer libros"
print("mi nombre es",nombre,"tengo",edad,"y mi hobby es",hobby)
#listas
listax=[1,2,3,4,5]
print(listax)
#crear una lista datos que en el primer lugar este tu nombre
#y en la segunda posicion este tu edad.
#imprimir "hola me llamo...y tengo...anhos"
Datos=["nora",23]
print("hola mi nombre es",Datos[0],"y tengo",Datos[1],"anhos")
Datos[1]=25#Sirve para modificar un elemento de la lista segun la posicion que ocupa
print("hola mi nombre es",Datos[0],"y tengo",Datos[1],"anhos")
#Ej.Agregar una profesion y un hobby a la lista datos
#previamente creada(usar append())
Datos.append("comerciante")#sirve para agregar elementos a una lista
print(Datos)
Datos.append("bailar")
print(Datos)
print("mi nombre es",Datos[0],"tengo",Datos[1],"soy",Datos[2],"y mi hobby es", Datos[3])
Datos.pop()#sirve para eliminar elementos 
print(Datos)
#funcion len()
#EJ. Obtener la dimension de la lista datos e imprimir:
#"la lista datos tiene... elementos"
print(len(Datos))#sirve para calcular la cantidad de elementos o dimension
print("la lista datos tiene",len(Datos),"elementos")
#ej.imprimir el ultimo elemento de una lista sin saber,
#cuantos elementos tiene,pista usar len()
lista_b=[1,2,3,4,5,5,6,7,10,20,30,40,50,40,90,80,100,200,89]
print(len(lista_b))
print(len(lista_b)-1)
print(lista_b[len(lista_b)-1])

#bucles/ciclos/interacciones
listas_temas=["variables","listas","tipos de datos"]
for concepto in listas_temas:
    print("hoy aprendi",concepto)
#recorrer una lista e imprimir en cada ciclo
#el valor del elemento con 3 signos de admiracion
#ingrese fuera de bucle "fin!!!"
for concepto in listas_temas:
    print(concepto,"!!!")
print("fin!!!")
ejemplo=["juana","jose","jorge"]
for amigos in ejemplo:
    print(amigos,"!!!")
print("fin!!!")
for x in range(4):
    print("hola")
    print("hola",x)
    #ej1 imprimir los numeros de 1 al 100 usando for
    #y range
    #ej2 imprimir el resultado de la suma de los numeros 
    #del 1 al 10
    for x in range(1,101):
        print( x )
    lista_a=[1,2,3,4,5,6,7,8,9,10]
    suma=0
    for i in lista_a:
        suma=suma+i
    print(suma)
    cobro=[426714,250000]
    suma=0
    for t in cobro:
        suma=suma+t
    print(suma)
#funciones
#def nombre_de_la_funcion():
def suma(num1,num2):
    resultado=num1+num2
    return resultado
#equivalente a lo de arriba
def suma2(num1,num2):
    return num1+num2

print(suma(5,10))
resul=suma(5,8)
print(resul)
# crear una funcion resta, que reciba como parametro dos numeros
#y retorno la resta de esos numeros
#luego llamar a la funcion e imprimir el resultado

#crear una funcion saludo2 que reciba como parametro nombre edad
#e imprimir "hola soy... y tengo...anhos"
#llamar varia veces a la funcion con distintos valores
#nota:retornar algo es opcional

def resta(n1,n2):
    return n1-n2
x=resta(4,2)
print(x)
print(resta(8,2))

def saludo2(nombre,edad):
    print("hola soy",nombre,"y tengo",edad,"anhos")
saludo2("nora",23)
saludo2("juan",33)
saludo2("thiago",45)

#Ej. crear una funcion suma_lista que reciba como argumento una lista de numero
#y retorne la suma de sus elementos
# pista: usar for y una variable acumulador

def suma_lista (lista_b):

    suma=0

    for x in lista_b:

        suma=suma+x

    return suma

listita=[1,2,3,4,5]


i=(suma_lista(listita))

print(i)

listota[100,5,5]

c=(suma_lista(listota))

print(c)





#ej.: eliminar todos los elementos de una lista utilizando "for"

#grupo5=["N","F1","F2","A"]



#Crear una funcion suma_cuadrado que reciba una lista de numeros
#y retorne el valor de la suma de cada numero al cuadrado
#[1,2,3,4].....1+4+9+16...30
datos=[1,2,3,4]
def suma_cuadrado (list_M):
    suma=0
    for x in list_M:
        suma=suma + (x*x)
    return suma
print(suma_cuadrado(datos))
    














    
    






