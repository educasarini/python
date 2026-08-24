"""
Verificador de Faixa e Paridade
Nivel 0 - Fundamentos | Facil

Dados tres inteiros numero, minimo e maximo (nessa ordem, lidos via
input()), imprima exatamente tres linhas:

Dentro do intervalo: <True ou False>
Par e positivo: <True ou False>
Fora do intervalo: <True ou False>

"Dentro do intervalo" e True se numero estiver entre minimo e maximo,
incluindo os limites. "Par e positivo" e True se numero for par E maior
que zero, ao mesmo tempo. "Fora do intervalo" e o oposto de "Dentro do
intervalo".

Exemplo 1:
Entrada: numero = 10, minimo = 1, maximo = 20
Saida:
Dentro do intervalo: True
Par e positivo: True
Fora do intervalo: False

Exemplo 2:
Entrada: numero = -4, minimo = 1, maximo = 20
Saida:
Dentro do intervalo: False
Par e positivo: False
Fora do intervalo: True

Exemplo 3:
Entrada: numero = 20, minimo = 1, maximo = 20
Saida:
Dentro do intervalo: True
Par e positivo: True
Fora do intervalo: False

Restricoes:
- minimo <= maximo
- -1000 <= numero, minimo, maximo <= 1000
"""

# Escreva sua solucao abaixo:

numero = int(input("Digite número: "))
minimo = int(input("Digite mínimo: "))
maximo = int(input("Digite máximo: "))

intervalo =  minimo <= numero <= maximo

fora_intervalo = not intervalo

par_positivo =  numero % 2 == 0 and numero > 0

print(f"Dentro do intervalo: {intervalo}")
print(f"Par e positivo: {par_positivo}")
print(f"Fora do intervalo: {fora_intervalo}")