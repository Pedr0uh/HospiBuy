import datetime

compras = []
contador_id = 1

def mostrar_menu():
    print("\n==== PAINEL DE COMPRAS ====")
    print("1. Registrar nova compra")
    print("2. Listar todas as compras")
    print("3. Buscar compras por fornecedor")
    print("4. Mostrar todos os criterios")
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

def mostrar_estatisticas():
    print("\n--- Estatísticas de Compras ---")
    if not compras:
        print("Nenhuma compra registrada.")
        return

    total_compras = len(compras)
    total_gasto = sum(c['quantidade'] * c['valor_unitario'] for c in compras)

    print(f"Total de compras registradas: {total_compras}")
    print(f"Valor total gasto: R$ {total_gasto:.2f}")

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
            mostrar_estatisticas()
        elif escolha == '5':
            print("Saindo... Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")


