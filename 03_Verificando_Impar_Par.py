print('VERIFICAR SE O NÚMERO E PAR OU ÍMPAR \n')

# Solicita o usuário a digitar um número
numero_str = input('Digite um número inteiro.: ')

# Ira tentar executar o código a seguir com base nos dados fornecidos pelo usuário
try:

    # Converte o valor digitado em número inteiro
    numero = int(numero_str)

    '''
    Faz a setença onde caso o a divisão do valor, o restante for zero, esse número é par.
    Caso contrario, será ímpar
    '''
    if  numero % 2 == 0:
        print(f'O número {numero} é par')

    else:   
        print(f'O número {numero} é ímpar')

    '''
    Caso o usuário digite qualquer valor que nao seja número, será gerado o erro "ValueError",
    Com isso, será executado a setença excepty retornando a mensagem ao usuario:
    "Você Não Digitou um Número Inteiro".
    '''
except ValueError:
    print(f'Você Não Digitou um Número Inteiro')