x1 = int(input("ingrese el valor de x1: "))
y1 = int(input("ingrese el valor de y1: "))
x2 = int(input("ingrese el valor de x2: "))
y2 = int(input("ingrese el valor de y2: "))
x3 = int(input("ingrese el valor de x3: "))
y3 = int(input("ingrese el valor de y3: "))

def distancia (x1, y1, x2, y2):
    cx = (x2 - x1)
    cy = (y2 - y1)
    dist1 = ((cx**2) + (cy**2))**(1/2)
    print(f"la distancia entre los dos puntos es a({x1}) y b ({x2}) es: {dist1}")

# calcular distancia entre a y b 
distancia (x1, y1, x2, y2)
# calcular distancia entre b y c
distancia (x2, y2, x3, y3)
#calcular distancia entre c y a 
distancia (x3, y3, x1, y1)

