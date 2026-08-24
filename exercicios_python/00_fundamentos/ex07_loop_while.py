"""
Soma dos Digitos
Nivel 0 - Fundamentos | Facil

Dado um inteiro n, nao negativo, lido via input(), some todos os seus
digitos. Imprima o resultado em uma unica linha, no formato "Soma: <valor>".

Exemplo 1:
Entrada: n = 1234
Saida: Soma: 10
(1 + 2 + 3 + 4 = 10)

Exemplo 2:
Entrada: n = 0
Saida: Soma: 0

Exemplo 3:
Entrada: n = 9
Saida: Soma: 9

Restricoes:
- 0 <= n <= 10^9
"""

# Escreva sua solucao abaixo:

n = int(input("Digite número inteiro positivo: "))

soma = 0

while n > 0:
    soma += n % 10
    n //= 10

print(f"Soma: {soma}")