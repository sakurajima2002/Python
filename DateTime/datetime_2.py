#time
from datetime import time

#time
time_1 = time(15,20,13,40)
print(time_1)
print(type(time_1))

#horas
print(f"\nHoras: {time_1.hour}")
#minutos
print(f"Minutos: {time_1.minute}")
#segundos
print(f"Segundos: {time_1.second}")
#microsegundos
print(f"Microsegundos: {time_1.microsecond}")