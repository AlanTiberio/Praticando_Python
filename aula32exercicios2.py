"""
EXERCICIO 2
Faça um programa que pergunte a hora ao usuário e , baseando-se no hodario
descrito, exiba a saudação apropriada. Ex:
Bom da 0-11, Boa tarde 12-17 e Boa Noite 18-23
"""


print('EXERCICIO 2 - Feito Por Mim \n')

hora_str = input('Informe a Hora.: ')
minuto_str = input('Informe o Minuto.: ')

try:

    hora = int(hora_str)
    minuto = int(minuto_str)

    madrugada = hora >= 0 and hora <= 5
    dia = hora > 5 and hora <= 11
    tarde = hora > 11 and hora <= 17
    noite = hora > 17 and hora <= 23
    minutof = minuto >=0 and minuto <=59


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

except ValueError:
    print(f'Verifique a hora e minuto digitados!!!')

print('-' * 90)

"""
EXERCICIO 2 - Feito Pelo Professor
"""

print('EXERCICIO 2 - Feito Pelo Professor \n')

horas = input("Que hora é: ")
horas_int = int(horas)

if horas_int >= 0 and horas_int <= 11:
    print('Bom dia!')
elif horas_int > 11 and horas_int <= 17:
    print('Boa tarde!')
elif horas_int > 17 and horas_int <= 23:
    print('Boa noite!')
