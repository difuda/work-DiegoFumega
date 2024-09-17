'''Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos'''

def convertir_minutos(horas):
    minutos = int (input('introduzca el numero de minutos a convertir:'))
    horas = minutos // 60 
    minutos_restantes = minutos - horas * 60
    return (f'{horas} horas y {minutos_restantes} minutos')



horas_minutos = convertir_minutos('horas')
print (f'Los minutos introducidos son : {horas_minutos}')
