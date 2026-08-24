"""
E Primo?
Nivel 0 - Fundamentos | Facil

Escreva uma funcao que recebe um inteiro n e retorna True se n for um
numero primo, ou False caso contrario. Um numero primo e um inteiro maior
que 1 que nao tem divisores alem de 1 e ele mesmo.

Assinatura:
def eh_primo(n: int) -> bool:

Exemplo 1:
eh_primo(7) -> True

Exemplo 2:
eh_primo(8) -> False

Exemplo 3:
eh_primo(1) -> False

Restricoes:
- 0 <= n <= 10**6
"""

# Escreva sua solucao abaixo:

def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(eh_primo(17))
print(eh_primo(20))
print(eh_primo(14))
print(eh_primo(9))