#Enteros (int): Representan números enteros sin punto decimal. Puedes definir una variable entera de la siguiente manera:
mi_entero = 42

#Flotantes (float): Representan números con punto decimal. Puedes definir una variable flotante de la siguiente manera:
mi_flotante = 3.14159

#Cadenas (str): Representan texto. Puedes definir una variable de cadena de la siguiente manera:
mi_cadena = "Hola, mundo"

#Booleanos (bool): Representan valores verdaderos o falsos. Puedes definir una variable booleana de la siguiente manera:
verdadero = True
falso = False

#Nada (NoneType): Representa la ausencia de valor. Puedes definir una variable nula de la siguiente manera:
nada = None

mi_entero = 42
mi_flotante = 3.14159
verdadero = True

# Concatenar y convertir las variables a una cadena
resultado = "El valor de mi_entero es: " + str(mi_entero) + ", el valor de mi_flotante es: " + str(mi_flotante) + ", y verdadero es: " + str(verdadero)

# Imprimir el resultado
print(resultado)

#Los límites de los enteros y los flotantes en Python dependen de la plataforma
#y la arquitectura en la que se ejecute Python.
#son diferentes los limites de Python en sistemas de 64 bits,
#a los limites en sistemas de 32 bits o en implementaciones específicas de Python

import sys

max_entero = sys.maxsize
min_entero = -sys.maxsize - 1

print("Límite máximo de entero:", max_entero)
print("Límite mínimo de entero:", min_entero)

import sys

max_flotante = sys.float_info.max
min_flotante = sys.float_info.min

print("Límite máximo de flotante:", max_flotante)
print("Límite mínimo de flotante:", min_flotante)


# Solicitar al usuario que ingrese un valor entero para "n"
n = int(input("Ingresa un número entero para 'n': "))

# Calcular la suma de los primeros "n" números pares
suma_numeros_pares = n * (n + 1)

# Imprimir el resultado
print("La suma de los primeros", n, "números pares es:", suma_numeros_pares)
