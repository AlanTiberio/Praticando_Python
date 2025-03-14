'''
Importar a função de limpeza do terminal
'''
import os

'''
Titulo do meu código
'''
print('PRATICANDO LISTAS COMBINADA COM FUNÇÕES EM PYTHON \n')


'''
Toda vez que o usuário desejar realizar uma alteração em sua lista após uma atualização, 
ele pode retornar ao menu em questão "[i]nserir [a]pagar [l]istar" até sair do loop.
Para sair do loop, basta digitar qualquer letra diferente de 's'
'''
modificarLista = 's'

'''
Cria uma lista que irá coletar os números digitados pelo usuário
'''
listaDeNumerosDoUsuario = []



while modificarLista == 's':
    '''
    Pedira o usuário para escolher uma das opções
    '''
    os.system('cls')
    opcao = input('Digite Uma Opção: \n [i]nserir [a]pagar [l]istar.: ')
    '''
    Opção de Inserir
    '''
    if opcao == 'i':
        # Pedirá para o usuario para incluir um número para calculo
        numeroDigitado = input('Valor a ser adicionado para calculo.: ')
        numeroInteiro = int(numeroDigitado)
        '''
        Valida se o que o usuário digitou é um número
        '''
        if numeroInteiro == int(numeroDigitado):
            '''
            Realiza a  conversão do dados digitado em número inteiro e
            retorna ao usuario com a informação de que o valor foi incluido na lista
            '''
            listaDeNumerosDoUsuario.append(int(numeroDigitado))
            print(f'Você adicionou o item: {numeroDigitado} em sua lista.')
            '''
            Informa se o usuário deseja continuar inserindo números.
            Caso a resposta seja diferente de "s"(sim) o sistema se encerrará
            '''
            modificarLista = input('Deseja realizar mais alterações? Digite "s" para continuar.: ')   
        
        else:
            '''
            Caso o usuario não digite um número, apresentara o erro abaixo e dará a 
            opção de voltar ao menu inicial.
            '''
            print(f'Erro! Digite apenas números!!!')
            modificarLista = input('Deseja realizar mais alterações? Digite "s" para continuar.: ') 


    #OPÇÃO [A]PAGAR
    elif opcao == 'a':
        '''
        Exibe a lista de números junto com seu índice
        '''
        for indice, numeroInteiro in enumerate(listaDeNumerosDoUsuario):
            print(indice,numeroInteiro)

        '''
        Pede para o usuário digitar um número (índice) para que seja selecionado para retirada da lista
        '''
        digitarNumeroDaLista = input('Digite o número do item da lista que deseja apagar.: ')
        numeroDaLista = int(digitarNumeroDaLista)
        '''
        Verifica se o dado digitado é um número
        '''
        #if digitarNumeroDaLista.isnumeric() == True:
        if numeroDaLista == int(digitarNumeroDaLista):
            numeroDaLista = int(digitarNumeroDaLista)

        else:
            '''
            Caso o valor digitado não seja um número, retornará o erro abaixo e perguntando se o usuário
            deseja seguir no sistema
            '''
            print(f'Erro! Digite apenas o número do indice (primeira coluna) para devida tratativa!!!')
            modificarLista = input('Deseja realizar mais alterações? Digite "s" para continuar.: ')    

        '''
        Após validar se o dados inserido e um número, vamos verificar se o indice se
        encontra na lista
        '''
        if (numeroDaLista <= len(listaDeNumerosDoUsuario)) and (numeroDaLista >= 0):
            '''
            Caso o número se encontra, ele retorna o valor a ser excluido pelo usuario e solicita a confirmação
            de tal ato
            '''
            print(f'Deseja excluir o número {listaDeNumerosDoUsuario[numeroDaLista]} da sua lista de calculo?')
            confirmaExclusaoDeNumero = input('Digite "s" para continuar.: ')

            if confirmaExclusaoDeNumero == 's':
                '''
                Caso a resposta seja s(sim) iremos executar o comando de exclusão daquele dada na lista
                '''
                print(f'O número {listaDeNumerosDoUsuario[numeroDaLista]} foi apagado de sua lista?')
                listaDeNumerosDoUsuario.pop(numeroDaLista)
                modificarLista = input('Deseja realizar mais alterações? Digite "s" para continuar ')

            else:
                '''
                Caso usuário digite qualquer coisa diferente de s(sim) retorna a setença abaixo.
                '''
                print(f'Operação cancelada!!!')
                print(f'Nenhuma alteração foi feita!!!')
                modificarLista = input('Deseja realizar mais alterações? Digite "s" para continuar ')
        
        else:
            '''
            Caso usuário não digite um número, será dado o retorno abaixo
            '''
            print(f'Operação cancelada!!!')
            print(f'Verifique o índice digitado: {numeroDaLista}')
            print(f'Nenhuma alteração foi feita!!!')
            modificarLista = input('Deseja realizar mais alterações? Digite "s" para continuar ')

    #OPÇÃO [L]ISTAR
    elif opcao == 'l':
        '''
        Mostra a lista de números digitados pelo usuário
        '''
        print('Segue os números digitados até aqui:')
        print(listaDeNumerosDoUsuario)
        modificarLista = input('Deseja realizar mais alterações? Digite "s" para continuar ')              

    else:
        '''
        Caso o usuário digite qualquer opção diferente de [i]nserir [a]pagar [l]istar
        será dado o retorno abaixo
        '''
        print('Opção Inválida!!! Número digitado não existe na lista')
        modificarLista = input('Deseja continuar? Digite "s" para continuar ')

'''
Criando o sistema de Calculo
'''
sistemaDeCalculo = 's'

while sistemaDeCalculo == 's':
    '''
    Limpeza do terminal
    '''
    os.system('cls')
    '''
    Exibe na tela os números digitados pelo usuário
    '''
    print(f'Segue sua lista de números: \n {listaDeNumerosDoUsuario} \n')

    '''
    Solicitará qual operação o usuário deseja realizar com os números digitados
    '''
    print('\n Qual Tipo de Calculo deseja realizar?')
    tipoDeCalculo = input('[a]dição  [s]ubtração [m]ultiplicação [d]ivisão? .:')

    '''
    Declamação das função em ordem:
    - adição
    - subtração
    - multiplicação
    - divisão
    '''
    def adicao(*args):
        total = 0
        for numero in args:
            total += numero
        return total

    def subtracao(*args):
        total = 0
        for numero in args:
            total -= numero
        return total

    def multiplicacao(*args):
        total = 1
        for numero in args:
            total *= numero
        return total

    def divisao(*args):
        total = 1
        for numero in args:
            total /= numero
        return total

    '''
    Calculo será realizado de acordo com a opção escolhida pelo usuário:
    [a]dição  [s]ubtração [m]ultiplicação [d]ivisão

    '''

    #CALCULO DE ADIÇÃO
    if tipoDeCalculo == 'a':
        calcularAdicao = adicao(*listaDeNumerosDoUsuario)
        print(f'a adição dos números {listaDeNumerosDoUsuario} foi de: {calcularAdicao}')
        sistemaDeCalculo = input('Deseja realizar uma nova Operação? Digite "s" para continuar.: ')

    #CALCULO DE SUBTRAÇÃO
    elif tipoDeCalculo == 's':
        calcularSubtracao = subtracao(*listaDeNumerosDoUsuario)
        print(f'a subtração dos números {listaDeNumerosDoUsuario} foi de: {calcularSubtracao}')   
        sistemaDeCalculo = input('Deseja realizar uma nova Operação? Digite "s" para continuar.: ')

    #CALCULO DE MULTIPLICAÇÃO
    elif tipoDeCalculo == 'm':
        calcularMultiplicacao = multiplicacao(*listaDeNumerosDoUsuario)
        print(f'a multiplicação dos números {listaDeNumerosDoUsuario} foi de: {calcularMultiplicacao}')
        sistemaDeCalculo = input('Deseja realizar uma nova Operação? Digite "s" para continuar.: ')

    #CALCULO DE DIVISÃO
    elif tipoDeCalculo == 'd':
        calcularDivisão = divisao(*listaDeNumerosDoUsuario)
        print(f'a divisão dos números {listaDeNumerosDoUsuario} foi de: {calcularDivisão}')        
        sistemaDeCalculo = input('Deseja realizar uma nova Operação? Digite "s" para continuar.: ')

print('FIM DO PROGRAMA!!! OBRIGADO POR USAR : )')   