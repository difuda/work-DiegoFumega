'''Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no'''
def ver_si_mayor_18(edad):
    if edad < 18:
     return 'eres menor de edad'
    else:
     return 'eres mayor de edad'

edad = int(input('Introduzca su edad :'))
nota = ver_si_mayor_18(edad)
print (nota)

