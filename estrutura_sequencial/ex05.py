"""
    5 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

lado = float(input('Digite o valor de um dos lados de um quadrado perfeito: '))

area_quadrado = lado ** 2

print(f'A área deste quadrado é: {area_quadrado}.')
print(f'O dobro da área deste quadrado é: {area_quadrado * 2}.')