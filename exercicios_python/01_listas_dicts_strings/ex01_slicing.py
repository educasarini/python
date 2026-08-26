"""
Metade da Lista
Nivel 1 - Listas, Dicionarios, Sets e Strings | Facil

Dada uma lista de inteiros numeros, com uma quantidade par de elementos,
retorne uma nova lista com dois inteiros: a soma dos elementos na primeira
metade de numeros, e a soma dos elementos na segunda metade.

Assinatura:
def soma_metades(numeros: list[int]) -> list[int]:

Exemplo 1:
soma_metades([1, 2, 3, 4]) -> [3, 7]
(primeira metade: 1 + 2 = 3; segunda metade: 3 + 4 = 7)

Exemplo 2:
soma_metades([10, 20, 30, 40, 50, 60]) -> [60, 150]

Exemplo 3:
soma_metades([-2, -2, 4, 4]) -> [-4, 8]

Restricoes:
- 2 <= len(numeros) <= 1000
- len(numeros) e par
- -1000 <= numeros[i] <= 1000
"""

# assim como range, ele faz início (contando o que escrevi) e fim (não conta esse, mas sim o anterior)

# Escreva sua solucao abaixo:


def soma_metades(numeros: list[int]) -> list[int]:
    i = len(numeros) // 2
    return [sum(numeros[:i]), sum(numeros[i:])]


print(soma_metades([1, 2, 3, 4]))               # esperado: [3, 7]
print(soma_metades([10, 20, 30, 40, 50, 60]))   # esperado: [60, 150]
print(soma_metades([-2, -2, 4, 4]))             # esperado: [-4, 8]