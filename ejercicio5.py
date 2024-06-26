import os
import random
from datetime import datetime, timedelta

class Alumno:
    def __init__(self, nombre, edad, fecha_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso

    def __repr__(self):
        return f'Alumno({self.nombre}, {self.edad}, {self.fecha_ingreso})'

class ListaAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as file:
                for alumno in self.alumnos:
                    file.write(f'{alumno.nombre},{alumno.edad},{alumno.fecha_ingreso}\n')
            print(f'Se ha guardado la lista de alumnos en el archivo: {nombre_archivo}')
        except IOError as e:
            print(f'Error al guardar en el archivo: {e}')

def crear_directorio_guardar_y_mover():
    try:
        # 1. Crear directorio
        directorio_origen = './directorio_alumnos'
        if not os.path.exists(directorio_origen):
            os.makedirs(directorio_origen)
        print(f'Se ha creado el directorio: {directorio_origen}')

        # 2. Crear lista de alumnos
        lista = ListaAlumnos()
        nombres = ['Juan', 'Ana', 'Luis', 'Maria', 'Jose', 'Marta', 'Pedro', 'Lucia']
        fecha_inicio = datetime(2020, 1, 1)
        for _ in range(5):  # Crear 5 alumnos de ejemplo
            nombre = random.choice(nombres)
            edad = random.randint(18, 25)
            fecha_ingreso = fecha_inicio + timedelta(days=random.randint(0, 365*3))
            lista.agregar_alumno(Alumno(nombre, edad, fecha_ingreso))

        # Guardar lista de alumnos en un archivo dentro del directorio
        nombre_archivo = os.path.join(directorio_origen, 'lista_de_alumnos.txt')
        lista.guardar_en_archivo(nombre_archivo)

        # 3. Mover el directorio a una nueva ruta
        directorio_destino = './nueva_ruta/directorio_alumnos'
        os.rename(directorio_origen, directorio_destino)
        print(f'Se ha movido el directorio a la nueva ruta: {directorio_destino}')

        # 4. Borrar el archivo y el directorio en la nueva ruta
        os.remove(os.path.join(directorio_destino, 'lista_de_alumnos.txt'))
        os.rmdir(directorio_destino)
        print(f'Se ha borrado el archivo y el directorio en la nueva ruta: {directorio_destino}')

    except OSError as e:
        print(f'Error al crear, mover o borrar directorio/archivo: {e}')

# Ejecutar la función principal
crear_directorio_guardar_y_mover()
