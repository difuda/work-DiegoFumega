'''Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual'''

def calcular_edad(año_nacimiento):
    año_actual = 2024
    edad = año_actual - año_nacimiento
    return edad
año_nacimiento = int(input (' introduce tu año de nacimiento:'))
edad = calcular_edad(año_nacimiento)
print (f'Tu edad es de : {edad} años')
