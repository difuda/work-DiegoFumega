'''Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%'''

def calcular_pecio_final(descuento):
    precio = int( input('introduce el precio del articulo:'))
    descuento = precio * 0.2
    precio_final= precio - descuento
    return precio_final

precio_final = calcular_pecio_final('descuento')
print (f'El precio final del articulo con descuento del 20% es: {precio_final} €')
