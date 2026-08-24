"""
Contains Duplicate
Blind 75 - Arrays & Hashing | Facil
Nivel 0 (forca bruta)

Dado um array de inteiros nums, retorne True se algum valor aparecer mais
de uma vez no array, ou False caso contrario.

Exemplo 1:
Entrada: nums = [1, 2, 3, 3]
Saida: True

Exemplo 2:
Entrada: nums = [1, 2, 3, 4]
Saida: False

Exemplo 3:
Entrada: nums = []
Saida: False

Restricoes:
- 0 <= len(nums) <= 10**5
- -10**9 <= nums[i] <= 10**9
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


print(Solution().hasDuplicate([1, 2, 3, 3]))   # esperado: True
print(Solution().hasDuplicate([1, 2, 3, 4]))   # esperado: False
print(Solution().hasDuplicate([]))             # esperado: False