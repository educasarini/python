"""
Group Anagrams
Blind 75 - Arrays & Hashing | Media
Nivel 1

Dada uma lista de strings strs, agrupe os anagramas juntos. Pode retornar
a resposta em qualquer ordem — tanto a ordem dos grupos quanto a ordem
das strings dentro de cada grupo nao importam.

Exemplo 1:
Entrada: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Saida: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Exemplo 2:
Entrada: strs = [""]
Saida: [[""]]

Exemplo 3:
Entrada: strs = ["a"]
Saida: [["a"]]

Restricoes:
- 1 <= len(strs) <= 10**4
- 0 <= len(strs[i]) <= 100
- strs[i] consiste apenas de letras minusculas do alfabeto ingles
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    print(Solution().groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["a"]))
