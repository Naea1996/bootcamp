#tipo de dato string/cadena str de texto
"esto es un string"
#tipo de dato Integer/entero/int
105
#listas
[]#lista vacia
["marce",33,"programador"]#lista de 3 elementoy
#variables
nombre="Marce"
edad=30+3
edad_mal="30+3"

otra_lista=[5,"hola que tal","chau",4]
otra_lista.append("AAAA")
#solucion paso a paso
dim_lista=len(otra_lista)
print("la dimension  de otra_lista es",dim_lista)
indice_del_ultimo=dim_lista-1
print("el indice del ltimo elemento es",indice_del_ultimo)
print(otra_lista[indice_del_ultimo])

#solucion de una linea
print(otra_lista[len(otra_lista)-1])

list_numeros=[1,2,3,4]

def suma_cuadrado(list_n):
    suma=0
    for p in list_n:
        suma=suma+(p*p)
    return suma
print(suma_cuadrado(list_numeros))

