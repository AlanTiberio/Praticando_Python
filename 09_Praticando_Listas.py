'''
Praticando a função de listas
'''

print('CRIANDO NA LISTA DE COMPRAS \n')

# Importar a função de limpeza do terminal
import os

# Criar um loop infinito chamado de sistema e uma lista de compras vazias para armazenar os dados
sistema = 's'
listaDeCompras = []

# Enquanto sisema for verdadeiro('s') o loop em questão vai rodar.
while sistema == 's':
    # Pedira o usuário paraescolher uma das opções, sendo que cada uma delas acionar um if
    os.system('cls')
    opcao = input('Digite Uma Opção: \n [i]nserir [a]pagar [l]istar.: ')

    # Opção de Inserir
    if opcao == 'i':
        # Pedirá para o usuario escrever o que deseja inserir na lista e incluirá
        item = input('O que você deseja adicionar a lista? ')       
        listaDeCompras.append(item)
        # Retorna informando que o item escrito foi incluido na lista
        print(f'Você adicionou o item: {item} em sua lista.')
        # Informa se o usuário deseja seguir editando sua lista.
        # Caso a resposta seja diferente de "S"(sim) o sistema se encerrencerrará
        sistema = input('Deseja realizar mais alterações? Digite "S" para continuar ')

    # Opção de Apagar
    elif opcao == 'a':
        # Pede para o usuário digitar um número (índice) para que seja selecionado para retirada da lista
        item = input('Digite o número do item que deseja apagar.: ')

        try:
            # Tenta converter o valor digitado pelo usuário em número
            apagar = int(item)
            
            # Caso o número digitado seja maior que o tamanho da lista retorna a setença abaixo
            if apagar > len(listaDeCompras):
                print(f'O item de número "{apagar}" não foi encontrado na sua lista de compras.')
                # Informa se o usuário deseja seguir editando sua lista.
                # Caso a resposta seja diferente de "S"(sim) o sistema se encerrencerrará
                sistema = input('Deseja realizar mais alterações? Digite "S" para continuar ')
            
            else:    
                # de acordo com o número digitado, busca na lista o nome do item e ... 
                # pergunta ao usuário se deseja o cancelamento         
                print(f'Deseja confirmar a exclusão do item "{listaDeCompras[apagar]}" da sua lista de compras?')
                confirmar_exclusão = input ('Digite a letra "s" para continuar... ')

                # Se usuário digitar a letra "s"(sim) seguirá com a exclusão do item na lista             
                if confirmar_exclusão == 's':
                    listaDeCompras.pop(apagar)
                    print(f'Você apagou o item de número {apagar} de sua lista de compras.')
                    # Informa se o usuário deseja seguir editando sua lista.
                    # Caso a resposta seja diferente de "S"(sim) o sistema se encerrencerrará
                    sistema = input('Deseja realizar mais alterações? Digite "S" para continuar ')

                # Qualquer coisa diferente de "s" a exclusão não seguirá e a lista permanecerá inalterada           
                else:
                    print(f'Operação cancelada! A Sua lista de compras não foi alterada!!!')
                    # Informa se o usuário deseja seguir editando sua lista.
                    # Caso a resposta seja diferente de "S"(sim) o sistema se encerrencerrará
                    sistema = input('Deseja realizar mais alterações? Digite "S" para continuar ')  
        
        # Caso o colaborador digite qualquer valor diferente de número será reportado tal erro             
        except ValueError:
            print('Digite um Numero Válido!!!')
            # Informa se o usuário deseja seguir editando sua lista.
            # Caso a resposta seja diferente de "S"(sim) o sistema se encerrencerrará
            sistema = input('Deseja realizar mais alterações? Digite "S" para continuar ')
            
    elif opcao == 'l':
        os.system('cls')
        # Caso a lista estiver vazia retorna a mensagem abaixo
        if listaDeCompras == []:
            print('Sua Lista de Compras Está Vazia!!!')
            # Informa se o usuário deseja seguir editando sua lista.
            # Caso a resposta seja diferente de "S"(sim) o sistema se encerrencerrará
            sistema = input('Deseja realizar mais alterações? Digite "S" para continuar ')

        else:
            # Caso a lista tenha lista, a mesma será exibida junto com seu índice
            print(f'SEGUE SUA LISTA DE COMPRAS:')
            for indice, item in enumerate(listaDeCompras):
                print(indice,item)
            # Informa se o usuário deseja seguir editando sua lista.
            # Caso a resposta seja diferente de "S"(sim) o sistema se encerrencerrará    
            sistema = input('Deseja realizar mais alterações? Digite "S" para continuar ')

    else:
        # Caso usuário digite qualquer coisa iferente das opções ofertadas ("i","a","l")
        print('opção Inválida!!!')  
        opcao = input('Digite Uma Opção: \n [i]nserir [a]pagar [l]istar ')

os.system('cls')
# Caso o retorno da pergunta: "Deseja realizar mais alterações? Digite "S" para continuar"
# diferente de sim("s") o programa será finalizado
print('Programa Finalizado!!! Até a Próxima!!!')