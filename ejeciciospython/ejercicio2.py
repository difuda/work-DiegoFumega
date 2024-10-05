'''Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta'''

def calcular_total(consumo):
    propina = consumo * 0.15
    total = consumo + propina
    return total

consumo = float(input('Introduzca el consumo de la cuenta a pagar:'))
total_a_pagar = calcular_total(consumo)
print(f'El total a pagar incluyendo propina es:{total_a_pagar}')