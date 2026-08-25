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

# Escreva sua solucao abaixo:

def soma_metades(numeros: list[int]) -> list[int]:
    pass


print(soma_metades([1, 2, 3, 4]))               # esperado: [3, 7]
print(soma_metades([10, 20, 30, 40, 50, 60]))   # esperado: [60, 150]
print(soma_metades([-2, -2, 4, 4]))             # esperado: [-4, 8]
