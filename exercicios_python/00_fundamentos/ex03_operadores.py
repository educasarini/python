"""
Exercicio: Divisao Inteira e Resto
Modulo 1 - Fundamentos (operadores aritmeticos: // e %)
Nivel: Facil

Enunciado:
Escreva um script que le do usuario, via input(), dois numeros inteiros:
dividendo e divisor (nessa ordem). Calcule o quociente da divisao inteira
e o resto da divisao, usando os operadores // e % (nao vale fazer conta
manual tipo dividendo - quociente*divisor). Imprima duas linhas, nesse
formato exato:
Quociente: X
Resto: Y

Especificacao das variaveis:
- dividendo: int. Pode ser negativo.
- divisor: int. Sempre positivo nos exemplos abaixo (nao precisa tratar
  divisor = 0 neste exercicio).

Requisitos tecnicos:
- input() retorna str -> converta ambos explicitamente para int.
- Use // para quociente e % para resto (nao use conversao de float nem
  divisao comum com truncamento manual).
- Nomes de variaveis claros (sem abreviacao tipo d, q, r).

Exemplo 1:
Entrada: dividendo=17, divisor=5
Saida:
Quociente: 3
Resto: 2

Exemplo 2:
Entrada: dividendo=20, divisor=4
Saida:
Quociente: 5
Resto: 0

Exemplo 3 (atencao, esse e o pegadinha):
Entrada: dividendo=-7, divisor=2
Saida:
Quociente: -4
Resto: 1

No Exemplo 3, repare que o resultado NAO e Quociente: -3, Resto: -1 (que
seria o comportamento de truncamento em direcao a zero, como em C/Java).
Em Python, // arredonda para baixo (floor), entao -7 // 2 = -4, e o resto
sempre tem o mesmo sinal do divisor, entao -7 % 2 = 1. Teste esse caso no
seu terminal antes de me entregar -- se o seu codigo usar // e % nativos
do Python, ele ja vai dar esse resultado sozinho, sem voce precisar tratar
nada manualmente.
"""

# Escreva sua solucao abaixo:

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f"Quociente: {quociente}")
print(f"Resto: {resto}")