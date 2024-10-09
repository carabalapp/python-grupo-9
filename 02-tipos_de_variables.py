# Numeros

# Enteros ( int )
entero = 42

print(type(entero))

# Flotantes

flotante = 3.14

print(type(flotante))

# Complejos

complejo = 2 +3j

print(type(complejo))

# Cadena o String
cadena = "Hola, Mundo!"

print(type(cadena))

# Booleanos ( Valores de verdad o falso)

verdadero = True
falso = False

print(type(verdadero))

print(type(falso))

#  Listas (Colecciones ordenadas y mutables de elementos, puede tener elementos de diferentes tipos.)
#  Las listas guardan los valores en posiciones, las cuales comienzan desde la posicion 0 hasta la n-1 siendo "n" el valor total de elementos

lista = [1,4,7,2,3.3]


print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

lista[2] = 8

print('Lista mutada',lista)
print('La longitud o cantidad de eklementos de mi lista es: ',len(lista))

#  Tuplas (Colecciones ordenadas e INMUTABLES de elementos, al igual que las listas pueden contener elementos de diferentes tipos)

tupla = (1,2,2,3,"cuatro",5.0)
print(type(tupla))
print(len(tupla))
print(tupla[-2]) # n-2 donde "n" es la longitud o el numero total de elementos que contiene mi tupla

# tupla[1] = 2 # Esto da error, ya que las tuplas no se pueden modificar

# print('Tratando de mutar la tupla',tupla)

# Diccionarrios (Colecciones de pares clave-valor) en donde cada clave es unica y son utilizadas para acceder a su valor

diccionario = {
    "nombre": "Adrian",
    "edad": 31,
    "altura": 1.75
    }

usuarios = [
    {
        "cedula": 9876543,
        "nombre": "Adrian",
        "edad": 31,
        "altura": 1.75
    },
    {
        "cedula": 1234567,
        "nombre": "Julio",
        "edad": 26
    }
]

# print(type(diccionario))
# print(diccionario["genero"])
# print(diccionario.get("altura", "No disponible o no existe"))

print(usuarios[3].get("altura", "No Disponible"))


