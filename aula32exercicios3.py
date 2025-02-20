"""
EXERCICIO 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu Nome é Curto"; se tiver entre 5 e 6 leras, escreva
"Seu Nome é Normal"; maior que 6 escreva "Seu Nome é Muito Grande".
"""

print('EXERCICIO 3 - Feito Por Mim \n')

nome = input('Informe o seu primeiro nome.: ')
quantLetras = len(nome)

nome_pequeno = (quantLetras <= 4) and (nome.isalpha() == True)
nome_normal = (quantLetras > 4 and  quantLetras <= 6) and (nome.isalpha() == True)
nome_grande = (quantLetras > 6) and (nome.isalpha() == True)

if  nome_pequeno :
    print(f'Seu nome é pequeno, pois possui apenas {quantLetras} letras')

if nome_normal:
    print(f'Seu nome é normal, pois possui apenas {quantLetras} letras')

if nome_grande :
    print(f'Seu nome é grande, pois possui apenas {quantLetras} letras')

else :
    print(f'Digite Apenas Letras no campo "Informe o seu primeiro nome"')

print('-' * 90)

"""
EXERCICIO 3 - Feito Pelo Professor
"""

print('EXERCICIO 3 - Feito Pelo Professor \n')

nome = input("Digite o seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")