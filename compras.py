import datetime
from random import random
from conexao import cursor, conn
import time

compras = []
contador_id = 1

def mostrar_menu():
    print("\n==== PAINEL DE COMPRAS ====")
    print("1. Registrar nova compra")
    print("2. Listar todas as compras")
    print("3. Buscar compras por fornecedor")
    print("4. Ver itens com menos estoque")
    print("5. Sair")
    

def registrar_compra():
    global contador_id

    print("\n--- Registrar Nova Compra ---")
    fornecedor = input("Nome do fornecedor: ").strip()
    item = input("Item comprado: ").strip()
    
    try:
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário (R$): "))
    except ValueError:
        print("Erro: valor inválido. Compra não registrada.")
        return

    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    compra = {
        "id": contador_id,
        "fornecedor": fornecedor,
        "item": item,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "data": data
    }

    compras.append(compra)
    contador_id += 1
    print("✅ Compra registrada com sucesso!")

def listar_compras():
    print("\n--- Lista de Compras ---")
    if not compras:
        print("Nenhuma compra registrada.")
        return

    for c in compras:
        valor_total = c['quantidade'] * c['valor_unitario']
        print(f"\nID: {c['id']}")
        print(f"Fornecedor: {c['fornecedor']}")
        print(f"Item: {c['item']}")
        print(f"Quantidade: {c['quantidade']}")
        print(f"Valor Unitário: R$ {c['valor_unitario']:.2f}")
        print(f"Valor Total: R$ {valor_total:.2f}")
        print(f"Data: {c['data']}")

def buscar_por_fornecedor():
    print("\n--- Buscar Compras por Fornecedor ---")
    nome = input("Digite o nome do fornecedor: ").strip().lower()

    encontrados = [c for c in compras if nome in c['fornecedor'].lower()]

    if not encontrados:
        print("Nenhuma compra encontrada para este fornecedor.")
        return

    print(f"\nCompras encontradas para '{nome}':")
    for c in encontrados:
        valor_total = c['quantidade'] * c['valor_unitario']
        print(f"\nID: {c['id']}")
        print(f"Item: {c['item']}")
        print(f"Quantidade: {c['quantidade']}")
        print(f"Valor Unitário: R$ {c['valor_unitario']:.2f}")
        print(f"Valor Total: R$ {valor_total:.2f}")
        print(f"Data: {c['data']}")

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
        print("-- Fornecedores --")
        for i in range(15):
            preco = random.uniform(6, 14)
            preco[i+1] = preco

            print('--------------------------------')
            print(f"{i+1} - Fornecedor {i+1}")
            print(f"preço unitário: R$ {preco:.2f}")
            print('--------------------------------')

        fornecedor_escolhido = int(input("Escolha o número do fornecedor: ").strip())
        preco_escolhido = preco[fornecedor_escolhido]
        quantidade_solicitada = input("Digite a quantidade a ser comprada do item: ").strip()
        local_item = input("Digite o local que o item será armazenado: ").strip()    

        soma = quantidade_solicitada * preco_escolhido

        print("-- Resumo da Compra --")
        print(f"SKU do Produto: {sku}")
        print(f"Fornecedor: Fornecedor {fornecedor_escolhido}")
        print(f"Quantidade: {quantidade_solicitada}")
        print(f"Preço Unitário: R$ {preco_escolhido:.2f}")
        print(f"Valor Total da Compra: R$ {soma:.2f}")

        confirmar = input("Confirmar compra? (s/n): ").strip().lower()
        if confirmar == 's':
            
            query = 'UPDATE produto SET sku = %s, descricao = %s, quantidade = %s, tipo = %s, data_compra = %s, lote = %s, validade = %s, localizacao = %s, ID_fornecedor = %s WHERE sku = %s'
            valores = (item['sku'], item['descricao'], item['quantidade'] + int(quantidade_solicitada), item['tipo'], datetime.datetime.now().strftime("%Y-%m-%d"), item['lote'], item['validade'], local_item, fornecedor_escolhido, sku)

            cursor.execute(query, valores)
            conn.commit()

            print("Salvando...")

            time.sleep(15)

            print("Compra registrada com sucesso!")
        else:
            print("Compra cancelada.")
          # Exemplo de limite baixo de estoque

def menu():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            registrar_compra()
        elif escolha == '2':
            listar_compras()
        elif escolha == '3':
            buscar_por_fornecedor()
        elif escolha == '4':
            menosEstoque()
        elif escolha == '5':
            print("Saindo... Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")


