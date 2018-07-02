"""
    09 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
"""

numero_inteiro_01 = int(input('Digite um número inteiro: '))
numero_inteiro_02 = int(input('Digite outro número inteiro: '))
numero_real = float(input('Digite um número real: '))

"""
    09.a - o produto do dobro do primeiro com metade do segundo 
"""

resultado01 = (numero_inteiro_01 * 2) * (numero_inteiro_02 / 2)
print(resultado01)
print()

"""
    09.b - a soma do triplo do primeiro com o terceiro
"""

resultado02 = (numero_inteiro_01 * 3) + numero_real
print(resultado02)
print()

"""
    09.c - o terceiro elevado ao cubo
"""

resultado03 = numero_real ** 3
print(resultado03)
print()