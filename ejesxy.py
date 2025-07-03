x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de y: "))
if (x == 0 and y == 0):
 print("El punto esta en el origen")
elif (x > 0 and y > 0):
 print("cuadrante 1")
elif (x < 0 and y > 0):
 print("cuadrante 2")
elif (x < 0 and y < 0):
 print("cuadrante 3")
elif (x > 0 and y < 0):
 print("cuadrante 4")