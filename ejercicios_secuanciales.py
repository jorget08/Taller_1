# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:13:30 2021

@author: jorge
"""

"""1. Tres personas deciden invertir su dinero para fundar una empresa.
Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
que cada quien invierte con respecto a la cantidad total invertida."""
def suma(lista):
    sum = 0
    for i in lista:
        sum = sum + i
    return sum
listax = []
count = 0
for i in range(3):
    count += 1
    inversor = int(input(f'Capital invertido por el inversor {count}: $'))
    listax.append(inversor)

capital_total = sum(listax)
contador = 0
for i in listax:
    contador += 1
    x = (i*100)/capital_total
    print(f'El porcentaje de inversión del inversor {contador} es del: {x}%')
    
    
"""2. Una empresa paga a sus empleados además del sueldo base una
bonificación especial de $80.000 por cada hijo. Realice un programa
en Java que determine el monto de la bonificación y el monto total a
pagar al trabajador."""

sueldo_base = int(input('Ingrese el sueldo base del empleado: $'))
hijos = int(input('Ingrese número de hijos del trabajador: '))
bonificacion = 80000 * hijos
total_empleado = sueldo_base + bonificacion
print(f'El monto total a pagar al empleado es de: ${total_empleado}')

"""3. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
ahorrado. Teniendo como dato de entrada el saldo inicial del
ahorrador determine el saldo final."""

dato_entrada = int(input('Ingrese el saldo inicial a ahorrar: $'))
total_salida = (dato_entrada * 0.015) + dato_entrada
print(f'El saldo final del ahorrado mas sus intereses es de: ${total_salida}')


"""4. Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
cliente debe dar una cuota inicial del 35%y el resto lo paga en 12
cuotas. Determine el valor a pagar por cuota inicial y el monto de
cada cuota."""

metros_cuadrados = int(input('Ingrese la cantidad de mestros cuadrados a comprar: '))
precio_total = metros_cuadrados * 80000
cuota_inicial = precio_total * 0.35
cuotas = (precio_total - cuota_inicial)/12
print(f'Para {metros_cuadrados} metros cuadrados el valor a pagar por cuota inicial es de: ${cuota_inicial}, y las 12 cuotas son de: ${cuotas}')


"""5. Una empresa le hace los siguientes descuentos sobre el sueldo base
a sus trabajadores: 1% por ley de politica pública, 4% por seguro
social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
programa en Java que determine el monto de cada descuento y el
monto total a pagar al trabajador"""

sueldo_trabajador = int(input('Ingrese el sueldo base del trabajador: $'))
politica_publica = sueldo_trabajador * 0.01
seguro_social = sueldo_trabajador * 0.04
seguro_forzoso = sueldo_trabajador * 0.005
caja_ahorro = sueldo_trabajador * 0.05
total_trabajador = sueldo_trabajador - seguro_forzoso - seguro_social - caja_ahorro - politica_publica

print(f'El monto de descuento por ley de politica pública es de: ${politica_publica}')
print(f'El monto de descuento por seguro social es de: ${seguro_social}')
print(f'El monto de descuento por seguro forzoso es de: ${seguro_forzoso}')
print(f'El monto de descuento por caja de ahorro es de: ${caja_ahorro}')
print(f'El monto total a pagar al trabajador es de: ${total_trabajador}')


"""6. El periódico el Informador cobra por un aviso clasificado un monto
que depende del número de palabras, tamaño en cetímetros y
número de colores. Cada palabra tiene un costo de $20.000, cada
centímetro tiene un costo de $15.000 y cada color tiene un costo de
$25.000. Realice un algoritmo que determine el monto a pagar por un
aviso clasificado"""

palabras = int(input('Ingrese el número de palabras que tendrá el aviso: '))
centimetros = int(input('Ingrese el tamoño en centimeros que tendrá el aviso: '))
color = int(input('Ingrese el número de colores que tendrá el aviso: '))
total_aviso = (palabras * 20000) + (color * 15000) + (centimetros * 25000)
print(f'El monto a pagar por el aviso clasificado es: ${total_aviso}')



"""7. Una empresa paga a sus empleados un bono por antigüedad que
consiste en $100.000 por el primer año laboral y $120.000 por cada
año siguiente. Realice un programa en Java que determine el monto
del bono a pagar a un trabajador que tiene varios años en la empresa."""

antiguedad = int(input('Ingrese el número de años que tiene el empleado en la empresa: '))
bono = ((antiguedad - 1) * 120000) + 100000
print(f'El monto del bono a pagar al trabajador es: ${bono}')


"""8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
un descuento del 5% por concepto de caja de ahorro. Determine el
monto del descuento y el monto total a pagar al profesor"""

horas_profesor = int(input('Ingrese el número de horas trabajadas por el profesor: '))
salario_sin_descuento = (horas_profesor * 20000)
descuento_salario = salario_sin_descuento * 0.05
salario_con_descuento = salario_sin_descuento - descuento_salario
print(f'El salario del profesor es de: ${salario_con_descuento} y su descuento es de: ${descuento_salario}')


"""9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
y cobran el monto consumido de la tarjeta mas un recargo del 20%.
Teniendo como dato de entrada el monto inicial y el monto final de la
tarjeta, determine el costo de la llamada."""

monto_inicial = int(input('Ingrese el monto inicial de la tarjeta: $'))
monto_final = int(input('Ingrese el monto final de la tarjeta: $'))
monto_consumido = (monto_inicial - monto_final)
costo_llamada = (monto_consumido * 0.2) + monto_consumido
print(f'El costo de la llamada es: ${costo_llamada}')

"""10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
foto. Realice un programa en Java que determine el monto a pagar
por un revelado completo sabiendo que adiconalmente le cobran el
IVA (16%)"""

fotos_revelar = int(input('Ingrese el número de fotos a revelar: '))
costo_revelador = fotos_revelar * 1500
total_revelado = (costo_revelador * 0.16) + costo_revelador
print(f'El monto a pagar para revelar {fotos_revelar} fotos es de: ${total_revelado}')


"""11. En un hospital existen tres áreas: Ginecología, Pediatría y
Traumatología. El presupuesto anual del hospital se reparte
conforme a la siguiente tabla:
Area Porcentaje Presupuestal
Ginecología 40%
Traumatología 30%
Pediatría 30%
Obtener la cantidad de dinero que recibirá cada área, para cualquier
monto presupuestal."""

presupuesto_anual = int(input('Ingrese el presupuesto de este año: $'))
ginecologia = presupuesto_anual * 0.4
traumatologia = presupuesto_anual * 0.3
pediatria = presupuesto_anual * 0.3

print(f'La cantidad de dinero para ginecologia es de: ${ginecologia}')
print(f'La cantidad de dinero para traumatologia es de: ${traumatologia}')
print(f'La cantidad de dinero para pediatria es de: ${pediatria}')


"""12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
que consiste en dejar gratis el alquiler de una película. Realice un
programa en Java que teniendo como dato de entrada el total de
películas alquiladas, y el número de días de alquiler, determine el
monto a pagar"""

peliculas_alquiladas = int(input('Ingrese el número de peliculas alquiladas: '))
dias_alquiler = int(input('Ingrese el número de dias de alquiler: '))
monto_alquiler = (peliculas_alquiladas - 1) * (dias_alquiler * 1500)
print(f'El monto a pagar por las {peliculas_alquiladas} peliculas es de: ${monto_alquiler}')


"""13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
diarios por persona. Realice un programa en Java que determine el
monto a pagar por una familia que desee realizar dicho Tour
sabiendo que también cobran el 12% de IVA"""

personas_viaje = int(input('Ingrese el número de personas que van a viajar: '))
costo_tour = personas_viaje * 25000
total_viaje = (costo_tour * 0.12) + costo_tour
print(f'El monto a pagar por el tour para las {personas_viaje} es de: ${total_viaje}')


"""14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
clientes. Cobra por una habitación $100.000 el primer día y por el
resto $200.000 por día. Realice un programa en Java que determine
el valor total a pagar por la habitación si la estadía fue de varios
días"""

dias_estadia = int(input('Ingrese el número de dias de estadia: '))
total_habitacion = ((dias_estadia - 1) * 200000) + 100000
print(f'El valor total a pagar por la habitacion es de: ${total_habitacion}')



"""El banco del Pueblo da microcréditos a empresarios para ser
cancelados en un lapso de 2 años (24 meses). Al monto del 
préstamo se le cobra un interés del 24%. El empresario debe pagar
la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
cuotas ordinarias. Realice un algoritmo que teniendo como dato de
entrada el monto del préstamo, determine el monto total a pagar por
el préstamo, el monto de las cuotas especiales y el monto de las
cuotas ordinarias."""


monto_prestamo = int(input('Ingrese valor del prestamo: $'))
intereses = monto_prestamo * 0.24
monto_total_pagar = monto_prestamo + intereses
mitad_prestamo = monto_total_pagar / 2
cuotas_especiales = mitad_prestamo / 4
cuotas_ordinarias = mitad_prestamo / 20
print(f'El monto total a pagar del credito es: ${monto_total_pagar}')
print(f'El monto de cada cuota especial es de: ${cuotas_especiales}')
print(f'El monto de cada cuota ordinaria es de: ${cuotas_ordinarias}')














