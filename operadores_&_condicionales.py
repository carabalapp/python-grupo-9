#  Operadores de comparacion
# Ejemplos practicos de operaciones de comparacion
# 1) == Igual a
a = 5
b = 5

if a == b:
    print("a es igual a b")
    
# 2) != Diferente de
a = 5
b = 3

if a != b:
    print('a es diferente de b')
    
# 3) < Menor que

a = 3
b = 5

if a < b:
    print('a es menor que b')
    
# 4) > Mayor que
a = 7
b = 5

if a > b:
    print('a es mayor que b')
    
# 5) <= Mwenor o igual que
a = 5
b = 5

if a <= b:
    print('a es menor o igual a b')

# 6) >= Mayor o igual que
a = 5
b = 3

if a >= b:
    print('a es mayor o igual a b')

# Operadores Logicos

# and   : Verdadero si ambas condiciones son verdaderas
a = 5
b = 10

if a < b and b > 3:
    print('Ambas condiciones son verdaderas')
    
# or    : Verdadero si al menos una de la condicionwes es verdadera
a = 5
b = 3

if a > 10 or b < 5:
    print('Al menos una de las condiciones es verdadera')
    
# not   : Invierte el valor de verdad de la condicion
a = False

if  not a:
    print("a es falso", a)
else:
    print('a es verdadero')

# Condicionales: Nos ayudan a ejecutar diferentes bloques de codigo segun se cumpla o no ciertas condiciones

edad = 17

if edad < 18:
    print('Eres menor de edad.')
    #  Bloque de codigo a ejecutarse si la condicion es verdadera
elif edad == 18:
    print('Tienes 18 años')
    #  Bloque de codigo a ejecutar si la otra condicion es verdadera
else:
    print('Eres mayor de edad')
    # Bloque de codigo a ejecutar si ninguna de las condiciones anteriores es verdadera


