print('VERIFICANDO A HORA \n')

# Solicita ao usuario a digitar a hora e minuto
hora_str = input('Informe a Hora.: ')
minuto_str = input('Informe o Minuto.: ')

# Irá tentar executar o bloco try de acordo com os dados fornecidos pelo usuário
try:

    hora = int(hora_str)
    minuto = int(minuto_str)

    # Saudação a ser utilizada de acordo com a hora fornecida pelo usuário
    madrugada = hora >= 0 and hora <= 5
    dia = hora > 5 and hora <= 11
    tarde = hora > 11 and hora <= 17
    noite = hora > 17 and hora <= 23

    # Valida se o minuto digitado pelo usuario está correto
    minutof = minuto >=0 and minuto <=59

    '''
    Retorna a setença de acordo com os valores digitados...
    Atenção para hora que será configurada de acordo com os padrões "00:00"(hh:mm)
    '''
    if madrugada and minutof :
        print(f'Boa Madrugrada!!! São {hora:02d}:{minuto:02d}')
    elif dia and minutof :
        print(f'Bom Dia!!! São {hora:02d}:{minuto:02d}')
    elif tarde :
        print(f'Boa Tarde!!! São {hora:02d}:{minuto:02d}')

    elif noite and minutof :
        print(f'Boa Noite!!! São {hora:02d}:{minuto:02d}')

    else :
        print(f'Verifique a hora e minuto digitados!!!')

    '''
    Caso o usuário digite qualquer valor que nao seja número, será gerado o erro "ValueError",
    Com isso, será executado a setença excepty retornando a mensagem ao usuario:
    "Verifique a hora e minuto digitados!!!"
    '''
except ValueError:
    print(f'Verifique a hora e minuto digitados!!!')
