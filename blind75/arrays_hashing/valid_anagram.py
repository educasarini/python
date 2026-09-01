"""
Valid Anagram
Blind 75 - Arrays & Hashing | Facil
Nivel 1

Dadas duas strings s e t, retorne True se t for um anagrama de s, ou False
caso contrario. Um anagrama e formado reorganizando as letras de uma
palavra, usando todas as letras originais exatamente uma vez.

Exemplo 1:
Entrada: s = "anagram", t = "nagaram"
Saida: True

Exemplo 2:
Entrada: s = "rat", t = "car"
Saida: False

Exemplo 3:
Entrada: s = "a", t = "ab"
Saida: False

Restricoes:
- 1 <= len(s), len(t) <= 5 * 10**4
- s e t consistem apenas de letras minusculas do alfabeto ingles
"""

# from collections import Counter
    # return Counter(s) == Counter(t) --> faz todo o bloco de gerar dicionário e contar a frequência e atrelar a chave já

    # return "igualdade" ou algum comparativo retorna True ou False se estiver certo ou errado


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d_2 = {}

        for n in s:
            d[n] = d.get(n, 0) + 1
        for m in t:
            d_2[m] = d_2.get(m, 0) + 1
        return d == d_2

if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))  # esperado: True
    print(Solution().isAnagram("rat", "car"))           # esperado: False
    print(Solution().isAnagram("a", "ab"))               # esperado: False
    print(Solution().isAnagram("aab", "abb"))               # esperado: False
