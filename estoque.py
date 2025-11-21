from conexao import cursor
from conexao import conn
from main import cnes

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
        
        print ('\n---- ESTOQUE HOSPIBUY ----\n')
        print ('O que deseja fazer ?\n')
        print ('    1.Procurar no estoque')
        print ('    2.Remover item')
        print ('    3.Adicionar item')
        print ("    4.Voltar para o menu\n")
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
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print(f"SKU: {resultado['sku']} | "
                        f"Nome: {resultado['descricao']} | "
                        f"Tipo: {resultado['tipo']} | "
                        f"Local: {resultado['localizacao']} | "
                        f"Quantidade: {resultado['quantidade']} | "
                        f"lote: {resultado['lote']}\n")
                        print("---------------------------------------------------------------------------------------------------------------------")

                    else:
                        print("\nItem não encontrado no estoque.\n")

                case 2:
                    descricao = str(input('Digite a descricao do item: '))

                    query = "SELECT * FROM produto WHERE descricao LIKE %s"
                    valores = (f"%{descricao}%", )

                    cursor.execute(query, valores)

                    resultado = cursor.fetchall()

                    if resultado:
                        print("\nItem encontrado:\n")

                        for item in resultado:    
                            print("---------------------------------------------------------------------------------------------------------------------")
                            print(f"SKU: {item['sku']} | "
                            f"Descricao: {item['descricao']} | "
                            f"Tipo: {item['tipo']} | "
                            f"Local: {item['localizacao']} | "
                            f"Quantidade: {item['quantidade']} | "
                            f"lote: {item['lote']}")
                            print("---------------------------------------------------------------------------------------------------------------------")
                            
                    else:
                        print("\nItem não encontrado no estoque.\n")

                case 3:
                     tipo = str(input('Digite o tipo :'))

                     query = "SELECT * FROM produto WHERE tipo LIKE %s"
                     valores = (f"%{tipo}%", )

                     cursor.execute(query, valores)

                     resultado = cursor.fetchall()

                     if resultado:
                        print("\nItem encontrado:\n")

                        for item in resultado:    
                            print("---------------------------------------------------------------------------------------------------------------------")
                            print(f"SKU: {item['sku']} | "
                            f"Descricao: {item['descricao']} | "
                            f"Tipo: {item['tipo']} | "
                            f"Local: {item['localizacao']} | "
                            f"Quantidade: {item['quantidade']} | "
                            f"lote: {item['lote']}")
                            print("---------------------------------------------------------------------------------------------------------------------")
                            
                     else:
                        print("\nItem não encontrado no estoque.\n")
            
                case 4:
                    local = str(input('Digite o local:'))

                    query = "SELECT * FROM produto WHERE localizacao LIKE %s"
                    valores = (f"%{local}%", )

                    cursor.execute(query, valores)

                    resultado = cursor.fetchall()

                    if resultado:
                        print("\nItem encontrado:\n")

                        for item in resultado:    
                            print("---------------------------------------------------------------------------------------------------------------------")
                            print(f"SKU: {item['sku']} | "
                            f"Descricao: {item['descricao']} | "
                            f"Tipo: {item['tipo']} | "
                            f"Local: {item['localizacao']} | "
                            f"Quantidade: {item['quantidade']} | "
                            f"lote: {item['lote']}")
                            print("---------------------------------------------------------------------------------------------------------------------")
                            
                    else:
                        print("\nItem não encontrado no estoque.\n")

                case 5:
                    print("Voltando para o menu...")
                    i = 1
                    return
                case _:
                    print ('\nOpção nao encontrada!')
                    contador += 1
            
        elif opcao == 2:
            sku = str(input('Escreva o sku que deseja remover: '))

            query = "SELECT * FROM produto WHERE sku = %s"
            valores = (sku, )

            cursor.execute(query, valores)

            resultado = cursor.fetchone()

            if resultado:
                print("\nItem encontrado:\n")  
                print("---------------------------------------------------------------------------------------------------------------------")
                print(f"SKU: {resultado['sku']} | "
                f"Descricao: {resultado['descricao']} | "
                f"Tipo: {resultado['tipo']} | "
                f"Local: {resultado['localizacao']} | "
                f"Quantidade: {resultado['quantidade']} | "
                f"lote: {resultado['lote']}")
                print("---------------------------------------------------------------------------------------------------------------------")

                confirmar = str(input('\nTem certeza que deseja remover este item ? (s/n): '))

                if confirmar.lower() == 's':

                    delete_query = "DELETE FROM produto WHERE sku = %s"
                    delete_valores = (sku, )

                    cursor.execute(delete_query, delete_valores)
                    conn.commit()

                    print("""\n
-------------------------------  
   Item removido com sucesso!
------------------------------- 
                          \n""")

                else:
                    print("""\n
------------------------------  
        Remocao cancelada!
------------------------------  
                          \n""")
            else:
                print("\nItem não encontrado no estoque.\n")
            
        elif opcao == 3:

            sku = str(input('Escreva o SKU do item :' ))
            descricao = str(input('Digite o descricao do item :'))
            quantidade = int(input('Digite a quantidade do item :'))
            tipo = str(input('Digite o tipo do item :'))
            data_compra = str(input('Digite a data de compra do item (YYYY-MM-DD) :'))
            lote = str(input('Digite o lote do item :'))
            validade = str(input('Digite a validade do item (YYYY-MM-DD) :'))
            localizacao = str(input('Digite a localizacao do item :'))
            ID_fornecedor = int(input('Digite o ID do fornecedor :'))
            
            insert_query = """INSERT INTO produto 
            (sku, descricao, quantidade, tipo, data_compra, lote, validade, localizacao, ID_fornecedor, cnes) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            insert_valores = (sku, descricao, quantidade, tipo, data_compra, lote, validade, localizacao, ID_fornecedor, cnes)

            cursor.execute(insert_query, insert_valores)
            conn.commit()

            print("""\n
-------------------------------
  Item adicionado com sucesso!
------------------------------- 
                          \n""")

            
        elif opcao == 4:
            print("Voltando para o menu...")
            i = 1
            return
            
    
        else:
            print ('\nOpção nao encontrada!')
            contador += 1

