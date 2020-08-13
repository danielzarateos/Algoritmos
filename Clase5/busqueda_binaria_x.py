numero = int(input("Ingrese un numero : "))
lista = [8,9,14,2,3,5,22]
lista_ordenada = sorted (lista)
print(lista_ordenada)

def busqueda_binaria (lista,comienzo,final,objetivo):
    if comienzo > final:
        return False
    medio = (comienzo +final)/2
    if lista(medio) == objetivo:
        return True
    elif lista(medio)<objetivo:
        return busqueda_binaria(lista,medio+1,objetivo)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo)

