from conexao import cursor
from conexao import conn
from utils.select_produto import select_produto
import time

def erro():
    
    print("\nmuitas tentativas invalidas\n")
    return

def estoque(cnes):
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
        print ('    4.Atualizar item')
        print ("    5.Voltar para o menu\n")
        opcao = int(input('Selecione uma opção :'))
   
        if opcao == 1:
            print(
'''\n--- Como deseja procurar ? ---

    1.Por sku
    2.Por nome
    3.Por tipo
    4.local
    5.por lote
    6.Voltar para o menu'''
                )
            subopcao = int(input('\nSelecione uma opção: '))

            match subopcao:
                case 1:
                    select_produto("sku")

                case 2:
                   select_produto("descricao")

                case 3:
                     select_produto("tipo")
            
                case 4:
                    select_produto("localizacao")

                case 5:
                    select_produto("lote")

                case 6:
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

                    time.sleep(15)

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

            print("\nAdicionando item ao estoque...")

            time.sleep(15)

            print("""\n
-------------------------------
  Item adicionado com sucesso!
------------------------------- 
                          \n""")


        elif opcao == 4:
            sku = str(input('\nEscreva o SKU do item que deseja atualizar: '))

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

                subopcao = str(input('\nDeseja atualizar este item ? (s/n): '))

                if subopcao.lower() == 's':
                    opcao_atualizacao = int(input('''\nO que deseja atualizar ?
    1.Descricao
    2.Quantidade
    3.Tipo
    4.Localizacao
    5.Todos os campos
    Escolha uma opção: '''))
                    
                    if opcao_atualizacao == 1:
                        nova_descricao = str(input('Digite a nova descricao do item: '))
                        
                        update_query = """UPDATE produto 
                                  SET descricao = %s
                                  WHERE sku = %s"""
                        update_valores = (nova_descricao, sku)
                    
                        cursor.execute(update_query, update_valores)
                        conn.commit()

                        print("\nAtualizando item...")

                        time.sleep(15)

                        print("""\n
-------------------------------
  Item atualizado com sucesso! 
------------------------------- 
                          \n""")
                        
                        print("\nItem atualizado:\n")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print(f"SKU: {resultado['sku']} | "
                        f"Descricao: {resultado['descricao']} | "
                        f"Tipo: {resultado['tipo']} | "
                        f"Local: {resultado['localizacao']} |"
                        f"Quantidade: {resultado['quantidade']} | "
                        f"lote: {resultado['lote']}")
                        print("---------------------------------------------------------------------------------------------------------------------")
                    
                    elif opcao_atualizacao == 2:
                        nova_quantidade = int(input('Digite a nova quantidade do item: '))
                        
                        update_query = """UPDATE produto 
                                  SET quantidade = %s
                                  WHERE sku = %s"""
                        update_valores = (nova_quantidade, sku)
                    
                        cursor.execute(update_query, update_valores)
                        conn.commit()

                        print("\nAtualizando item...")

                        time.sleep(15)

                        print("""\n
-------------------------------
  Item atualizado com sucesso! 
------------------------------- 
                          \n""")
                        
                        print("\nItem atualizado:\n")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print(f"SKU: {resultado['sku']} | "
                        f"Descricao: {resultado['descricao']} | "
                        f"Tipo: {resultado['tipo']} | "
                        f"Local: {resultado['localizacao']} |"
                        f"Quantidade: {resultado['quantidade']} | "
                        f"lote: {resultado['lote']}")
                        print("---------------------------------------------------------------------------------------------------------------------")
                    
                        
                    elif opcao_atualizacao == 3:
                        novo_tipo = str(input('Digite o novo tipo do item: '))
                        
                        update_query = """UPDATE produto 
                                  SET tipo = %s
                                  WHERE sku = %s"""
                        update_valores = (novo_tipo, sku)
                    
                        cursor.execute(update_query, update_valores)
                        conn.commit()

                        print("\nAtualizando item...")

                        time.sleep(15)

                        print("""\n
-------------------------------
  Item atualizado com sucesso! 
------------------------------- 
                          \n""")
                        
                        print("\nItem atualizado:\n")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print(f"SKU: {resultado['sku']} | "
                        f"Descricao: {resultado['descricao']} | "
                        f"Tipo: {resultado['tipo']} | "
                        f"Local: {resultado['localizacao']} |"
                        f"Quantidade: {resultado['quantidade']} | "
                        f"lote: {resultado['lote']}")
                        print("---------------------------------------------------------------------------------------------------------------------")
                    
                    elif opcao_atualizacao == 4:
                        nova_localizacao = str(input('Digite a nova localizacao do item: '))
                        
                        update_query = """UPDATE produto 
                                  SET localizacao = %s
                                  WHERE sku = %s"""
                        update_valores = (nova_localizacao, sku)
                    
                        cursor.execute(update_query, update_valores)
                        conn.commit()

                        print("\nAtualizando item...")

                        time.sleep(15)

                        print("""\n
-------------------------------
  Item atualizado com sucesso! 
------------------------------- 
                          \n""")
                        
                        print("\nItem atualizado:\n")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print(f"SKU: {resultado['sku']} | "
                        f"Descricao: {resultado['descricao']} | "
                        f"Tipo: {resultado['tipo']} | "
                        f"Local: {resultado['localizacao']} |"
                        f"Quantidade: {resultado['quantidade']} | "
                        f"lote: {resultado['lote']}")
                        print("---------------------------------------------------------------------------------------------------------------------")                    


        elif opcao == 5:
            print("Voltando para o menu...")
            i = 1
            return
        

        else:
            print ('\nOpção nao encontrada!')
            contador += 1