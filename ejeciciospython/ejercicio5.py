'''Escribe un programa que calcule la suma de todos los números pares del 1 al 100'''

suma = 0
for i in range(0,101,2):
    suma += i
print(f'La suma de los numeros pares es: {suma}')
