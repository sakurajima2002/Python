#date
from datetime import date

#date
date_1 = date(2013, 5, 20)
print(date_1)
print(type(date_1))

#datetime.date
print(f"\n{date_1}")
print("Dia: ",date_1.day)
print("Mes: ",date_1.month)
print("Año: ",date_1.year)

#date.today
date_1 = date.today()
print(f"\n{date_1}")
print("Dia: ",date_1.day)
print("Mes: ",date_1.month)
print("Año: ",date_1.year)


