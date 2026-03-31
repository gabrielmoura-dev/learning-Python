# challenge
'''Escreva um programa que obtém um número dinâmico de valores de entrada.
A primeira entrada informa quantos números virão a seguir. As próximas entradas são números inteiros que você precisa somar.
No final, imprima a soma de todos os números de entrada (não incluindo a primeira entrada).
Por exemplo,
Entrada:
3
1
5
6

Saída esperada: 12
Explicação:

1 + 5 + 6 = 12, e há exatamente 3 números seguindo o primeiro número de entrada (3).'''

n = int(input()) #numero dinamico
x = 0
s = 0 # guardar soma
for i in range(n):
    x = int(input())
    s += x
print(s)
