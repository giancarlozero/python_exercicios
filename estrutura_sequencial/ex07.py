"""
    7 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
"""

temp_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

# Fórmula para conversão: Celsius = ((Fahrenheit - 32) / 1.8)
temp_celsius = (temp_fahrenheit - 32) / 1.8

print(f'A temperatura é de {temp_celsius}ºC.')