'''Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona'''

peso = float(input('introduce tu peso en kg :'))
altura = float(input('introduce tu altura en m: '))

def calcular_imc(cuerpo):
    imc = peso / (altura **2)
    return imc

imc = calcular_imc('cuerpo')   
print(f'el imc es de : {imc:.2f}')

    