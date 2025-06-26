#*
#* ---------------Variables-------------------
#* 1. TIPOS PRIMITIVOS
# Entero (int)
edad = 25  # Para números sin decimales
# Flotante (float)
pi = 3.1416  # Para números con decimales
# Booleano (bool)
es_mayor = True  # Puede ser True o False
# String (str)
nombre = "Ana"  # Cadena de texto (unicode)
# NoneType
dato = None  # Representa ausencia de valor

#* 2. ESTRUCTURAS DE DATOS

# Lista (list) - Mutable y ordenada
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", True, 3.14]  # Puede contener mixed types

# Tupla (tuple) - Inmutable y ordenada
Tupla_coordenadas = (4, 5)
Tupla_configuracion = ("localhost", 8080, "https")

# Diccionario (dict) - Pares clave-valor
persona = {
    "nombre": "Luis",
    "edad": 30,
    "es_estudiante": False
}
# Conjunto (set) - Elementos únicos desordenados
set_unicos = {1, 2, 3, 3, 2}  # Resultado: {1, 2, 3}
# Frozenset - Conjunto inmutable
frozenset_fset = frozenset({1, 2, 3})

#* 3. TIPOS AVANZADOS/ESPECIALES

# Bytes - Secuencia inmutable de bytes
b = b"hola"  # Prefijo 'b'
# Bytearray - Secuencia mutable de bytes
ba = bytearray(b"hola")
# Range - Secuencia inmutable de números
rango = range(0, 10, 2)  # 0, 2, 4, 6, 8
# Complex - Números complejos
z = 3 + 5j

# Formas correctas de Nombrar Variables
numero_cinco=5
NumeroCinco=5
_numeroCinco=5

# Asignacion de variables
a,b,c = 2,6,"string"
# print(b)

def myFunction():
  variable_1="texto de ejemplo"
  print(variable_1)

# myFunction()

# Operadores

# 5==5
# 4 !=5
# 0 < 1
# 5 <= 5

# or
# and
# not

edad=18

# if edad<18:
#   print("Eres menor de edad")
# elif edad==18:
#   print("Acabas de convertirte en mayor de edad")
# else:
#   print("Eres mayor de edad")

lista_nombres=["Brahan","lider","Tunquipa","mamani"]

# for nombre in lista_nombres:
#   print(nombre)

lista_numeros=[23,24,25,26]

# for num in lista_numeros:
#   if num ==25:
#     # break #hasta ahí
#     continue # tod0s menos ese
#   print(num)

cadena_texto = "hola, soy brahan"

# for letra in cadena_texto:
#   print(letra)

print(cadena_texto[2])