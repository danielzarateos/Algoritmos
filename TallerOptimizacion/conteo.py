#Caso1
print("Hola mundo")
nombre = input(str("Ingrese su nombre : "))
print(nombre)

# PASOS = 3

#Caso2
print("Hola mundo")
nombre = input(str("Ingrese su nombre : "))
print(nombre)
x = int(input("Ingrese hasta cuanto voy a contar : "))

for i in range (x):
    print(f"He contado {i+1} pasos")
# PASOS = 4 (hasta x) + x 

#Caso3
print("Hola mundo")
nombre = input(str("Ingrese su nombre : "))
print(nombre)
x = int(input("Ingrese hasta cuanto voy a contar : "))

for i in range (x):
    print("He contado {i+1} pasos")
print("ya casi termino!")
print("adios")
# PASOS = 4 (hasta x) + 2 prints abajo + x 

#Caso4
x = int(input("Ingrese hasta cuanto voy a contar : "))

for i in range (x):
    for j in range (x):
        print(x)
print("Hola como vas")
print("Termine")
# PASOS = 1 (hasta x) + 2 prints abajo + x^2 (for dentro de for )

#Caso4
y = int(input("Ingrese hasta cuanto voy a contar : "))
x = int(input("Ingrese hasta cuanto voy a contar : "))

for i in range (x):
    for j in range (x):
        print(x)

for i in range (y):
    for j in range (y):
        print(y)

for i in range (x):
    for j in range (y):
        print(y)
print("Hola como vas")
print("Termine")
# PASOS = 2 (hasta x) + 2 prints abajo + x^2 (for dentro de for ) + y^2 + xy

