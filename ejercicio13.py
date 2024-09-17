'''Escribe un programa que determine si un número ingresado por el usuario es primo
o no'''

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range (2,numero):
        if numero % i == 0:
           return False
    return True

numero= int(input('introduce un numero:'))

if es_primo(numero):
    print (f' el numero {numero} es primo')
else:
    print (f'el numero {numero} no es primo')