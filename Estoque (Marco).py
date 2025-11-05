def erro():
    
    print("\nmuitas tentativas invalidas\n")
    return

def estoque():
    contador = 0
    
    while True : 
        
        if contador >= 5:
            erro()
            break
        
        print ('\n---- ESTOQUE HOSPYBUY ----\n')
        print ('O que deseja fazer ?')
        print ('1.Cadastrar item')
        print ('2.Procurar no estoque')
        print ('3.Remover item')
        print ('4.Buscar item\n')
        opcao = int(input('Selecione uma opção :'))
    
        if opcao == 1:
            nome = str(input('Digite o nome do item :'))
            tipo = str(input('Digite o tipo do item :'))
            quantidade = int(input('Digite a quantidade :'))
            validade = int(input('Digete a validade :'))
            local = str(input('Digite o local :'))
            print ('Novo produto cadastrado com sucesso :')
            
    
        elif opcao == 2:
            ide = int(input('Digite o id do item :'))
            nome1 = str(input('Digite o nome do item :'))
            tipo1 = str(input('Digite o tipo :'))
            quantidade1 = int(input('Digite  a quantidade :'))
            local1 = str(input('Digite o local :'))
            
    
        elif opcao == 3:
            nome3 = str(input('Escreva o nome do item/cod que deseja remover :'))
            
        elif opcao == 4:
            nome3 = str(input('Escreva o nome do item :' ))
            ide1 = int(input('Digite o id do item :'))
            
        else:
            print ('\nOpção nao encontrada!')
            contador += 1

print('\nObrigado por usar o sistema de estoque HOSPYBUY!\n')
