'''
Site para geração de CPF para testes:
https://www.4devs.com.br/gerador_de_cpf
'''

'''Importando limpeza de terminal, sendo que
    - Para linux e mac usa-se a palavra 'clear'
    - Para windows(sistema qual utilizo), usaa-se a palavra 'cls'
'''    
import os

# Titulo do meu Programa
print("VALIDADOR DE CPF\n")

'''
Cria uma condição para o sistema rode quantas vezes o usuário desejar
    - Enquanto o usuario responder a pegunta com a letra "s" o sistema/cógigo rodará
'''
sistemaVerificarCPF = 's'
while sistemaVerificarCPF == 's':  

    #Solicita o usuário a digitar o seu CPF
    cpf = input('Digite Seu CPF (apenas números).: ')

    try:

        # Cria Uma lista vazia para alocação dos digitos do CPF
        listaNumCPF = []

        # Verifica se o usuário encaminhou dados sequenciais

        cpfSequencial = cpf == cpf[0] * len(cpf)

        # Passará número por número digitado pelo usuário na alocação dos mesmos dentro da lista
        for item in cpf:
            listaNumCPF.append(item) 

        #Caso o usuário digite um sequencia de números(Ex.: 11111111111) apresentará o erro abaixo
        if cpfSequencial:
            os.system('cls')
            print('Erro!! Você digitou números em sequência. Verifique os dados digitados e tente novamente')
            print(f'Dados Digitados.: {cpf}')
            print('Deseja fazer uma nova consulta?')
            sistemaVerificarCPF = input('Digite a letra "s" para sim ou a letra "n" para não .:' )           

        # Caso minha lista de número fique com 11 item, o mesmo executará o cógido a seguir
        elif len(listaNumCPF) == 11:
            # Realizando o calculo do primeiro digito
            # Realizara a multiplicação de cada número de acordo com a regra do cpf
            dig01 = 10 * int(listaNumCPF[0])
            dig02 =  9 * int(listaNumCPF[1])
            dig03 =  8 * int(listaNumCPF[2])
            dig04 =  7 * int(listaNumCPF[3])
            dig05 =  6 * int(listaNumCPF[4])
            dig06 =  5 * int(listaNumCPF[5])
            dig07 =  4 * int(listaNumCPF[6])
            dig08 =  3 * int(listaNumCPF[7])
            dig09 =  2 * int(listaNumCPF[8])
            '''
            Após a multiplicação de cada um dos números, o mesmo será somada e logo em seguida, será calculado sua sobra onde:
                - verificarDigito01 < 2 o primeiro digito verificado do CPF será zero 
                - Caso contrario o resto da divisão que será o digito verificador
            '''
            verificarDigito01 = (dig01 + dig02 + dig03 + dig04 + dig05 + dig06 + dig07 + dig08 + dig09)%11

            if verificarDigito01 < 2:
                verificarDigito01 = 0
            else:    
                verificarDigito01 = 11-verificarDigito01

            # Realizando o calculo do segundo digito  
            # Realizara a multiplicação de cada número de acordo com a regra do cpf
            dig01 = 11 * int(listaNumCPF[0])
            dig02 = 10 * int(listaNumCPF[1])
            dig03 =  9 * int(listaNumCPF[2])
            dig04 =  8 * int(listaNumCPF[3])
            dig05 =  7 * int(listaNumCPF[4])
            dig06 =  6 * int(listaNumCPF[5])
            dig07 =  5 * int(listaNumCPF[6])
            dig08 =  4 * int(listaNumCPF[7])
            dig09 =  3 * int(listaNumCPF[8])
            dig10 =  2 * int(listaNumCPF[9])

            verificarDigito02 = (dig01 + dig02 + dig03 + dig04 + dig05 + dig06 + dig07 + dig08 + dig09 + dig10)%11

            if verificarDigito02 < 2:
                verificarDigito02 = 0
            else:    
                verificarDigito02 = 11-verificarDigito02

            '''
            Formata o CPF no seu padrão de visualização (000.000.000-00) para que seja demonstrado na tela 
            de acordo com o resultado da verificação dos digitos
            '''
            pt01 = (listaNumCPF [0]+listaNumCPF [1]+listaNumCPF [2])
            pt02 = (listaNumCPF [3]+listaNumCPF [4]+listaNumCPF [5])
            pt03 = (listaNumCPF [6]+listaNumCPF [7]+listaNumCPF [8])
            pt04 = (listaNumCPF [9]+listaNumCPF [10])
            cpfFinal = f'{pt01}.{pt02}.{pt03}-{pt04}'
  
            # Valida se o CPF digitado está válido
            if int(listaNumCPF[9]) == verificarDigito01 and int(listaNumCPF[10]) == verificarDigito02:
                os.system('cls')
                print(f'O cpf {cpfFinal} é valido')
                print('Deseja fazer uma nova consulta?')
                sistemaVerificarCPF = input('Digite a letra "s" para sim ou a letra "n" para não .:' )
                os.system('cls')
            else:
                os.system('cls')
                print(f'O cpf {cpfFinal} é invalido')
                print('Deseja fazer uma nova consulta?')
                sistemaVerificarCPF = input('Digite a letra "s" para sim ou a letra "n" para não .:' )
                os.system('cls')

        # Caso a lista contem uma quantidade menos do que 11 itens, apresentará o erro a seguir.
        elif len(listaNumCPF) < 11:
            os.system('cls')
            print('Erro!! Você digitou dados que não deveria. Verifique os dados digitados e tente novamente')
            print(f'Dados Digitados.: {cpf}')
            print('Deseja tentar novamente?')
            sistemaVerificarCPF = input('Digite a letra "s" para sim ou a letra "n" para não .:' )
            os.system('cls')

        # Caso a lista contem uma quantidade maior do que 11 itens, apresentará o erro a seguir.
        elif len(listaNumCPF) > 11:
            os.system('cls')
            print('Erro!! Você digitou dados que não deveria. Verifique os dados digitados e tente novamente')
            print(f'Dados Digitados.: {cpf}')
            print('Deseja tentar novamente?')
            sistemaVerificarCPF = input('Digite a letra "s" para sim ou a letra "n" para não .:' )
            os.system('cls')

    except ValueError:
        # Caso o colaborador digite outros caracteres que não sejam números, apresentará o erro abaixo
        os.system('cls')
        print('Erro!! Você digitou dados que não deveria')
        print('Digite apenas números no campo "Digite Seu CPF (apenas números).:!!!"')
        print(f'Dados Digitados.: {cpf}')
        print('Deseja tentar novamente?')
        sistemaVerificarCPF = input('Digite a letra "s" para sim ou a letra "n" para não .:' )
        os.system('cls')

os.system('cls')
print('Programa Encerrado!!! Até a Proxima!!!!')