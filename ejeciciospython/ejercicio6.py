'''Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)'''

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

palabra = input('escriba su palabra:')

print (es_palindromo (palabra))

