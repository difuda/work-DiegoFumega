'''Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros'''

def millas_a_kilometros(distancia):
    millas = int(input(' introduce el numero de millas a convertir:'))
    km = millas * 1.60934
    return km

kilometros = millas_a_kilometros('distancia')
print(f' Los km resultantes son: {kilometros}')