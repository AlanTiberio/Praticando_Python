
print('COMPARAÇÃO DE NÚMEROS')

# Solicita que o usuário digite dois números
primeiro_valor = input("Digite o Primeiro Valor Inteiro: ")
segundo_valor = input("Digite o Segundo Valor Inteiro: ")

# Verifica se o que foi digitado é número
if primeiro_valor.isdigit and segundo_valor.isdigit:

    # Atribue os valores digitados para variaveis
    valor1 = int(primeiro_valor)
    valor2 = int(segundo_valor)

    # Compara os valores e retorna o resultado
    if valor1 > valor2 :
        print(f"O primeiro valor: {valor1} é MAIOR que o segundo valor: {valor2}")
    elif valor1 < valor2 :
        print(f"O segundo valor: {valor2} é MAIOR que o primeiro valor: {valor1}")
    else  :
        print(f"O primeiro valor: {valor1} é IGUAL que o segundo valor: {valor2}")

else:
    # Caso o usuário não digite um numero retorna a setença abaixo
    print('Verifique os valores Digitados!!!')