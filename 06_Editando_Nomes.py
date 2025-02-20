print('Editando o Nome \n')

# Solicita o usuário a digitar um nome e um simbolo para compor o nome
nome = input('Digite um Nome.: ')
simbolo = input('Digite um Simbolo.: ')

'''
definindo o indice de onde irá começar a verificação da variavél nome.
A mesma inicia com zero para que busque a primeira letra

Também definido o resultado, o qual constara a nosso texzto editado (de acordo com o simbolo digitado)
'''
indice = 0
resultado = ''

'''
realiza a colocação do simbolo digitado após cada letra do nome digitado.
'''
while indice < len(nome):
    letra = nome[indice]
    resultado += f'{simbolo}{letra}'
    indice += 1

'''
Realiza a impressão do valor digitado no terminal
'''
print(resultado)