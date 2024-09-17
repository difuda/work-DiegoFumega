'''Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario'''

def lista_pares_impares(n):
    contador_pares = 0
    contador_impares = 0
    for numero in n:
        if numero % 2 == 0:
            contador_pares = contador_pares + 1
        else:
            contador_impares += 1
    return contador_pares, contador_impares

numeros = list(map(int, input('introduce una serie de numeros separados por un espacio:').split()))

contador_pares, contador_impares = lista_pares_impares(numeros)

print(f'la lista contiene {contador_pares} numeros pares y {contador_impares} numeros impares')
