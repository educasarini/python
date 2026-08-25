"""
Two Sum
Blind 75 - Arrays & Hashing | Facil
Nivel 0 (forca bruta)

Dado um array de inteiros nums e um inteiro target, retorne os indices dos
dois numeros que somam exatamente target. Existe sempre exatamente uma
solucao valida, e o mesmo elemento do array nao pode ser usado duas vezes.
A ordem dos dois indices no retorno nao importa.

Exemplo 1:
Entrada: nums = [2, 7, 11, 15], target = 9
Saida: [0, 1]
(nums[0] + nums[1] = 2 + 7 = 9)

Exemplo 2:
Entrada: nums = [3, 2, 4], target = 6
Saida: [1, 2]

Exemplo 3:
Entrada: nums = [3, 3], target = 6
Saida: [0, 1]

Restricoes:
- 2 <= len(nums) <= 10**4
- -10**9 <= nums[i] <= 10**9
- -10**9 <= target <= 10**9
- Existe exatamente uma solucao valida.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, n in enumerate(nums):
            j = len(nums) - 1
            while j > i:
                if target == n + nums[j]:
                    return [i, j]
                j -= 1


print(Solution().twoSum([2, 7, 11, 15], 9))   # esperado: [0, 1]
print(Solution().twoSum([3, 2, 4], 6))         # esperado: [1, 2]
print(Solution().twoSum([3, 3], 6))            # esperado: [0, 1]