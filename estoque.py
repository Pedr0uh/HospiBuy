from conexao import cursor

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
'''\n--- Como deseja procurar ? ---
1.Por sku
2.Por nome
3.Por tipo
4.local
5.Voltar para o menu'''
                )
            subopcao = int(input('\nSelecione uma opção: '))

            match subopcao:
                case 1:
                    sku = (input('\nDigite o sku do item: '))

                    query = "SELECT * FROM produto WHERE sku = %s"
                    valores = (sku, )

                    cursor.execute(query, valores)

                    resultado = cursor.fetchone()

                    if resultado:
                        print("\nItem encontrado:\n")
                        print(f"SKU: {resultado['sku']} | "
                        f"Nome: {resultado['descricao']} | "
                        f"Tipo: {resultado['tipo']} | "
                        f"Local: {resultado['localizacao']} | "
                        f"Quantidade: {resultado['quantidade']} | "
                        f"lote: {resultado['lote']}\n"
                        )
                    else:
                        print("\nItem não encontrado no estoque.\n")

                case 2:
                    descricao = str(input('Digite a descricao do item: '))

                    query = "SELECT * FROM produto WHERE descricao = %s"
                    valores = (f"%{descricao}%", )

                    cursor.execute(query, valores)

                    resultado = cursor.fetchall()

                    if resultado:
                        for item in resultado:
                            print("\nItem encontrado:\n")
                            print(f"SKU: {item['sku']} | "
                            f"Nome: {item['descricao']} | "
                            f"Tipo: {item['tipo']} | "
                            f"Local: {item['localizacao']} | "
                            f"Quantidade: {item['quantidade']} | "
                            f"lote: {item['lote']}\n"
                            )
                    else:
                        print("\nItem não encontrado no estoque.\n")

                case 3:
                     tipo1 = str(input('Digite o tipo :'))
                case 4:
                    local1 = str(input('Digite o local :'))
                case 5:
                    print("Voltando para o menu...")
                    i = 1
                    return
                case _:
                    print ('\nOpção nao encontrada!')
                    contador += 1
            
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

