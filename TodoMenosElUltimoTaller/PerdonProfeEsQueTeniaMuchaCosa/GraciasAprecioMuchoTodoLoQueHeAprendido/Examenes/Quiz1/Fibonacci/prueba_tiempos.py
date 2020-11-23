import formulas
import time

n=int(input("Hasta que numero de la sucesion de Fibonacci quieres llegar : "))
inicio = time.time() 
formulas.caso1(n)
tiempo_caso1 = inicio-time.time()
inicio = time.time() 
formulas.caso2(n)
tiempo_caso2 = inicio-time.time()

if tiempo_caso1>tiempo_caso2:
  print("El caso 2 es el mas optimo en tiempo")
else: 
  print("El caso 1 es el mas optimo en tiempo")
