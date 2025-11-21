
def erro():
    
    print("\nmuitas tentativas invalidas\n")
    return

def estoque():
    contador = 0
    i = 0

    while i == 0 : 
        
        if contador >= 5:
            erro()
            break
        
        print ('\n---- ESTOQUE HOSPYBUY ----\n')
        print ('O que deseja fazer ?')
        print ('1.Procurar no estoque')
        print ('2.Remover item')
        print ('3.Buscar item')
        print ("4.Voltar para o menu\n")
        opcao = int(input('Selecione uma opção :'))
   
        if opcao == 1:
            print(

                
            )

            ide = int(input('Digite o sku do item :'))
            nome1 = str(input('Digite o nome do item :'))
            tipo1 = str(input('Digite o tipo :'))
            quantidade1 = int(input('Digite  a quantidade :'))
            local1 = str(input('Digite o local :'))
            
    
        elif opcao == 2:
            nome3 = str(input('Escreva o nome do item/cod que deseja remover :'))
            
        elif opcao == 3:
            nome3 = str(input('Escreva o nome do item :' ))
            ide1 = int(input('Digite o id do item :'))
            
        elif opcao == 4:
            print("Voltando para o menu...")
            i = 1
            return
            
    
        else:
            print ('\nOpção nao encontrada!')
            contador += 1

