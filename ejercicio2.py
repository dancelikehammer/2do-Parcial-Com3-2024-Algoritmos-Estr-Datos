from datetime import datetime

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def cambiar_dni(self, nuevo_dni):
        self.dni = nuevo_dni
    
    def cambiar_fecha_ingreso(self, nueva_fecha_ingreso):
        self.fecha_ingreso = nueva_fecha_ingreso
    
    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
    
    def antiguedad(self):
        fecha_ingreso = datetime.strptime(self.fecha_ingreso, "%Y-%m-%d")
        return (datetime.now() - fecha_ingreso).days
    
    def __str__(self):
        return f"Alumno: {self.nombre}, DNI: {self.dni}, Fecha de Ingreso: {self.fecha_ingreso}, Carrera: {self.carrera}"
    
    def __eq__(self, otro):
        if not isinstance(otro, Alumno):
            return False
        return self.dni == otro.dni

alumno1 = Alumno("Juan Perez", 12345678, "2020-01-15", "Ingeniería")
print(alumno1)

alumno1.cambiar_nombre("Juan P. Perez")
alumno1.cambiar_carrera("Matemáticas")
print(alumno1)

print(f"Antigüedad: {alumno1.antiguedad()} días")

alumno2 = Alumno("Ana Lopez", 87654321, "2019-09-01", "Medicina")
print(alumno1 == alumno2)

