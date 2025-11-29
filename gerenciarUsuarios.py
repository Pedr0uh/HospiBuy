from conexao import conn, cursor
import time

def gerenciarUsuarios(cnes):
    print('\nSeja bem-vindo ao sistema de gerenciamento de usuarios!\n')

    while True:
        print("1. Registrar novo usuario")
        print("2. Listar todas os usuarios")
        print("3. Buscar usuarios por algum cargo")
        print("4. Buscar por nome")
        print("5. Mostrar estatísticas")
        print("6. Deletar usuario")
        print("7. Sair")
        opcao = input("Escolha a opção: ")

        if opcao == "1":
            novo_usuario = input('Digite o nome do novo usuario: ')
            email_usuario = input('Digite o email do novo usuario: ')
            cpf_usuario = input('Digite o CPF do novo usuario: ')
            cargo = input('Digite o cargo do novo usuario: ')   
            ende = input('Digite o endereco do novo usuario: ')
            senha = input('Digite a senha do novo usuario: ')

            query = 'INSERT INTO usuario (nome, email, cnes, cpf, cargo, endereco, senha) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            valores = (novo_usuario, email_usuario, cnes, cpf_usuario, cargo, ende, senha)

            cursor.execute(query, valores)
            conn.commit()

            print("Salvando novo usuario...")

            time.sleep(10)
            print(f'Novo usuario registrado: {novo_usuario}')

        elif opcao == "2":
            print('Listando todos os usuarios...')

            cursor.execute('SELECT * FROM usuario')
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                print('---------------------------------------------------------------------------------------------------------------------------------')
                print(f"ID: {usuario['ID_usuario']} | Nome: {usuario['nome']} | Email: {usuario['email']} | CNES: {usuario['cnes']} | CPF: {usuario['cpf']} | Cargo: {usuario['cargo']} | Endereco: {usuario['endereco']}")
                print('---------------------------------------------------------------------------------------------------------------------------------')

        
        elif opcao == "3":
            cargo_busca = input('Digite o cargo que deseja buscar: ')
            print(f'Buscando usuarios com cargo: {cargo_busca}')

            query = 'SELECT * FROM usuario WHERE cargo = %s'
            cursor.execute(query, (cargo_busca,))
            usuarios = cursor.fetchall()

            for usuario in usuarios:
                print('---------------------------------------------------------------------------------------------------------------------------------')
                print(f"ID: {usuario['ID_usuario']} | Nome: {usuario['nome']} | Email: {usuario['email']} | CNES: {usuario['cnes']} | CPF: {usuario['cpf']} | Cargo: {usuario['cargo']} | Endereco: {usuario['endereco']}")
                print('---------------------------------------------------------------------------------------------------------------------------------')  


        elif opcao == "4":
            nome_busca = input('Digite o nome que deseja buscar: ')
            print(f'Buscando usuarios com nome: {nome_busca}')

            query = 'SELECT * FROM usuario WHERE nome LIKE %s'
            cursor.execute(query, (f'%{nome_busca}%',))
            usuarios = cursor.fetchall()

            for usuario in usuarios:
                print('---------------------------------------------------------------------------------------------------------------------------------')
                print(f"ID: {usuario['ID_usuario']} | Nome: {usuario['nome']} | Email: {usuario['email']} | CNES: {usuario['cnes']} | CPF: {usuario['cpf']} | Cargo: {usuario['cargo']} | Endereco: {usuario['endereco']}")
                print('---------------------------------------------------------------------------------------------------------------------------------')

        elif opcao == "5":
            print('Mostrando estatísticas...')

            cursor.execute('SELECT cargo, COUNT(*) AS total FROM usuario GROUP BY cargo')
            estatisticas = cursor.fetchall()

            for estatistica in estatisticas:
                print('------------------------------------------')
                print(f"Cargo: {estatistica['cargo']} | Total de usuarios: {estatistica['total']}")
                print('------------------------------------------')

        elif opcao == "6":
            cpf_usuario = input('Digite o CPF do usuario que deseja deletar: ')
            print(f'Deletando usuario com CPF: {cpf_usuario}')

            query_valida = 'SELECT nome FROM usuario WHERE cpf = %s'
            cursor.execute(query_valida, (cpf_usuario,))

            resultado = cursor.fetchone()
            if resultado is None:
                print("Usuário não encontrado.")
                return

            subopcao = input(f'Tem certeza que deseja deletar usuario {resultado["nome"]}? (s/n): ')

            if subopcao.lower() != 's':
                print('Operação cancelada.')
                return
            
            query = 'DELETE FROM usuario WHERE cpf = %s'
            cursor.execute(query, (cpf_usuario,))
            conn.commit()

            print("Deletando usuario...")

            time.sleep(10)

            print('--------------------------------')
            print("Usuario deletado com sucesso.")
            print('--------------------------------')

        elif opcao == "6":
            print('Saindo do sistema de gerenciamento de usuarios...')
            break
        else:
            print('Opção inválida. Tente novamente.')
# ...existing code...  