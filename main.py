from conexao import conn, cursor
import time
from fazerLogin import fazerLogin
from criarLogin import criarLogin
from gerenciarUsuarios import gerenciarUsuarios
import estoque, compras

nome_usuario = None
cargo = None
cnes = None

def main():

    print("\nConectando com o Banco...")
    
    time.sleep(2)

    if conn.is_connected():
        print("\nConectado com o banco com sucesso!")
    else:
        print("\nFalha em conectar com o banco!")

    inicio()


def inicio():

    while True:  # loop para manter o menu ativo
        print(r"""
----------------------------------------------
       Bem-Vindo(a) ao Serviço HOSPIBUY
----------------------------------------------  
              """)
        print(r"""Escolha uma opção:

1 - Fazer Login
2 - Criar Login
3 - Sair
""")
        escolha = input("Digite a opção: ")
        match escolha: # match para "escolha e caso" ligado a variavel escolha
            case "1": # caso a variavel seja 1
                usuario = fazerLogin()  
                if usuario:
                    global nome_usuario, cargo, cnes
                    nome_usuario = usuario["nome"]
                    cargo = usuario["cargo"]
                    cnes = usuario["cnes"]
                    home()
                else:
                    print("falha no login ou cancelado")
            case "2": # caso a variavel seja 2
                sucesso = criarLogin()
                if sucesso:
                    print("""
-------------------------------
Cadastro realizado com sucesso!
-------------------------------
""")
            case "3": # caso a variavel seja 3
                sair()
            case _: # caso a variavel não seja nenhuma das opções
                print("Erro! Opção inválida!")



def home():

    global nome_usuario, cargo    

    while True:
        print(f"\nBem vindo {nome_usuario}! \nCargo: {cargo} \ncnes: {cnes}\n")

        print(r"""-- O que deseja fazer hoje? -- 

    1 - Gerenciar Estoque    
    2 - Comprar Itens
    3 - Descarte de Itens
    4 - Gerenciar Usuários
    5 - Sair 
        """)

        opcao = input("Escolha a opção: ")

        if opcao == "4":
            if cargo != "ADM":
                print("Acesso negado, apenas Adminstradores podem acessar. Entre em contato com o adminstrador da plataforma")
                home()

        match opcao:
            case "1":
                estoque.estoque(cnes)
                continue
            case "2":
                compras.menu()
                continue
            case "3":
                descarte()
                continue
            case "4":
                gerenciarUsuarios()
                continue
            case "5":
                sair()
                break
                return
            case _:
                print("Erro! Tente novamente")
                continue



def descarte():
    print("\nDescarte aqui!\n")
    home()
    return


def sair():
    print("\nEncerrando Programa...\n")
    
    cursor.close()
    conn.close()
    import sys
    sys.exit()


if __name__ == "__main__":
    main()