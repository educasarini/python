"""
Fura-Fila
Nivel 1 - Listas, Dicionarios, Sets e Strings | Facil

Dada uma lista de inteiros fila, representando senhas de atendimento na
ordem em que serao chamadas, e um inteiro senha que aparece exatamente uma
vez em fila, mova essa senha para o inicio da lista (ela "fura a fila"),
mantendo a ordem relativa das demais senhas. Retorne a lista resultante.

Assinatura:
def furar_fila(fila: list[int], senha: int) -> list[int]:

Exemplo 1:
furar_fila([5, 3, 8, 1], 8) -> [8, 5, 3, 1]

Exemplo 2:
furar_fila([2, 4, 6], 4) -> [4, 2, 6]

Exemplo 3:
furar_fila([9], 9) -> [9]

Restricoes:
- 1 <= len(fila) <= 100
- senha aparece exatamente uma vez em fila
- todos os valores em fila sao distintos
"""

# Escreva sua solucao abaixo:


def furar_fila(fila: list[int], senha: int) -> list[int]:
    fila.remove(senha)
    fila.insert(0, senha)
    return fila


print(furar_fila([5, 3, 8, 1], 8))   # esperado: [8, 5, 3, 1]
print(furar_fila([2, 4, 6], 4))      # esperado: [4, 2, 6]
print(furar_fila([9], 9))            # esperado: [9]