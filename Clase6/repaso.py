#Ordenamiento
import time 
def crear_lista():
    size_list= int (input("ingrese el tamaño de la lista : "))
    lista  = [r.randint(1,1000000) for i in range (size_list)]

    return lista


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

print(lista)

inicio = time.time()
print(8 in lista)
final_nativo = time.time()-inicio
lista_ordenada = sorted(lista)
inicio = time.time()
print(busqueda_binaria(lista_ordenada,0,len(lista),8))
final_binario = time.time()-inicio
print(final_nativo)
print(final_binario)