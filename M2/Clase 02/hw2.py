#lanzar moneda al aire 10 veces y determinar resultados posibles en espacio muestral
tiros = 10
espacio_muestral = 2**tiros
print(espacio_muestral)

#combinaciones y permutaciones posibles
import math
pasajeros = 10
tamano_grupo = 3
permutaciones = math.perm(pasajeros, tamano_grupo)
combinaciones = math.comb(pasajeros, tamano_grupo)
print('Combinaciones: ', combinaciones)
print('Permutaciones: ', permutaciones)

from math import factorial
permutaciones = factorial(pasajeros) / factorial(pasajeros - tamano_grupo)
combinaciones = factorial(pasajeros) / (factorial(tamano_grupo) * factorial(pasajeros - tamano_grupo))
print('Combinaciones: ', combinaciones)
print('Permutaciones: ', permutaciones)


import pandas as pd
regiones = ['Norte','Noreste','Sur','Centro']
valores_si = [148, 162, 296, 252]
valores_no = [52, 54, 74, 48]
datos = dict(Si = valores_si, No = valores_no)
print(datos)
cuadro = pd.DataFrame(datos, index=regiones)

#¿Cuál es la probabilidad de que se use el cinturón en las distintas regiones del país? ¿En qué región se usa más el cinturón?(Utilizar misma tabla que el ejercicio anterior).
cuadro = cuadro/sum(cuadro.sum())
cuadro.loc['Total'] = sum(cuadro.Si), sum(cuadro.No)
cuadro = cuadro.assign(Total = cuadro.Si + cuadro.No)
print(cuadro)

# Crear una funcion que permita calcular a probabilidad de los siguientes eventos en un baraja de 52 cartas.
def probabilidad_cartas(palo, color):
    total_cartas = 52
    cartas_palo = 13
    cartas_color = 26

    if palo:
        return cartas_palo / total_cartas
    elif color:
        return cartas_color / total_cartas
    else:
        return 0

print('Probabilidad de sacar una carta de un palo: ')
print(probabilidad_cartas(True, False))
print('Probabilidad de sacar una carta de un color: ')
print(probabilidad_cartas(False, True))

# La probabilidad de que salga un 7 o un 8 al seleccionar una carta de una baraja de las 52 cartas que contiene el mazo.
cantidad_7 = 4
cantidad_8 = 4
total_cartas = 52
probabilidad = (cantidad_7 + cantidad_8) / total_cartas
print('Probabilidad de sacar un 7 o un 8: ', probabilidad)

#La probabilidad de tu país gane el mundial de fútbol.
probabilidad = 1 / 32
print('Probabilidad de que tu país gane el mundial de fútbol: ', probabilidad)

#Un experimento que tiene tres resultados es repetido 50 veces y se ve que E1 aparece 20 veces, E2 13 veces y E3 17 veces. Asigne probabilidades a los resultados.
total_experimentos = 50
E1 = 20
E2 = 13
E3 = 17
probabilidad_E1 = E1 / total_experimentos
probabilidad_E2 = E2 / total_experimentos
probabilidad_E3 = E3 / total_experimentos
print('Probabilidad de E1: ', probabilidad_E1)
print('Probabilidad de E2: ', probabilidad_E2)
print('Probabilidad de E3: ', probabilidad_E3)

#Si la probabilidad de que un cliente pague en efectivo (E) es 6/15, con tarjeta de crédito (TC) es 7/15 y con tarjeta de débito (TD) es 2/15. Hallar la probabilidad de que dos clientes sucesivos que pagan sus cuentas lo hagan: el primero en efectivo y el segundo con tarjeta de crédito.
probabilidad_E = 6 / 15
probabilidad_TC = 7 / 15
probabilidad_TD = 2 / 15
probabilidad = probabilidad_E * probabilidad_TC
print('Probabilidad de que el primer cliente pague en efectivo y el segundo con tarjeta de crédito: ', probabilidad)

# Los dos clientes en efectivo
probabilidad = probabilidad_E * probabilidad_E
print('Probabilidad de que los dos clientes paguen en efectivo: ', probabilidad)
