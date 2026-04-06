c1=int(input("ingrese el valor del primer cateto: "))
c2=int(input("ingrese el valor del segundo cateto: "))
area=(c1*c2)/2
hipotenusa=(c1**2+c2**2)**0.5
perimetro=c1+c2+hipotenusa 
print(f"area = {area: .2f}")
print(f"promedio = {perimetro}")