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


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))  # esperado: True
    print(Solution().isAnagram("rat", "car"))           # esperado: False
    print(Solution().isAnagram("a", "ab"))               # esperado: False
