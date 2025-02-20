print('VERIFICAR O SEU NOME \n')

# Solicita o usuário a inserir seu primeiro nome
nome = input('Informe o seu primeiro nome.: ')

# Retorna a quant de letras que o nome possui
quantLetras = len(nome)

# Setença sendo determinada de acordo com a quant de letras do nome
nome_pequeno = (quantLetras <= 4) and (nome.isalpha() == True)
nome_normal = (quantLetras > 4 and  quantLetras <= 6) and (nome.isalpha() == True)
nome_grande = (quantLetras > 6) and (nome.isalpha() == True)

# Retorna a setença de acordo com as validações acima
if nome_pequeno :
    print(f'Seu nome é pequeno, pois possui apenas {quantLetras} letras')

elif nome_normal:
    print(f'Seu nome é normal, pois possui apenas {quantLetras} letras')

elif nome_grande :
    print(f'Seu nome é grande, pois possui apenas {quantLetras} letras')

# Retorno caso o colaborador digite algo diferente de letra no campo "'Informe o seu primeiro nome.:"
else :
    print(f'Digite Apenas Letras no campo "Informe o seu primeiro nome"')