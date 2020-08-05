import random as r
import time as t

def crear_lista():
    size_list = (int(input("Ingrese el tamaño de la lista : ")))

    lista = [r.randint(1,100) for i in range (size_list)]
            #Esto QUE llena          Esto cuantas veces

    return lista

def busqueda_lineal(lista, objetivo):
    encontrado = False

    for elemento in lista:
        if elemento == numero:
            encontrado = True
            break
    if encontrado == True:
        print("el numero esta en la lista")
    else:
        print("el numero no esta en la lista")

def busqueda_lineal_original(lista, objetivo):
    encontrado = False

    for i in range(len(lista)):
        if lista[i] == objetivo:
            encontrado = True
            break
    if encontrado == True:
        print("el numero esta en la lista")
    else:
        print("el numero no esta en la lista")



lista_objetivo = crear_lista()
print(lista_objetivo)
numero = int(input("Ingrese el numero a buscar : "))
inicio = t.time()
busqueda_lineal(lista_objetivo,numero)
print(t.time()-inicio)

inicio = t.time()
busqueda_lineal_original(lista_objetivo,numero)
print(t.time()-inicio)



#Como hacer break para que pare cuando lo encuentre

"""""
lista = [1,2,4,6,7]
#print( 2 in lista)
numero = int(input("Ingrese el numero que esta buscando : "))
print(lista_random)

for elemento in lista:
    if elemento = numero:
        encontrado = true
if encontrado = true:
    print("el numero esta en la lista")
else:
    print("el numero no esta en la lista")