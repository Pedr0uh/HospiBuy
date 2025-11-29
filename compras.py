import datetime
import random
from conexao import cursor, conn
import time

compras = []
contador_id = 1

def mostrar_menu():
    print("\n==== PAINEL DE COMPRAS ====\n")
    print("1. Registrar nova compra")
    print("2. Listar todas as compras")
    print("3. Ver itens com menos estoque")
    print("4. Deletar operação de compra")
    print("5. Sair\n")
    

def registrar_compra():
    global contador_id

    print("\n--- Registrar Nova Compra ---")
    fornecedor = input("ID do fornecedor: ").str
    
    if fornecedor not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
        print("Erro: Fornecedor inválido. Compra não registrada.")
        return

    item = input("sku do comprado: ").strip().upper()

    query_verifica = 'SELECT * FROM produto WHERE sku = %s'
    cursor.execute(query_verifica, (item,)) 
    resultado = cursor.fetchone()

    if not resultado:
        print("Erro: SKU do produto não encontrado no estoque. Compra não registrada.")
        return
    
    try:
        quantidade = int(input("Quantidade: "))
        unidade = input("Unidade (ex: UN, KG, LT): ").strip().upper()
        valor_unitario = float(input("Valor unitário (R$): "))
    except ValueError:
        print("Erro: valor inválido. Compra não registrada.")
        return

    query = 'INSERT INTO operacoes (nome_operacao, descartar, quantidade, unidade, sku) VALUES (%s, %s, %s, %s, %s)'
    valores = ('Entrada', None, quantidade, unidade, item)

    query_adicionar = 'UPDATE produto SET quantidade = quantidade + %s WHERE sku = %s'
    valores_adicionar = (quantidade, item)

    cursor.execute(query_adicionar, valores_adicionar)
    cursor.execute(query, valores)
    conn.commit()

    print('Salvando...')
    time.sleep(15)
    contador_id += 1
    print("✅ Compra registrada com sucesso!")

def listar_compras():
    print("\n--- Lista de Compras ---")
    
    query = 'SELECT * FROM operacoes WHERE nome_operacao = %s'
    cursor.execute(query, ('Entrada',))

    resultado = cursor.fetchall()

    if resultado:
        for compra in resultado:
            print("--------------------------------------------------------------")
            print(f"ID: {compra['id_operacao']} | NomeOP: {compra['nome_operacao']} | SKU: {compra['sku']} | Quantidade: {compra['quantidade']} {compra['unidade']}")
            print("--------------------------------------------------------------")
    else:
        print("Nenhuma compra registrada.")

def menosEstoque():
    print("\n--- Produtos com menos estoque ---")
    
    query = 'SELECT * FROM produto ORDER BY quantidade ASC'
    
    cursor.execute(query)
    resultado1 = cursor.fetchall()
    
    if resultado1:
        print("Produtos com menos estoque:")
        for item in resultado1:
            print("---------------------------------------------------------------------------------------------------------------------")
            print(f"SKU: {item['sku']} | "
            f"Descricao: {item['descricao']} | "
            f"Tipo: {item['tipo']} | "
            f"Local: {item['localizacao']} | "
            f"Quantidade: {item['quantidade']} | "
            f"lote: {item['lote']}")
            print("---------------------------------------------------------------------------------------------------------------------")
    else:
        print("Nenhum produto encontrado no estoque.")

    subopcao = input("Deseja solicitar compra para algum desses itens? (s/n): ").strip().lower()

    if subopcao == 's':
        sku = input("Digite o SKU do produto: ").strip()
        print("\n-- Fornecedores --\n")
        precos = {}

        for i in range(15):
            preco = random.uniform(6, 14)
            precos[i+1] = preco

            print('--------------------------------')
            print(f"{i+1} - Fornecedor {i+1}")
            print(f"preço unitário: R$ {preco:.2f}")
            print('--------------------------------')

        fornecedor_escolhido = int(input("\nEscolha o número do fornecedor: ").strip())

        while fornecedor_escolhido not in precos:
            print("Fornecedor inválido. Tente novamente.")
            fornecedor_escolhido = int(input("Escolha o número do fornecedor: ").strip())

        preco_escolhido = precos[fornecedor_escolhido]
        quantidade_solicitada = int(input("Digite a quantidade a ser comprada do item: ").strip())
        local_item = input("Digite o local que o item será armazenado: ").strip()    

        mult = quantidade_solicitada * preco_escolhido

        print("\n-- Resumo da Compra --\n")
        print(f"SKU do Produto: {sku}")
        print(f"Fornecedor: Fornecedor {fornecedor_escolhido}")
        print(f"Quantidade: {quantidade_solicitada}")
        print(f"Preço Unitário: R$ {preco_escolhido:.2f}")
        print(f"Valor Total da Compra: R$ {mult :.2f}\n")

        confirmar = input("Confirmar compra? (s/n): ").strip().lower()
        if confirmar == 's':
            
            query = 'UPDATE produto SET quantidade = %s, data_compra = %s, ID_fornecedor = %s WHERE sku = %s'
            valores = (item['quantidade'] + int(quantidade_solicitada), datetime.datetime.now().strftime("%Y-%m-%d"), fornecedor_escolhido, sku)

            query_operacao = 'INSERT INTO operacoes ( nome_operacao, descartar, quantidade, unidade, sku) VALUES (%s, %s, %s, %s, %s)'
            valores_operacao = ('Entrada', None, quantidade_solicitada, 'UN', sku)

            cursor.execute(query_operacao, valores_operacao)
            cursor.execute(query, valores)
            conn.commit()

            print("Salvando...")

            time.sleep(15)

            print('\n--------------------------------')
            print("Compra registrada com sucesso!")
            print('--------------------------------')
        else:
            print("Compra cancelada.")


def deletar_operacao():
    print("\n--- Deletar Operação de Compra ---")
    id_operacao = input("Digite o ID da operação de compra a ser deletada: ").strip()

    query_verifica = 'SELECT * FROM operacoes WHERE id_operacao = %s AND nome_operacao = %s'
    cursor.execute(query_verifica, (id_operacao, 'Entrada'))
    resultado = cursor.fetchone()

    if not resultado:
        print("Erro: Operação de compra não encontrada.")
        return

    print('--------------------------------------------------')
    print(f"ID: {resultado['id_operacao']} | SKU: {resultado['sku']} | Quantidade: {resultado['quantidade']} {resultado['unidade']}")
    print('--------------------------------------------------')

    confirmar = input(f"Tem certeza que deseja deletar a operação de compra com ID {id_operacao}? (s/n): ").strip().lower()

    if confirmar == 's':
        query_deletar = 'DELETE FROM operacoes WHERE id_operacao = %s'
        cursor.execute(query_deletar, (id_operacao,))
        conn.commit()
        print("\nOperação de compra deletada com sucesso!")
    else:
        print("\nOperação de compra não deletada.")

def menu():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            registrar_compra()
        elif escolha == '2':
            listar_compras()
        elif escolha == '3':
            menosEstoque()
        elif escolha == '4':
            deletar_operacao()
        elif escolha == '5':
            print("Saindo... Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")


