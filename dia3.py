# utilidad de for dentro de def

ing_pan=["harina","levadura","sal","azucar","agua"]

def imprimir_lista(ingredientes):

    for producto in ingredientes:

        print(producto)
imprimir_lista(ing_pan)

###########CONDICIONALES########
#== igual
#>mayor que
#<menor que
#>= mayor o igual
#<=menor o igual que
#!= distinto o no igual

a=3

#pregunta 1...if 

if a>3:

    print("si,a es mayor a 3")
    print("chau!")
else:
    print("no, a no es mayor a 3")
#pregunta 2
if a==3:
    print("a es igual a 3")

nota=60
#pregunta  3
if nota>= 60:
    print("pasate!!")
else:
    print("hule ya")

    #Ej. crear una funcion que reciba como parametro una
    #nota de 1 al 100 e imprimir si pasaste o te aplazte
 
def proceso(noti):

    if noti>= 61:
         print("pasaste")

    else:
        print("no pasaste")

proceso(67)
proceso(59)

#######el uso de and para unir 2condiciones
a=11
if a>5 and a<10:
    print("a es mayor a 5 y menor que 10")
else:
    print("a no esta en el rango, alguna de las 2 condiciones no se cumplieron")

    #el uso de or para validar una de las condiciones que se cumpla

#if a>5 or a<10:




    

#el uso de elif

Edad = 7

if Edad>18:
    print("universidad")
elif Edad>13:
    print("secundaria")
elif Edad>6:
    print("primaria")
else:
    print("bbdlc")

#Ej. crear una funcion puntaje que reciba como parametro una nota
#del 1 al 100 e imprima que nota sacaste
#nota<60.....1
#nota entre 60 y 70....2
#nota entre 71 y 75....3
#nota entre 76 y 85.....4
#nota mayor que 85......5

def puntaje(nt):
    if nt<60:
        print(1)
    elif nt>=60 and nt<=70:
        print(2)
    elif nt>=71 and nt <=75:
        print(3)
    elif nt>= 76 and nt<=85:
        print(4)
    elif nt>85:
        print(5)
puntaje(73)
    

#true false



#EJ. Pedir al usuario que ingrese tres numeros y multiplicarlos entre si,
#imprimir el resultado

mult=input("ingrese el primer numero:")
mult2=input("ingrese el segundo numero:")
mult3=input("ingrese el tercer numero:")
print(int(mult)*int(mult2)*int(mult3))
#eje.2 pedir al usuario un numero del 1 al 100 y llamar a la
#funcion que retornaba la nota que creamos hace un rato
#utilizando el valor ingresado por el usuario
us=int(input("ingresar un numero de 1 al 100:"))
puntaje(us)

#bucle while== MIENTRAS SE CUMPLA UNA CONDICION 
#x=74956
#while x!=5:  #mientras x sea distinto de 5 hacer lo siguiente
    #print("esto es un bucle while,se va a ejecutar mientras x sea distinto de 5")
    #x=int(input("ingresa un numero:"))  #ingresamos un valor para x
    #print("el valor de x ahora es",x)
#print("termino!!!")















#usando while pedir al usuario 5 ingredientes para hacer una pizza
#y agregar a una lista, al final imprimir la lista

conta=0
ing_lista2=[]
while conta<5:
    print("hola")
    
    y=input("ingrese el primer ingrediente :")
    ing_lista2.append(y)
    conta=conta+1
print("los ingredientes de la pizza son:",ing_lista2)
 



    
    










    




    
        

