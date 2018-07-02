"""
    8 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
"""

temp_celsius = float(input('Digite a temperatura em Celsius: '))

# Fórmula para conversão: Fahrenheit = (Celsius * 1.8) + 32
temp_fahrenheit = (temp_celsius * 1.8) + 32

print(f'A temperatura é de {temp_fahrenheit}ºF.')