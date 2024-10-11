# Funciones sin parametros

def saludar():
    print('Hola')

# a = 4
# b = 5
# print(a + b)

# a = 6
# b = 3
# print(a + b)

# a = 3
# b = 2
# print(a + b)

#  Funciones con parametros
def sumar(num1=2, num2=3):
    saludar()
    return num1 + num2
    
resultado = sumar()

print('El resultado de la suma con funcion asignado a una variable es:',resultado)
print('El resultado de la suma con funcion sin asignarlo a una variable es:',sumar(6,3))


def resta(num1, num2):
    print('El resultado de la resta es:', num1 - num2)

a = 3
b = 2 

resta(a, b)
resta(2, 3)


#  Funciones con parametros por defecto
def despedir(nombre='Juan'):
    if nombre is None:
        print('Adios Amigo')
    else:
        print(f'Adios {nombre}')

despedir()
despedir('Adonis')
despedir(None)


# *args
# Funciones con numero variable de argumentos ( no conocemos la cantidad de argumentos que vamos a necesitar)

def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)
    print('--------------------------------------------------------')

listar_nombres('adrian', 'douglas', 'adonis', 'juan','bettina')
listar_nombres('adrian', 'douglas', 'adonis', 'juan','bettina', 'carlos')
listar_nombres('adrian', 'douglas', 'adonis', 'juan','bettina', 'carlos', 'jorge')

# **kwargs -> kw = "Keyword" args = arguments ó argumentos
# Funciones con con un numero de argumentos variables pero se recibe un conjunto de pares clave-valor
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f'{clave}: {valor}')
    
mostrar_info(nombre="pedro", edad=30, ciudad="madrid")

# Funciones lambda ( funciones sin nombre )
#  1) Se utilizan cuando necesitamos realizar operaciones simples de una sola linea
#  2) Usarlas como argumentos para funciones de orden superior, como: map(), filter(), sorted()

multiplicar = lambda x,y: print('Resultado de la funcion lambda multiplicando es :',x * y)
sumando = lambda x: print('Resultado de la funcion lambda sumando una lista es :',sum(x))

multiplicar(3,3)
sumando([1,2,3,4,5])

# Funciones anidadas

def funcion_externa(x): # X en este punto vale 3, tiene un scope global
    def funcion_interna(y): # Scope local
        return y ** 2
    resultado = funcion_interna(x) # Llamando a la funcion interna
    return resultado + 1 # Sumando 1 al resultado de la funcion interna

resultado_final = funcion_externa(3)

print('resultado final de funciones anidadas',resultado_final)

# Recursividad.
# Contiene 2 conceptos

#  1) El caso Base: Es la conduicion que va detener la recursion. Sin un caso base, la funcion se estaria llamando a si misma indefinidamente, lo que nos llevaria a un desbordamiento de pila ( stack overflow )

#  2) Caso recursivo: esta es la parte de la funcion donde se llama a si misma, pero con un argumento modificado que eventualmente alcanzara el caso base.

# Factorial de un numero: es el producto ( multiplicacion ) de todos los numeros enteros desde el 1 hasta n

# 1...n si n = 5 entonces seria: 1x2x3x4x5 = 120

#  factorial iterativo:

def factorial_iterativo(n):
    resultado = 1
    for i in range (1, n + 1):
        resultado *= i # resultado = resultado * i
    return resultado

n = 5
print(f'el factorial iterativo de {n} es: ',factorial_iterativo(n))

def factorial_recursivo(n):
    # caso base
    if n == 0:
        return 1
    # caso recursivo
    else:
       return n * factorial_recursivo(n - 1)
        
print(f'factorial recursivo de {n} es:', factorial_recursivo(n))

