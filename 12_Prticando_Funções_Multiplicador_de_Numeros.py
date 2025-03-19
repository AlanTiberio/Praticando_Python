'''
Importantdo biblioteca para limpeza de terminal
'''
import os
'''
Variavel que roda meu sistema
'''
sistema = 's'

while sistema == 's':
    '''
    Irá limpar o terminal e iniciar novamente o programa
    '''
    os.system('cls')

    '''
    Titulo do meu programa
    '''
    print('EXERCICIOS COM LISTAS - MULTIPLICADOR\n')

    '''
    Cria a fuunção função multiplicador, que pegara o número digitado pelo usuário
    '''
    def criar_multiplicador(multiplicador):

        '''
        Cria a função multiplicar, no qual será criado sera multiplicado de acordo com meu multiplicador
        '''
        def multiplicar(numero):
            return numero * multiplicador
        return multiplicar
    
    '''
    Criando os multiplicadores onde:

    duplicar     = número digitado pelo usuário X 2
    triplicar    = número digitado pelo usuário X 3
    quadruplicar = número digitado pelo usuário X 4
    '''
    duplicar     = criar_multiplicador(2)
    triplicar    = criar_multiplicador(3)
    quadruplicar = criar_multiplicador(4)

    '''
    Solicita o usuário a digitar um número
    '''
    digitarNumero = input('Digite um número (ex.: 1, 1.2, 3.0).: ')

    try:
        '''
        Irá converter o número digitado pelo usuário em float
        '''
        numero = float(digitarNumero)
        '''Irá exibir o resultado de acordo com o número digitado'''
        print(f'\n')
        print(f'O número digitado foi {numero:.2f} \n')
        print(f'O doblo de {digitarNumero} é.: {duplicar(numero):.2f}')
        print(f'O triplo de {digitarNumero} é.: {triplicar(numero):.2f}')
        print(f'O quadruplo de {digitarNumero} é.: {quadruplicar(numero):.2f} \n')
        '''
        Pergunta se o usuario deseja seguir utilizando o sistema
        '''
        sistema = input('Deseja Continuar? Digite "s" para sim ou qualquer tecla para não.: ' )

    except ValueError:
        print(f'\n')
        print('Verifique o valor digitado \n')
        '''
        Pergunta se o usuario deseja seguir utilizando o sistema
        '''
        sistema = input('Deseja Continuar? Digite "s" para sim ou qualquer tecla para não.: ')
        
    except TypeError:
        print(f'\n')
        print('Verifique o valor digitado \n')
        '''
        Pergunta se o usuario deseja seguir utilizando o sistema
        '''
        sistema = input('Deseja Continuar? Digite "s" para sim ou qualquer tecla para não.: ')    

'''
Retorna aquilo de acordo com o que o usuario digitar
'''
if sistema != 's':
    '''
    Irá limpar o terminal
    '''
    os.system('cls')  
    '''
    Mensagem de finalização
    '''
    print('Obrigado por utilizar nosso programa!!!') 
else:
    '''
    o programa volta ao inicio e segue seu fluxo!!!
    '''
    ...