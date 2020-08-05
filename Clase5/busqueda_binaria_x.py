numero = int(input("Ingrese un numero : "))
lista = [8,9,14,2,3,5,22]
lista_ordenada = sorted (lista)
print(lista_ordenada)

def busqueda_binaria (lista,comienzo,final,objetivo):
    if comienzo > final:
        return False
    if lista 