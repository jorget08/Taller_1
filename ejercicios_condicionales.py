# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:35:48 2021

@author: jorge
"""
from random import randint
"""1. Hacer un algoritmo que calcule el total a pagar por la compra de
camisas. Si se compran tres camisas o mas se aplica un descuento
del 30% sobre el total de la compra y si son menos de tres camisas
un descuento del 10%."""
def suma(lista):
    sum = 0
    for i in lista:
        sum = sum + i
    return sum

camisas = int(input("Número de camisas a comprar: "))
count = 0
listax = []
for i in range(camisas):
    count += 1
    valor = int(input(f"Ingrese el precio de la camisa {count}: $"))
    listax.append(valor)
    
total = suma(listax)
if camisas >=3:
    total *= 0.7
    print(f"El total de la compra es: ${total}")
else:
    total *= 0.9
    print()
    print(f"El total de la compra es: ${total}")
    
    
"""2. En un supermercado se hace una promoción, mediante la cual el
cliente obtiene un descuento dependiendo de un número que se
escoge al azar. Si el número escogido es menor que 74 el descuento
es del 15% sobre el total de la compra, si es mayor o igual a 74 el
descuento es del 20%. Obtener cuanto dinero se le descuenta."""
    
valor_compra = int(input('Valor de la compra: $'))
aleatorio = randint(0,100)
print(f"Su numero aleatorio es: {aleatorio}")
if aleatorio < 74:
    valor_compra *= 0.85
else:
    valor_compra *= 0.80
    
print(f"Su descuento fue de: ${valor_compra}")


"""3. Una compañía de seguros está abriendo un departamento de
finanzas y estableció un programa para captar clientes, que conssite
en lo siguiente: Si el monto por el que se efectúa la fianza es menor
que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
es mayor que $50.000 la cuota a pagar será el 2% del monto. La
afianzadora desea determinar cual será la cuota que debe pagar al
cliente."""

fianza = int(input('Monto de la fianza: $'))
if fianza < 50000:
    cuota = fianza*0.03
else:
    cuota = fianza*0.02
print(f'La cuota a pagar es de: ${cuota}')

"""4. Una fábrica ha sido sometida a un programa de control de
contaminación para lo cual se efectúa una revisión de los puntos de
contaminación generados por la fábrica. El programa de control de
contaminación consiste en medir los puntos que emite la fábrica en
cinco días de una semana y si el promedio es superior a los 170
puntos entonces tendrá la sanción de parar su producción por una
semana y una multa del 50% de las ganancias diarias cuando no se
detiene la producción. Si el promedio obtenido de puntos es de 170 o
menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
desea saber cuanto dinero perderá después de ser sometido a la
revisión"""

listay = []
for i in range(5):
    puntos = int(input(f'Indique los puntos medidos del dia {i}: '))
    listay.append(puntos)
suma4 = suma(listay)
promedio = suma4/5
if promedio > 170:
    print('Debe cerar por una semana a demas de una multa del 50% de las ganancias diarias')
else:
    print('No debe ser sancionado')
    

"""5. Una persona se encuentra con un problema de comprar un automóvil
o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
mientras el automóvil se devalúa, con el terreno sucede lo contrario.
Esta persona comprará el automóvil si al cabo de tres años la
devaluación de este no es mayor que la mitad del incremento del
valor del terreno. Ayúdale a esta pesona a determinar si debe o no
comprar el automóvil."""




"""6. En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoreas que
compre. Si las computadoras son menos de cinco se les dará un 10%
de descuento sobre el total de la compra; si el número de
computadoras es mayor o igual a cinco pero menos de diez se le
otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
precio de cada computadora es de $11.000."""

computadoras = int(input('Ingrese el número de computadoras que comprará: '))
listaz = []
contador = 0
for i in range(computadoras):
    contador += 1
    valor_computadora = int(input(f'Ingrese el precio de la computadora {contador}: $'))
    listaz.append(valor_computadora)
precio_total_computadoras = suma(listaz)
if computadoras < 5:
    precio_total_computadoras *= 0.9
    print(f"El total con el 10% de descuento es: {precio_total_computadoras}")
elif computadoras >= 5 and computadoras < 10:
    precio_total_computadoras *= 0.8
    print(f"El total con el 20% de descuento es: {precio_total_computadoras}")
else:
    precio_total_computadoras *= 0.6
    print(f"El total con el 40% de descuento es: {precio_total_computadoras}")
    

"""7. Un proveedor de estéreos ofrece un descuento del 10% sobre el
precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
independientemente de esto, ofrece un 5% de descuento si la marca
es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
cualquiera por la compra de su aparato. IVA es del 16%."""

precio_con_iva = int(input('Ingrese el precio del producto: $'))
marca = input('Ingrese el precio del producto: $')
marca.upper()
precio_sin_iva = precio_con_iva / 1.19
if precio_con_iva >= 2000 and marca == 'NOSY':
    precio_sin_iva = *0.85
    total_con_iva = (precio_sin_iva*0.16)+precio_sin_iva
    print(f'El precio total con descuento es: {total_con_iva}')
elif precio_con_iva >= 2000:
    precio_sin_iva = *0.80
    total_con_iva = (precio_sin_iva*0.16)+precio_sin_iva
    print(f'El precio total con descuento es: {total_con_iva}')
    
"""8. Una empresa quiere hacer una compra de varias piezas de la misma
clase a una fábrica de refacciones. La empresa, dependiendo del
monto total de la compra, decidirá que hacer para pagar al fabricante.
Si el monto total de la compra excede de $500.000 la empresa tendrá
la capacidad de invertir de su propio dinero un 55% del monto de la
compra, pedir prestado al banco un 30% y el resto lo pagará
solicitando un crédito al fabricante. Si el monto total de la compra no
excede de $500.00 la empresa tendrá capacidad de invertir de su
propio dinero un 70% y el restante 30% lo pagará solicitando crédito
al fabricante. El fabricante cobra por concepto de interes un 20%
sobre la cantidad que se le pague a crédito. Obtener la cantidad a
inverir, valor del préstamo, valor del crédito y los intereses."""

piezas = int(input('Ingrese el numero de piezas a comprar: '))
valor_pieza = int(input('Ingrese el valor de cada pieza a comprar: $'))
total_compra = piezas * valor_pieza
if total_compra > 500000:
    capacidad_de_invertir = total_compra * 0.55
    prestamo_banco = total_compra * 0.3
    valor_credito = total_compra * 0.15
    intereses = valor_credito * 0.2
    print(f'La cantidad a invertir será de: ${capacidad_de_invertir}, con un prestamo al banco de: ${prestamo_banco} y un crédito al fabricante de: ${valor_credito} con intereses de: ${intereses}')
    
else:
    capacidad_de_invertir = total_compra * 0.7
    valor_credito = total_compra * 0.3
    intereses = valor_credito * 0.2
    print(f'La cantidad a invertir será de: ${capacidad_de_invertir} y un crédito al fabricante de: ${valor_credito} con intereses de: ${intereses}')


"""9. Leer 2 números; si son iguales que lo multiplique, si el primero es
mayor que el segundo que los reste y sino que los sume."""

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
if num1 == num2:
    respuesta = num1 * num2
elif num1 > num2:
    respuesta = num1 - num2
elif num1 < num2:
    respuesta = num1 + num2
print(respuesta)

"""10. Leer tres números diferentes e imprimir el número mayor de los
tres"""
listaw = []
for i in range(3):
    numero = int(input(f'Ingrese el número deseado: '))
    listaw.append(numero)
mayor = max(listaw)
print('')
print(f'El número mayor de los 3 es: {mayor}')
    