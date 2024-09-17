'''Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario'''

def contador_palabras(oracion):
    palabras = oracion.split()
    print (palabras)
    cantidad_palabras = len(palabras)
    print (cantidad_palabras)
    return cantidad_palabras

oracion = input('Introduzca la oración:')
contar_palabras = contador_palabras(oracion)

print (f' El numero de palabras en la oracion es de: {contar_palabras}')



