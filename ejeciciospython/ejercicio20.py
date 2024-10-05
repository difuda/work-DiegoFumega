'''Crea un programa que sume todos los números en una lista ingresada por el
usuario'''

def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

lista = list(map(int, input('Introduzca una serie de numeros separados por un espacio:').split()))
sumatorio = suma_lista(lista)
print (f' La suma total de los numeros de la lista es de : {sumatorio}')
