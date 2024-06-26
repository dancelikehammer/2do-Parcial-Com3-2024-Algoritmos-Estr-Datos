import random
import string

class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f'Alumno({self.nombre}, {self.edad})'

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def __iter__(self):
        return ListaDoblementeEnlazadaIterador(self.cabeza)

    def lista_ejemplo(self, cantidad):
        nombres = ['Juan', 'Ana', 'Luis', 'Maria', 'Jose', 'Marta', 'Pedro', 'Lucia']
        for _ in range(cantidad):
            nombre = random.choice(nombres)
            edad = random.randint(18, 25)
            self.insertar_al_final(Alumno(nombre, edad))
        return self

class ListaDoblementeEnlazadaIterador:
    def __init__(self, cabeza):
        self.actual = cabeza

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual.dato
        self.actual = self.actual.siguiente
        return dato

# Ejemplo de uso
lista = ListaDoblementeEnlazada().lista_ejemplo(10)
for alumno in lista:
    print(alumno)
