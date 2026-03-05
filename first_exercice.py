import random
# from decimal import Decimal
'''
Criar Variáveis:
Crie duas variáveis para armazenar seu nome e sua idade. 
Em seguida, use print() para exibir uma mensagem como: "Olá, meu nome é [seu nome] e eu tenho [sua idade] anos." 
'''
# nome = input("Digite seu nome: ")
# idade = input("Qual é a sua idade: ")
# print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
Identificadores:
Crie uma variável para armazenar o preço de um produto e outra para armazenar a quantidade comprada. 
Calcule o total gasto e mostre o resultado.
'''
# preco = Decimal(input("Insira o preço do produto que comprou: "))
# qtde_comprada = int(input("Quantos você comprou?: "))
# gasto_total = preco * qtde_comprada
# print(f"O total de gasto foi: R$ {gasto_total:.2f}")
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
Tomadas de Decisão:
Digite um programa que solicite ao usuário sua idade e verifique se ele pode votar (idade mínima de 18 anos). 
Utilize if e else para mostrar uma mensagem apropriada.
'''
# idade = int(input("Qual a sua idade? "))
# if (idade >= 18):
#     print("Você já pode votar!")
# else:
#     print("Você ainda não têm idade mínima para votar.")

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''    
'''
Decisões Compostas:
Crie um programa que pergunte ao usuário se ele deseja sair de casa. 
Se ele responder 'sim', mostre "Leve a chave!", caso contrário, mostre "Fique em casa!".
'''
# desejo = input("Deseja sair de casa? ")
# while desejo != 'SIM' and desejo != 'NAO':
#     print("Digite SIM ou NAO")
#     desejo = input("Deseja sair de casa? ").upper()

# if desejo == 'SIM':
#     print("Leve a chave!")
# else:
#     print("Fique em casa!")
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''    
'''
Operadores Lógicos:
Solicite ao usuário para digitar sua idade e se ele possui carteira de motorista. 
Se a idade for 18 anos ou mais e ele possuir carteira, exiba "Você pode dirigir". Caso contrário, exiba "Você não pode dirigir".
'''
# idade_usuario = int(input("Qual é a sua idade? "))
# carteira_motorista = input("Possui carteira de motorista? ")
# while carteira_motorista != 'SIM' and carteira_motorista != 'NAO':
#     print("Digite SIM ou NAO")
#     carteira_motorista = input("Possui carteira de motorista? ").upper()

# if idade_usuario >= 18 and carteira_motorista == 'SIM':
#     print("Você pode dirigir")
# else:
#     print("Você não pode dirigir")
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''  
'''
Laços de Repetição - while:
Crie um programa que peça ao usuário que insira números e os some. 
O programa deve continuar a perguntar até que o usuário digite 0. Ao final, exiba a soma total.  
'''

# soma = 0
# numero = int(input("Insira um número: "))

# while numero != 0:
#     soma += numero
#     numero = int(input("Insira um número: "))

# print("A soma total é:", soma)

'''
Laços de Repetição - for:
Utilize um for para criar uma lista de números de 1 a 10 e imprima o quadrado de cada número.
'''

# lista_numeros = []
# for x in range(1, 11):
#     lista_numeros.append(x)
#     print(x ** 2)
    
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''  
'''
Desafio de Mistura:
Faça um programa que pergunte ao usuário quantas vezes ele deseja jogar um jogo de adivinhação. 
Utilize um for para repetir o jogo por esse número de vezes, onde o usuário deve tentar adivinhar um número entre 1 e 100. 
Ao final de cada tentativa, informe se a tentativa foi muito alta, muito baixa ou correta. 
O jogo deve parar se o usuário adivinhar corretamente ou se ele não quiser mais jogar.
'''

usuario = input("Qual é o seu nome? ")
user_attempts = int(input(f"{usuario}, quantas vezes você deseja jogar um jogo de adivinhação? "))

random_integer = random.randint(1, 100)

for i in range(user_attempts):
    user_number_selected = int(input("Qual número você escolhe? "))

    if user_number_selected > random_integer:
        print("Sua tentativa foi muito alta")
    elif user_number_selected < random_integer:
        print("Sua tentativa foi muito baixa")
    else:
        print("Você adivinhou o número!")
        break
else:
    print(f"Suas tentativas acabaram! O número era {random_integer}.")


