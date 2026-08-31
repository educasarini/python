"""
Inverter Palavras
Nivel 1 - Listas, Dicionarios, Sets e Strings | Facil

Dada uma string frase contendo uma ou mais palavras separadas por espacos
simples, sem espacos no inicio ou no fim, retorne uma nova string com as
mesmas palavras na ordem inversa, separadas por um unico espaco.

Assinatura:
def inverter_palavras(frase: str) -> str:

Exemplo 1:
inverter_palavras("o rato roeu a roupa") -> "roupa a roeu rato o"

Exemplo 2:
inverter_palavras("ola mundo") -> "mundo ola"

Exemplo 3:
inverter_palavras("python") -> "python"

Restricoes:
- 1 <= len(frase) <= 1000
- frase contem apenas letras minusculas e espacos simples entre palavras
"""

# Escreva sua solucao abaixo:


def inverter_palavras(frase: str) -> str:
    return " ".join(frase.split()[::-1])


# esperado: "roupa a roeu rato o"
print(inverter_palavras("o rato roeu a roupa"))

# esperado: "mundo ola"
print(inverter_palavras("ola mundo"))

# esperado: "python"
print(inverter_palavras("python"))
