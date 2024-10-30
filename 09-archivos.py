# Abrir un archivo
# Hacemos uso de una funcion de python que se llama open()
# ejemplo: archivo = open('nombre_del_archivo.txt', 'modo')

# Los modos mas comunes para abrir archivos son:
# 'r': Leer ( read ). Abre el archivo para lectura. Si el archivo no existe, se genera un error.
# 'w': Escribir ( write ). Abre el archivo en modo escritura. Si el archivo ya existe, se sobrescribe.
# 'a': Añadir: ( append ). Abre el archivo para añasdir contenido al final, Si el archivo no existe, se crea uno nuevo.

# archivo = open('archivo_ejemplo.txt', 'w')
# # for linea in archivo:
# #     print(linea.strip())
    
# # parte = archivo.read(10)
# # print(parte)

# archivo.write('Hola Mundo!\n')

# archivo.close()

# archivo = open('archivo_ejemplo.txt', 'r')

# print(archivo.read())

# try:
#     with open('archivo_ejemplo.txt', 'r') as archivo:
#         contenido = archivo.readline()
#         print(contenido)
# except FileNotFoundError:
#     print('El archivo no existe')
# except Exception as e:
#     print(f"Ocurrio un error {e}")


        
# with open('archivo_ejemplo.txt', 'a') as archivo:
#     archivo.write('\nLinea 5: Añadiendo mas contenido.\n')
#     archivo.write('Linea 6: Sigo manteniendo los registros anteriores.\n')

# with open('archivo_ejemplo.txt', 'r') as archivo:
#         contenido = archivo.read()
#         print(contenido)

with open('ejemplo.txt', 'w+') as archivo:
    archivo.write('Linea 1: Este es un ejemplo de archivo.\n')
    archivo.write('Linea 2: Arpendiendo a manejar archivos en python.\n')
    archivo.write('Linea 3: Este archivo contiene varias linea.\n')

