#  Ciclos ( o bucles )

# Son estruxcturas de control que permiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion

#  Hay 2 tipos principales de ciclos en python -> "for" y el "while"

# 1. Ciclo "for"

frutas = ["manzana", "cereza", "pera", "patilla"]

for fruta in frutas:
    print(fruta) # Imprime cada fruta de la lista
    
for i in range(5):
    print(i) # Imprime los numeros del 0 al 4

# Calculando los numeros pares hasta el 100

for numero in range(1,100): # Comienza en 1 y termina en 100
    if numero % 2 == 0:
        print(numero, 'Es par')
        
#  2. Ciclo "while" se va a ejecutar un bloque de codigo mientras una condicion sea verdadera

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1
