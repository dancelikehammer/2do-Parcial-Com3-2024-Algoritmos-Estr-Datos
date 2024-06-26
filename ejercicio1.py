from datetime import datetime, timedelta
import random
import os

# Ejercicio 1:
# Definir una clase Fecha. Formato: (dd, mm, aaaa).
class Fecha:
    def __init__(self, dd=None, mm=None, aaaa=None):
        if dd is None or mm is None or aaaa is None:
            # Si no se especifican los parámetros, se inicializa con la fecha de hoy
            hoy = datetime.today()
            self.dd = hoy.day
            self.mm = hoy.month
            self.aaaa = hoy.year
        else:
            self.dd = dd
            self.mm = mm
            self.aaaa = aaaa
    
    def calcular_dif_fecha(self, otra_fecha):
        # Calcula la diferencia en días entre dos fechas
        fecha1 = datetime(self.aaaa, self.mm, self.dd)
        fecha2 = datetime(otra_fecha.aaaa, otra_fecha.mm, otra_fecha.dd)
        diferencia = abs((fecha1 - fecha2).days)
        return diferencia
    
    def __str__(self):
        return f'({self.dd}, {self.mm}, {self.aaaa})'
    
    def __add__(self, dias):
        # Suma una cantidad de días a la fecha actual
        fecha_actual = datetime(self.aaaa, self.mm, self.dd)
        nueva_fecha = fecha_actual + timedelta(days=dias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
    
    def __eq__(self, otra):
        # Compara si dos fechas son iguales
        return self.dd == otra.dd and self.mm == otra.mm and self.aaaa == otra.aaaa


# Ejercicio 2:
# Definir una clase Alumno como un diccionario, el cual contiene los datos:
# { "Nombre" : 'string', "DNI" : 'integer' , "FechaIngreso" : 'Fecha', "Carrera" : 'cualquier tipo' }
class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }
    
    def cambiar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera=None):
        if nombre:
            self.datos["Nombre"] = nombre
        if dni:
            self.datos["DNI"] = dni
        if fecha_ingreso:
            self.datos["FechaIngreso"] = fecha_ingreso
        if carrera:
            self.datos["Carrera"] = carrera
    
    def antiguedad(self):
        # Calcular hace cuánto tiempo el alumno está inscrito en la carrera
        fecha_ingreso = self.datos["FechaIngreso"]
        hoy = datetime.now()
        antiguedad = hoy.year - fecha_ingreso.aaaa
        return antiguedad
    
    def __str__(self):
        return f'Alumno: {self.datos["Nombre"]} - DNI: {self.datos["DNI"]} - Carrera: {self.datos["Carrera"]}'
    
    def __eq__(self, otro):
        # Comparar si dos alumnos son iguales (mismo DNI)
        return self.datos["DNI"] == otro.datos["DNI"]


# Ejercicio 3:
# Crear una clase ListaDoblementeEnlazada cuyos nodos contengan como dato objetos del tipo Alumno.
# Implementar un Iterador para la lista enlazada (será útil en el siguiente ejercicio).
# La lista tendrá un método lista_ejemplo() el cual retorna un lista doblemente enlazada de alumnos cargada con datos aleatorios (random).
class Nodo:
    def __init__(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class IteradorLista:
    def __init__(self, lista):
        self.lista = lista
        self.actual = self.lista.cabeza
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration
        alumno = self.actual.alumno
        self.actual = self.actual.siguiente
        return alumno

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    
    def lista_ejemplo(self, cantidad_alumnos):
        nombres = ['Juan', 'Ana', 'Luis', 'Maria', 'Jose', 'Marta', 'Pedro', 'Lucia']
        carreras = ['Ingeniería Informática', 'Ingeniería Industrial', 'Matemáticas', 'Química', 'Biología']
        for _ in range(cantidad_alumnos):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = Fecha(random.randint(1, 31), random.randint(1, 12), random.randint(2000, 2023))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.agregar_al_final(alumno)
    
    def __iter__(self):
        return IteradorLista(self)


# Ejercicio 4:
# Implementar una función que permita ordenar la Lista Doblemente Enlazada "de Alumnos".
# El criterio de ordenación es: Fecha de Ingreso
# Ejercicio 4:
# Implementar una función que permita ordenar la Lista Doblemente Enlazada "de Alumnos".
# El criterio de ordenación es: Fecha de Ingreso
def ordenar_lista(lista):
    if lista.esta_vacia() or lista.cabeza == lista.cola:
        return
    
    current = lista.cabeza
    while current:
        min_node = current
        next_node = current.siguiente
        while next_node:
            if next_node.alumno.datos["FechaIngreso"].calcular_dif_fecha(min_node.alumno.datos["FechaIngreso"]) < 0:
                min_node = next_node
            next_node = next_node.siguiente
        
        # Swap nodes
        if min_node != current:
            current.alumno, min_node.alumno = min_node.alumno, current.alumno
        
        current = current.siguiente

import os
import random
from datetime import datetime, timedelta

# Define las clases Fecha y Alumno aquí (como ya han sido definidas antes)

# Ejercicio 5:
# Se debe crear un directorio en el cual guardaremos en un archivo una "lista de alumnos".
# Luego, deberán mover el directorio a una nueva ruta (path).
# Finalmente deben borrar el nuevo archivo y el nuevo directorio.
# NO útilizar el módulo shutil (pueden usa el módulo os).
def crear_directorio_guardar_datos(lista_alumnos, nombre_archivo, directorio_destino):
    try:
        # Obtener el directorio actual donde está el script parcial.py
        directorio_origen = os.path.dirname(os.path.abspath(__file__))
        
        # Crear el directorio en el directorio_origen
        nuevo_directorio = os.path.join(directorio_origen, "datos_alumnos")
        os.mkdir(nuevo_directorio)
        
        # Guardar la lista de alumnos en un archivo dentro del nuevo directorio
        ruta_archivo = os.path.join(nuevo_directorio, nombre_archivo)
        with open(ruta_archivo, 'w') as f:
            for alumno in lista_alumnos:
                f.write(str(alumno) + '\n')
        
        # Mover el directorio a directorio_destino
        nueva_ruta = os.path.join(directorio_destino, "datos_alumnos")
        os.rename(nuevo_directorio, nueva_ruta)
        
        # Borrar el archivo y el directorio
        os.remove(ruta_archivo)
        os.rmdir(nueva_ruta)
    
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    # Ejemplo de uso de las clases y funciones definidas
    
    # Ejercicio 1: Uso de la clase Fecha
    fecha1 = Fecha(25, 6, 2023)
    fecha2 = Fecha(26, 6, 2024)
    print(f'Fecha 1: {fecha1}')
    print(f'Fecha 2: {fecha2}')
    diferencia = fecha1.calcular_dif_fecha(fecha2)
    print(f'Diferencia en días entre Fecha 1 y Fecha 2: {diferencia} días')

    fecha3 = fecha2 + 10
    print(f'Fecha 3 (Fecha 2 + 10 días): {fecha3}')
    
    print(f'¿Fecha 1 es igual a Fecha 2? {fecha1 == fecha2}')
    
    # Ejercicio 2: Uso de la clase Alumno
    alumno1 = Alumno("Juan Perez", 12345678, fecha1, "Ingeniería Informática")
    print(alumno1)
    
    # Cambiar datos del alumno
    alumno1.cambiar_datos(nombre="Juan García")
    print(f'Alumno modificado: {alumno1}')
    
    # Ejercicio 3: Ejemplo de uso de la Lista Doblemente Enlazada
    lista_alumnos = ListaDoblementeEnlazada()
    lista_alumnos.lista_ejemplo(5)
    
    # Ejercicio 4: Ordenar la lista doblemente enlazada de alumnos por Fecha de Ingreso
    ordenar_lista(lista_alumnos)
    
    # Ejercicio 5: Crear directorio, guardar datos, mover y borrar
    nombre_archivo = "lista_alumnos.txt"
    directorio_destino = os.path.dirname(os.path.abspath(__file__))
    crear_directorio_guardar_datos(lista_alumnos, nombre_archivo, directorio_destino)
