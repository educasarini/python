"""
Classificador de IMC
Nivel 0 - Fundamentos | Facil

Dado um valor de IMC (float), lido via input(), imprima a categoria
correspondente em uma unica linha, no formato "Categoria: <categoria>".

As categorias sao:
- "Abaixo do peso"  -> IMC menor que 18.5
- "Peso normal"     -> IMC maior ou igual a 18.5 e menor que 25
- "Sobrepeso"       -> IMC maior ou igual a 25 e menor que 30
- "Obesidade"       -> IMC maior ou igual a 30

Exemplo 1:
Entrada: imc = 17.2
Saida: Categoria: Abaixo do peso

Exemplo 2:
Entrada: imc = 24.9
Saida: Categoria: Peso normal

Exemplo 3:
Entrada: imc = 30.0
Saida: Categoria: Obesidade

Restricoes:
- 0.0 <= imc <= 100.0
"""

# Escreva sua solucao abaixo:

imc = float(input("Digite IMC: "))

if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

print(f"Categoria: {categoria}")