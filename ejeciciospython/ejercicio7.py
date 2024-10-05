'''Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario'''

num1 = float(input('introduce elprimer numero:'))
num2 = float(input('introduce el sugindo numero:'))
operacion = input('introduzca la operación a realizar(suma, resta, multiplicacion,division):')

def calculadora(resultado):
    resultado = 0
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        resultado = num1 / num2
    return resultado

nota = calculadora('resultado')
print (f'el resultado de su operacion es: {nota}')

 
