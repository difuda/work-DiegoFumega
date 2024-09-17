''' Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario'''
def numero_vocales(palabra):
    contador = 0
    vocales = 'aeiouAEIOU'
    for letra in palabra:
         if letra in vocales:
            contador = contador + 1
        
    return contador

palabra = input('escriba su palabra:')
nota = numero_vocales(palabra)
print (f' El numero de vocales es: {nota}')

