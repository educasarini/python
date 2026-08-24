"""
Exercicio: Conversor de Temperatura (Celsius -> Fahrenheit)
Modulo 1 - Fundamentos (variaveis, tipos primitivos, conversao de tipos, f-strings)
Nivel: Facil

Enunciado:
Escreva um script que le do usuario, via input(), a temperatura em graus Celsius,
converte para Fahrenheit usando a formula F = C * 9/5 + 32, e imprime APENAS UMA
linha de saida, no formato "Fahrenheit: X.XX", com 2 casas decimais, usando f-string.

Especificacao das variaveis:
- celsius: float. Aceita valores com casas decimais e negativos (ex: 0, 37.5, -40).
- fahrenheit: float. Resultado calculado a partir de celsius.

Requisitos tecnicos:
- input() retorna str -> converta celsius explicitamente para float (nao use int()).
- Formatacao com f-string e 2 casas decimais (nao usar round() manual nem
  concatenacao de string).
- Nomes de variaveis claros (sem abreviacao tipo c, f).
- Saida: uma unica linha, exatamente no formato "Fahrenheit: X.XX".

Exemplo 1:
Entrada: 0
Saida: Fahrenheit: 32.00

Exemplo 2:
Entrada: 37.5
Saida: Fahrenheit: 99.50

Exemplo 3:
Entrada: -40
Saida: Fahrenheit: -40.00
(caso curioso: -40 graus e o ponto onde Celsius e Fahrenheit se cruzam)
"""

# Escreva sua solucao abaixo:

celsius = float(input("Digite a temperatura: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"Fahrenheit: {fahrenheit:.2f}")