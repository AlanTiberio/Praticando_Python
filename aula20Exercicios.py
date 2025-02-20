primeiro_valor = input("Digite o Primeiro Valor: ")
segundo_valor = input("Digite o Segundo Valor: ")

valor1 = int(primeiro_valor)
valor2 = int(segundo_valor)

if valor1 > valor2 :
    print(f"O primeiro valor: {valor1} é MAIOR que o segundo valor: {valor2}")
elif valor1 < valor2 :
    print(f"O segundo valor: {valor2} é MAIOR que o primeiro valor: {valor1}")
else  :
    print(f"O primeiro valor: {valor1} é IGUAL que o segundo valor: {valor2}")