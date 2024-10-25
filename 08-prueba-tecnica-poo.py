# Implementacion de una lista musical utilizando clases. ( Playlist )

class Cancion:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista

class Playlist:
    def __init__(self):
        self.lista = {}
    
    def agregar_cancion(self, cancion):
        if cancion.artista in self.lista:
            #  Verificamos si la cancion ya existe para ese artista
            if cancion.nombre not in self.lista[cancion.artista]:
                self.lista[cancion.artista].append(cancion.nombre)
                print(f"La cancion '{cancion.nombre}' ha sido agregada a {cancion.artista}")
            else:
                print(f"La cancion '{cancion.nombre}' ya existe en la lista de {cancion.artista}")
        else:
            # Si el artista no existe, lo agregamos con la cancion
            self.lista[cancion.artista] = [cancion.nombre]
            print(f"El artista '{cancion.artista}' ha sido agregado con la cancion '{cancion.nombre}'.")
    
    def mostrar_lista(self):
        print(self.lista)
        if not self.lista:
            print("La liosta musical esta vacia.")
            return
        for artista, canciones in self.lista.items():
            # Imprimir las canciones accediendo directamente a los atributos
            print(f"{artista}: {', '.join(canciones)}")
        
# Ejemplo de uso
lista_musical = Playlist()

# Crear algunas canciones
cancion1 = Cancion("Despacito", "Luis Fonsi")
cancion2 = Cancion("Shape of you", "Ed Sheeran")
cancion3 = Cancion("La Bicicleta", "Carlos Vives")
cancion4 = Cancion("Despacito Remix", "Luis Fonsi")
cancion5 = Cancion("Shape of you", "Ed Sheeran")

# Agregar canciones a la lista musical
lista_musical.agregar_cancion(cancion1)
lista_musical.agregar_cancion(cancion2)
lista_musical.agregar_cancion(cancion3)
lista_musical.agregar_cancion(cancion4)
lista_musical.agregar_cancion(cancion5)

# Mostrar la lista musical

lista_musical.mostrar_lista()