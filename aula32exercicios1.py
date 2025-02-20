"""
EXERCICIO 1
Fça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é número inteiro
"""

print('EXERCICIO 1 - Feito Por Mim \n')

numero_str = input('Digite um número inteiro.: ')


try:
    numero = int(numero_str)
    if  numero % 2 == 0:
        print(f'O número {numero} é par')
    else:   
        print(f'O número {numero} é ímpar')
except ValueError:
    print(f'Você Não Digitou um Número Inteiro')
    
print('-' * 90)


"""
EXERCICIO 1 - Feito Pelo Professor
"""

print('EXERCICIO 1 - Feito Pelo Professor \n')


numero = input("Digite um número inteiro: ")

try:
    conversao_inteiro = int(numero)
except:
    print("Isso não é um número inteiro")

if conversao_inteiro % 2 == 0:
    print("O número é Par")
elif conversao_inteiro % 2 != 0:
    print("O número é ímpar")
