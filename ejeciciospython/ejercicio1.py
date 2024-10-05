'''Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit '''

def celsius_a_fahrenheit(temperatura):
    temperatura = float (input ('introduzca la temperatura a convertir:'))
    return temperatura * 1.8 + 32

temperatura_fahrenheit = celsius_a_fahrenheit('temperatura')
print(f'la temperatura en Fahrenheit es: {temperatura_fahrenheit}')
