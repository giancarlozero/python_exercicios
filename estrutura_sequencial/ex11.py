"""
    11 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7 * altura_homem) - 58
    Para mulheres: (62.1 * altura_mulher) - 44.7
"""

altura_homem = float(input('Olá, moço. Por favor, digite sua altura: '))
altura_mulher = float(input('Olá, garota! Por gentileza, digite sua altura: '))

# Calculando o peso ideal - para homens
peso_ideal_homem = (72.7 * altura_homem) - 58

print(f'Peso ideal (homem): {peso_ideal_homem} kg.')

# Calculando o peso ideal - para mulheres
peso_ideal_mulher = (62.1 * altura_mulher) - 44.7

print(f'Peso ideal (mulher): {peso_ideal_mulher} kg.')