'''
Quam deseja ter acesso ao curso, segue link:

https://www.udemy.com/course/python-3-do-zero-ao-avancado/?srsltid=AfmBOopzELrr8O_3LNRY_iX2gNxc97u9NblVZg6O85DEWZCB-XOufF0x&couponCode=ST22MT240325G3
'''

print('EXERCICIO - SITEMA DE PERGUNTAS E RESPOSTAS')

print()
#Quadro de perguntas:
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opcoes': ['1','2','3','4','5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5x5 ?',
        'Opcoes': ['25','55','310','51','10'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2 ?',
        'Opcoes': ['4','5','2','1','0'],
        'Resposta': '5'
    },
    {
        'Pergunta': 'Quanto é 8 x 7 ?',
        'Opcoes': ['15','48','56','64','57'],
        'Resposta': '56'
    },
    {
        'Pergunta': 'Quanto é 186 - 132 ?',
        'Opcoes': ['46','54','24','56','37'],
        'Resposta': '54'
    },
]

#Contador de perguntas
qtd_perguntas = 1

#Contador de Acertos
qtd_acertos = 0

#Um de Para para passar por cada pergunta
for pergunta in perguntas:
    print(f'Pergunta {qtd_perguntas}:' , pergunta['Pergunta'])
    qtd_perguntas += 1
    print()
    
    #Outro De Para para passar nas opções enumerando de acordo com o índice cada opção
    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')

    #Solicitando o usuário a digitar uma opção/índice de acordo com o ofertado
    escolha = input('Escolha uma Opção.: ')

    #Variavel para retornar se o usuario acertou a resposta da pergunta
    acertou = False

    #Variavel que irá converter o valor digitado em número
    escolha_int = None

    #Variavel afim de verificar a quantidade de opções de resposta disponiveis em cada pergunta
    qtd_opcoes = len(opcoes)

    #Caso o usuario digite um número o mesmo será convertido em inteiro para a variavel escolha_int
    if escolha.isdigit():
        escolha_int = int(escolha)

    '''
    Caso o valor digitado pelo uisuario seja um número o mesmo for entre 0 e o tamanho da quantidade de opções
    ofertadas na questão vai verificar se a opção escolhida do usuario e a mesma da resposta, ou seja, verifica
    se a resposta foi respondida corretamente
    '''
    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()

    #Caso acerte, retorna a  primeira sentença, em caso de erro, retorna a segunda setença
    if acertou:
        qtd_acertos +=1
        print('Você Acertou 👍')
    else:
        print('Você Errou ❌')
        print(f'Você escolheu a opção: {opcoes[escolha_int]}')                
        print(f'A resposta correta é: {pergunta['Resposta']}')
    print()

# retorna a setença de acordo com a quant. de acertos do usuario.
if qtd_acertos >= 3:
    print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas!!!')
    print('Parabéns!!! Você Passou no Teste 🎉🎊🎉🎊🎉🎊🎉')
else:    
    print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas!!!')
    print('Que Pena!!! Você Não Passou no Teste 😭😭😢😢')