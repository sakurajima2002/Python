#datetime.datetime
from datetime import date
import datetime

#Fecha y Hora Actual
date_1 = datetime.datetime.now()
print(date_1)

print(f"\nDia: {date_1.day}")
print(f"Mes: {date_1.month}")
print(f"Año: {date_1.year}")
print(f"Horas: {date_1.hour}")
print(f"Minutos: {date_1.minute}")
print(f"Segundos: {date_1.second}")
print(f"Microsegundos: {date_1.microsecond}")

#weekday() -> Primer dia de Semana Lunes
print(f"\nDia de la Semana: {date_1.weekday()}")

#isoweekday() -> Primer dia Semana Domingo
print(f"Dia de la Semana: {date_1.isoweekday()}")

#isocalendar() 
print(f"\n{date_1.isocalendar()}")

#fromisofromat()
date_1 = date.fromisoformat('2020-04-23')
print(f"\n{date_1}")
print(type(date_1))

#isoformat()
date_1 = date(2020,4,23).isoformat()
print(f"\n{date_1}")
print(type(date_1))

#strptime()
fecha = "30 Nov 00"
date_1 = datetime.datetime.strptime(fecha, "%d %b %y")
print(f"\n{date_1}")
print(type(date_1))

#timedelta
date_1 = datetime.datetime.now()
print("\nFecha de hoy: ",date_1)

#Sumar dias con datetime.timedelta
date_2 = date_1 + datetime.timedelta(days=2)
print("\nFecha 2 dias apartir de hoy: ",date_2)

#Sumar semanas con datetime.timedelta
date_3 = date_1 + datetime.timedelta(weeks=2)
print("\nFecha 2 semanas apartir de hoy: ",date_3)

#Fecha Pasada con datetime.timedelta
date_2 = date_1 - datetime.timedelta(days=3)
print("\nFecha 3 dias antes de hoy: ",date_2)

date_3 = date_1 - datetime.timedelta(weeks=2)
print("\nFecha 2 semanas antes de hoy: ",date_3)