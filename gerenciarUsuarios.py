 # ...existing code...
def gerenciarUsuarios():
    print('Seja bem-vindo ao sistema de gerenciamento de usuarios!')

    while True:
        print("1. Registrar novo usuario")
        print("2. Listar todas os usuarios")
        print("3. Buscar usuarios por algum cargo")
        print("4. Mostrar estatísticas")
        print("5. Sair")
        opcao = input("Escolha a opção: ")

        if opcao == "1":
            novo_usuario = input('Digite o nome do novo usuario: ')
            print(f'Novo usuario registrado: {novo_usuario}')
        elif opcao == "2":
            print('Listando todos os usuarios...')
        elif opcao == "3":
            cargo_busca = input('Digite o cargo que deseja buscar: ')
            print(f'Buscando usuarios com cargo: {cargo_busca}')
        elif opcao == "4":
            print('Mostrando estatísticas...')
        elif opcao == "5":
            print('Saindo do sistema de gerenciamento de usuarios...')
            break
        else:
            print('Opção inválida. Tente novamente.')
# ...existing code...  