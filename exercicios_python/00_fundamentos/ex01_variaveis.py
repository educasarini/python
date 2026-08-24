"""
Exercicio: Calculadora de IMC
Modulo 1 - Fundamentos (revisao: variaveis, tipos primitivos, conversao de tipos, f-strings)
Nivel: Facil

Enunciado:
Escreva um script que le do usuario (via input()) o peso (kg) e a altura (m),
calcula o IMC (peso / altura ** 2) e imprime o resultado formatado com 2 casas
decimais, usando f-string.

Requisitos:
- input() sempre retorna str -> converta explicitamente para o tipo numerico
  certo antes de fazer a conta.
- Formatacao com f-string e 2 casas decimais (nao usar round() manual nem
  concatenacao de string).
- Nomes de variaveis claros (sem abreviacao tipo p, a).

Exemplo de entrada/saida:
Peso (kg): 70
Altura (m): 1.75
IMC: 22.86
"""

# Escreva sua solucao abaixo:

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

print(f"Peso (kg): {peso:.2f}")
print(f"Altura (m): {altura:.2f}")
print(f"IMC: {imc:.2f}")