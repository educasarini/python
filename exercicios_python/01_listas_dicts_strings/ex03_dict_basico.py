"""
Contador de Votos
Nivel 1 - Listas, Dicionarios, Sets e Strings | Facil

Dada uma lista de strings votos, onde cada string e o nome de um candidato
votado, retorne um dicionario em que cada chave e um nome de candidato
presente em votos e o valor correspondente e quantas vezes esse candidato
aparece na lista.

Assinatura:
def contar_votos(votos: list[str]) -> dict[str, int]:

Exemplo 1:
contar_votos(["ana", "bruno", "ana"]) -> {"ana": 2, "bruno": 1}

Exemplo 2:
contar_votos(["carla"]) -> {"carla": 1}

Exemplo 3:
contar_votos(["ana", "ana", "ana"]) -> {"ana": 3}

Restricoes:
- 1 <= len(votos) <= 1000
- cada string em votos tem entre 1 e 50 caracteres, apenas letras minusculas
"""

# Escreva sua solucao abaixo:


def contar_votos(votos: list[str]) -> dict[str, int]:
    d = {}

    for n in votos:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d

'''
d = {}

for n in votos:
    d[n] = d.get(n, 0) + 1
return d
'''

# esperado: {"ana": 2, "bruno": 1}
print(contar_votos(["ana", "bruno", "ana"]))

# esperado: {"carla": 1}
print(contar_votos(["carla"]))

# esperado: {"ana": 3}
print(contar_votos(["ana", "ana", "ana"]))

# esperado: {"ana: 2, "bruno: 1}
print(contar_votos(["ana", "ana", "bruno"]))