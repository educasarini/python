"""
Interesses em Comum
Nivel 1 - Listas, Dicionarios, Sets e Strings | Facil

Dadas duas listas de strings interesses_a e interesses_b, representando
os interesses de duas pessoas (sem repeticoes dentro de cada lista),
retorne um set com os interesses que aparecem nas duas listas ao mesmo
tempo.

Assinatura:
def interesses_em_comum(
    interesses_a: list[str], interesses_b: list[str]
) -> set[str]:

Exemplo 1:
interesses_em_comum(["futebol", "musica", "livros"],
                     ["musica", "cinema", "livros"]) -> {"musica", "livros"}

Exemplo 2:
interesses_em_comum(["a", "b"], ["c", "d"]) -> set()

Exemplo 3:
interesses_em_comum(["x"], ["x"]) -> {"x"}

Restricoes:
- 0 <= len(interesses_a), len(interesses_b) <= 500
- cada string tem entre 1 e 30 caracteres
"""

# Escreva sua solucao abaixo:


def interesses_em_comum(
    interesses_a: list[str], interesses_b: list[str]
) -> set[str]:
    pass


print(interesses_em_comum(
    ["futebol", "musica", "livros"], ["musica", "cinema", "livros"]
))  # esperado: {"musica", "livros"}

print(interesses_em_comum(["a", "b"], ["c", "d"]))  # esperado: set()

print(interesses_em_comum(["x"], ["x"]))  # esperado: {"x"}
