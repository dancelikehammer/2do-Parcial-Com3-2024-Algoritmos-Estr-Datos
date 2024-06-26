from datetime import date, timedelta

class Fecha:
    def __init__(self, dia=None, mes=None, anio=None):
        if dia is None or mes is None or anio is None:
            hoy = date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.anio = anio
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"
    
    def __add__(self, dias):
        nueva_fecha = date(self.anio, self.mes, self.dia) + timedelta(days=dias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
    
    def __eq__(self, otra):
        if not isinstance(otra, Fecha):
            return False
        return self.dia == otra.dia and self.mes == otra.mes and self.anio == otra.anio

    def calcular_dif_fecha(self, otra):
        if not isinstance(otra, Fecha):
            raise TypeError("El argumento debe ser una instancia de Fecha")
        fecha1 = date(self.anio, self.mes, self.dia)
        fecha2 = date(otra.anio, otra.mes, otra.dia)
        return abs((fecha1 - fecha2).days)

fecha1 = Fecha(10, 6, 2022)
fecha2 = Fecha(15, 6, 2022)

print(fecha1) 
print(fecha2)

print(fecha1 + 5)  
print(fecha1 == fecha2)  

dias_diferencia = fecha1.calcular_dif_fecha(fecha2)
print(f"Días de diferencia: {dias_diferencia}")  
