"""
    6 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

ganho_por_hora = float(input('Quanto você ganha por hora trabalhada? '))
hora_trabalhada_por_mes = int(input('Quantas horas você trabalha por mês? '))

print(f'Eu trabalho {hora_trabalhada_por_mes} horas por mês e ganho R$ {ganho_por_hora} por hora trabalhada. Logo, eu ganho R$ {ganho_por_hora * hora_trabalhada_por_mes} por mês.')