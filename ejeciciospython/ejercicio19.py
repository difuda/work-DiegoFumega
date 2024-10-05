'''Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no'''

def es_bisiesto(annio):
    if (annio % 4 == 0 and annio % 100 !=0) or annio % 400 == 0:
        return True
    return False

annio = int(input('Introduzca el año: '))

if es_bisiesto(annio):
    print (f' El {annio} es un año bisiesto')
else:
    print (f' El {annio} no es un año bisiesto')