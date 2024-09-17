'''Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros'''

dolares = float( input('introduce la cantidad de dolares a convertir:'))

def convertir_dolares_a_euros(monedas):
    euros = dolares * 0.85
    return euros

euros = convertir_dolares_a_euros('monedas')
print(f' La cantidad en euros es : {euros}')


