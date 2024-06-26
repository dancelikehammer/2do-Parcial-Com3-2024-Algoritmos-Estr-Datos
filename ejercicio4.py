import random
from datetime import datetime, timedelta

class Alumno:
    def __init__(self, nombre, edad, fecha_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso

    def __repr__(self):
        return f'Alumno({self.nombre}, {self.edad}, {self.fecha_ingreso})'

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
        fecha_inicio = datetime(2020, 1, 1)
        for _ in range(cantidad):
            nombre = random.choice(nombres)
            edad = random.randint(18, 25)
            fecha_ingreso = fecha_inicio + timedelta(days=random.randint(0, 365*3))
            self.insertar_al_final(Alumno(nombre, edad, fecha_ingreso))
        return self

    def ordenar_por_fecha_ingreso(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return
        
        actual = self.cabeza.siguiente
        while actual is not None:
            key = actual.dato
            j = actual.anterior

            while j is not None and j.dato.fecha_ingreso > key.fecha_ingreso:
                j.siguiente.dato = j.dato
                j = j.anterior
            
            if j is None:
                self.cabeza.dato = key
            else:
                j.siguiente.dato = key
            
            actual = actual.siguiente

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

lista = ListaDoblementeEnlazada().lista_ejemplo(10)
print("Lista antes de ordenar:")
for alumno in lista:
    print(alumno)

lista.ordenar_por_fecha_ingreso()
print("\nLista después de ordenar por fecha de ingreso:")
for alumno in lista:
    print(alumno)
