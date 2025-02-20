'''
importando os para realizar a limpeza do termninal assim que o usuário acertar a palavra
NOTA: Em alguns sistemas ir
'''
import os

# Definindo o nome do Loop (while)
descobrir_palavra_secreta = True

# Definindo a palavra secreta
palavra_secreta = 'programacao'

# Definindo a qvariavel que incluirá as letras acertadas
letras_acertadas = ''

# Contador de número de tentativas
numero_tentativas = 0

# Definindo um titulo ao meu projeto
print('DESCUBRA A PALAVRA SECRETA \n')

# Realizando uma breve descrição
print('Descubra a palavra secreta do sistema!\r')
print('Você pode digitar apenas uma letra por\r')
print('vez até realizar a formação da palavra \n')

while descobrir_palavra_secreta == True:

    # Solicita uma letra para o usuário
    letra_digitada = input('Digite uma letra.: ')
    numero_tentativas += 1

    '''
    Se usuário digitar no campo "Digite uma letra.:" mais de uma letra retorna o informativo
    "Digite Apenas Uma Única Letra!!!"
    '''
    if len(letra_digitada) > 1:
        print('Digite Apenas Uma Única Letra!!!')
        continue

    # Se a letra digitada estiver na palavra, a mesma sera acrescentada na váriavel "letras_acertadas"
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    '''
    Variavel criada para armazenar as letras (tanto as acertadas quanto a ainda serem descobertas)
    e que será impressa de acordo com as tentativas (Ex.: pro**g*ac*o)
    '''
    palavra_formada = ''

    #Para a letra secreta(ainda não descoberta)estiver na palavra secreta ...
    for letra_secreta in palavra_secreta:

        '''
        ...Será executado o 'Se', onde a letra digitada pelo usuario for uma das letras corretas 
        será armazenada na variavel "palavra_formada".
        Caso a letra digitada não corresponde a nennhuma letra da palavra, a mesma será 
        substituida pelo '*'
        '''
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'


    # Aqui será o resultado sempre em que o usuario digitar uma letra
    print('Palavra formada:', palavra_formada)

    # Caso o usuario acerte a palavra, sera apresentado a mensagens abaixo e finalizado o programa
    if palavra_formada == palavra_secreta:

        '''
        NOTA SOBRE O USO DO OS -> Em alguns sistemas operacionais, como algumas versões antigas do 
        windows, deve se utilizar a sigla 'cls', em outros como o mac, utiliza a palavra 'clean'
        Em caso de duvidas sobre a linha de cógigo abaixo, realizar consulta junto a documentação 
        do python:
        '''
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {numero_tentativas} x')
        print(f'ATÉ A PRÓXIMA!!!')

        # Após descobrir a palavra secreta a variavel em questão será falsa para que o loop se encerre
        descobrir_palavra_secreta = False