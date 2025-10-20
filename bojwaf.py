def menu():
    while True:
        print("\n=== SISTEMA DE ESTOQUE HOSPITALAR ===")
        print("1. Cadastrar novo item")
        print("2. Ver todos os itens")
        print("3. Remover item")
        print("4. Buscar item")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_item()
        elif opcao == '2':
            listar_itens()
        elif opcao == '3':
            atualizar_quantidade()
        elif opcao == '4':
            remover_item()
        elif opcao == '5':
            buscar_item()
        elif opcao == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar_item():


    sql = "INSERT INTO estoque (nome, tipo, quantidade, unidade, validade, local) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (nome, tipo, quantidade, unidade, validade, local)

    cursor.execute(sql, valores)
    conexao.commit()
    print("Item cadastrado com sucesso.")



def listar_itens():
    cursor.execute("SELECT * FROM estoque")
    resultados = cursor.fetchall()

    print("\n=== ITENS NO ESTOQUE ===")
    for item in resultados:
        id, nome, tipo, quantidade, unidade, validade, local = item
        validade_str = validade.strftime('%Y-%m-%d') if validade else "Sem validade"
        print(f"ID: {id} | Nome: {nome} | Tipo: {tipo} | Qtd: {quantidade} {unidade} | Validade: {validade_str} | Local: {local}")


def buscar_item():
    termo = input("Buscar por nome ou tipo: ")
    query = "SELECT * FROM estoque WHERE nome LIKE %s OR tipo LIKE %s"
    valores = (f"%{termo}%", f"%{termo}%")
    cursor.execute(query, valores)
    resultados = cursor.fetchall()

    if resultados:
        for item in resultados:
            id, nome, tipo, quantidade, unidade, validade, local = item
            validade_str = validade.strftime('%Y-%m-%d') if validade else "Sem validade"
            print(f"ID: {id} | Nome: {nome} | Tipo: {tipo} | Qtd: {quantidade} {unidade} | Validade: {validade_str} | Local: {local}")
    else:
        print("Nenhum item encontrado.")


# Iniciar o menu
menu()
