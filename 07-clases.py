# Clases ( class ) son parte fundamental de la POO ( Programacion orientada a objetos )

# 1) Definicion de una clase: Se define utilizando la palabra clave "class", seguido del nombre de la dclase. Por convencion, el nombre de la clase comienza con una letra mayuscula, Las clases son plantillas que nos permiten crear objetos.

class MiClase:
    pass

# 2) Atributos: Son variables que pertenecen a la clase. Se peuden definir con el metodo especial "init", que se llama cuando se crea una instancia de la clase..
# 3) Metodos: Son funciones que pertenecen a la clase y pueden operar sobre los atributos de la clase. El primer parametro de un metodo debe ser "self" que se refiere a la instancia actual de la clase.
class Persona:
    def __init__(self, nombre, edad, estatura=170):
        self.nombre = nombre # Atributo nombre
        self.edad = edad # Atributo edad
        self.estatura = estatura # Atributo estatura
        
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y mido {self.estatura}cm")
        

# 4) Instanciacion: Para crear un objeto de una clase, se llama a la clase como si fuera una funcion
adrian = Persona("Adrian", 31, 173)
carlos = Persona("Carlos", 21, 182)

# print(adrian.nombre)
# print(adrian.edad)
# print(adrian.estatura)

adrian.saludar()
carlos.saludar()


#  Herencia: Las clases pueden heredar atributos y metodos de otra clase, lo que nos permite crear jerarquias y reutilizar codigo

class Trabajador(Persona):
    def __init__(self,nombre, edad, estatura, curso):
        super().__init__(nombre, edad, estatura) # Llama al constructor de la clase base ( Persona )
        self.curso = curso
        
    def trabajar(self):
        print(f"{self.nombre} esta trabajando en {self.curso}")

trabajador1 = Trabajador("Alexei", 22, 175, "Oplesk")

trabajador1.saludar()
trabajador1.trabajar()


# Ejemplo de clases aplicado en situaciones de la vida real

# 1. Sistema de gestion de estudiantes

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado = grado
        self.notas = []
        
    def agregar_nota(self,nota):
        self.notas.append(nota)
    
    def promedio(self):
        # sum(1,2,3) = 1 + 2 + 3 = 6 / len(self.notas) = 3
        return sum(self.notas) / len(self.notas) if self.notas else 0
    
    
#  Usabilidad

estudiante1 = Estudiante("Ana", 16, "10°")
# estudiante1.agregar_nota(1)
# estudiante1.agregar_nota(2)
# estudiante1.agregar_nota(3)
estudiante1.saludar()
print(f"Promedio de {estudiante1.nombre}: {estudiante1.promedio()}")


# 2. Sistema de gestion de inventario

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            print("Stock insuficiente")
            return False

# Uso
producto1 = Producto("Laptop", 1200, 10)
producto1.vender(2)
print(f"Stock de {producto1.nombre}: {producto1.cantidad}")