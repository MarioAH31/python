import random 
temperaturaMax = int(input("ingrese la temperatura maxima: "))
temperaturaMin = int(input("ingrese la temperatura minima: "))
valorNO2anual = 10

temperaturaActual = int(input("ingrese la temperatura actual: "))

if temperaturaActual >= temperaturaMax: 
    print(f"Alerta! temperatura alta, mayor a {temperaturaMax} alcanzada")

elif temperaturaActual <= temperaturaMin:
    print(f"Alerta! temperatura baja, menor a {temperaturaMin} alcanzada")

else:
    print("Temperatura normal, dentro de los paranetros")

alertameteoro = random.randint(0, 1)

if alertameteoro == 1:
    print("Alerta meteorologica activada")

nivelNO2 = random.randint(0, 15)

if nivelNO2 > valorNO2anual: 
    print(f"Alerta! contaminacion por NO2, nivel {nivelNO2} mayor a {valorNO2anual}")

else:
    print("Todo correcto")
