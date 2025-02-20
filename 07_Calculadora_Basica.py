print('Calculadora Feita Por Mim \n')

while True:
    
    '''
    Solicita o usuário a digitar dois números
    '''
    num1 = input('Digite um Número.: ')
    num2 = input('Digite outro Número.: ')

    '''
    Solicita o usuário a digitar um operador sendo:
    - Soma(+)
    - Subtração(-)
    - Multiplicação(*)
    - Divisão(/)
    '''
    operador = input('Digite Apenas Um Operador (+ - * /).: ')
    operadores_permitidos = '+-*/'

    '''
    Verificar se os dados que o usuário digitou são validados, sendo que:
    - (num1.isdigit() == True and num2.isdigit() == True) -----> Verifica se o usuario digitou dois números no campos num1 e num2 respectivamente;
    - len(operador) == 1 --------------------------------------> Verifica se o usuário digitou apenas um caractere;
    - operador in operadores_permitidos -----------------------> Verifica que o caractere digitado no campo operador é valido ('+' , '-', '/' ou '*');
    '''
    verificacao_de_dados = (num1.isdigit() == True and num2.isdigit() == True) and \
                            len(operador) == 1 and \
                            operador in operadores_permitidos
    
    '''
    Caso a sentença verificacao_de_dados for verdadeira, será executado o código a seguir, onde:
    - numOne e numTwo receberão os valores de num1 e num2 respectivamente convertidos em float (decimal)
    - será executada a operação de acordo com o sinal indicado pelo usuário ('+' , '-', '/' ou '*')
    - O else dessa sentença retorna"'Erro!!! Contate o Administrador do Sistema!!!!'", porém, nunca ocorrerá tal erro, uma vez que todas possibilidades
      foram validadas nos elif anteriores
    '''
    if verificacao_de_dados == True:

        numOne = float(num1)
        numTwo = float(num2)

        if operador == '+':
            print(f'A soma dos valores {numOne} e {numTwo} é...: ', numOne + numTwo)

        elif operador == '-':
            print(f'A subtração dos valores {numOne} e {numTwo} é...: ', numOne - numTwo)

        elif operador == '*':
            print(f'A multiplicação dos valores {numOne} e {numTwo} é...: ', numOne * numTwo)    

        elif operador == '/':
            print(f'A divisão dos valores {numOne} e {numTwo} é...: ', numOne / numTwo)

        else:
            print(f'Erro!!! Contate o Administrador do Sistema!!!!')

        '''
    Caso a setetença verificacao_de_dados for falsa, será executado o código a seguir (else), onde:
    - Apresentara a mensagem de erro: "Erro em um dos valores digitados!!!"
    - Informara os dados digitados pelo usuário (primeiro e segundo números, além do operador)
    - Apresentara a mensagem de erro: VERIFIQUE OS NÚMEROS E OPERADOR DIGITADOS!!!
    '''
    else:
        print(f'\n \
            Erro em um dos valores digitados!!! \n \
            Você digitou as seguintes informações Digite um Número.: {num1} \n \
            Digite outro Número.: {num2} \n \
            Digite Apenas Um Operador (+ - * /).: {operador} \n \
            VERIFIQUE OS NÚMEROS E OPERADOR DIGITADOS!!!')
        
    '''
    Perguntará ao usuário se deseja coninuar no programa
    - Caso o usuário digite qualquer coisa que começe com a letra "S" o programa reiniciaá, 
      caso contrario o programa se encerra com a mensagem: "Programa Finalizado!!!!"
    '''    
    FINALIZAR_PROGRAMA = input('Deseja Sair do Programa? [s]im x [n]ão ...:').lower().startswith('s')

    if FINALIZAR_PROGRAMA is True:
        print('Programa Finalizado!!!!')
        break