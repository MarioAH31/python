def imprimirPares(lista):
    for num in lista:
        if num % 2 == 0:
            print(num, end=" ")

def imprimirImpares(lista):
    for num in lista:
        if num % 2 != 0:
            print(num, end=" ")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
imprimirPares(numeros)
imprimirImpares(numeros)