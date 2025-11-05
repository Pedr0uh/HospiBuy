import mysql.connector
import time

conn = mysql.connector.connect(
    host="shinkansen.proxy.rlwy.net", # temos que aprender como esconder host e senha
    user="root",
    password="eSGzRtPwShQdjLoqAqsjUCpAIzHqPLRX",
    database="HospiBuy",
    port="18428"
)

cursor = conn.cursor(dictionary=True)

login = ""  # variavel login vazia
senha = ""  # variavel senha vazia
nome_usuario = ""
cargo = ""
tentativa = 0  # contador global para tentativas


def main():

    print("\nConectando com o Banco...")
    
    time.sleep(2)

    if conn.is_connected():
        print("\nConectado com o banco com sucesso!")
    else:
        print("\nFalha em conectar com o banco!")

    inicio()


def inicio():

    """
    cpf_teste = "12345678900"
    nome_teste = "Pedro Teste"
    num_acess_teste = 0
    senha_teste = "1234"

    query = "INSERT INTO usuarios (CPF, nome, num_acesso, senha) VALUES (%s, %s, %s, %s)"
    valores = cpf_teste, nome_teste, num_acess_teste, senha_teste

    cursor.execute(query, valores) = digitar valores para query do SQL

    conn.commit() = para salvar no banco de dados

    cursor.execute("SELECT * FROM usuarios;") = query para mostrar os dados da tabela
    dadosUsuarios = cursor.fetchall() = guardei o comando fetchall em uma tabela, que mostra os dados da query
    (todas as linhas, fetchone para uma linha só)

    print(dadosUsuarios) dei print para mostrar o valor da variavel que é o fetchall

    """

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
                fazerLogin()
            case "2": # caso a variavel seja 2
                criarLogin()
            case "3": # caso a variavel seja 3
                sair()
            case "4": # caso 4 vai pra home
                home()
            case _: # caso a variavel não seja nenhuma das opções
                print("Erro! Opção inválida!")


def criarLogin():

    i = 0    

    while i == 0:
        
        cnes = pedir_input("\nInsira o CNES do Hospital (sem caracteres) Ou digite 0 para voltar para o menu: ")
        if cnes is None:
            return
        
        queryVerific = "SELECT * FROM hospitais WHERE CNES = %s"
        cursor.execute(queryVerific, (cnes,))
        
        resultado = cursor.fetchone()
        
        if resultado:
            
            print("\n-- Hospital já cadastrado! --\n")
            inicio()
        else:
        
            cnpj = pedir_input("Insira o CNPJ do Hospital (sem caracteres) Ou digite 0 para voltar para o menu: : ")
            if cnpj is None:
                return
            
            nomeHospital = pedir_input("Insira o nome do Hospital Ou digite 0 para voltar para o menu: : ")
            if nomeHospital is None:
                return
            
            telefone = pedir_input("Insira um telefone de contato Ou digite 0 para voltar para o menu: : ")
            if telefone is None:
                return
            
            email = pedir_input("Insira um email principal Ou digite 0 para voltar para o menu: : ")
            if email is None:
                return
            
            cpfADM = pedir_input("Insira o CPF do administrador Ou digite 0 para voltar para o menu: : ")
            if cpfADM is None:
                return
            
            nomeADM = pedir_input("Insira o nome do administrador Ou digite 0 para voltar para o menu: : ")
            if nomeADM is None:
                return
            
            senha = pedir_input("Crie uma senha para o login do adminstrador Ou digite 0 para voltar para o menu: : ")
            if senha is None:
                return
            
            plano = pedir_input("""
        -- Qual plano quer assinar? -- 
        
            1 - Plano 1    
            2 - Plano 2
            3 - Plano 3
            0 - voltar para o menu: 
            
            """)
            if plano is None:
                return
        
            while plano not in ["1", "2", "3", "0"]:
                print(r"""
        Número digitado incorreto, tente novamente:
        
        -- Qual plano quer assinar? -- 
        
            1 - Plano 1    
            2 - Plano 2
            3 - Plano 3 
            """)
                
                plano = input("Escolha a opção: ")
        
            query = "INSERT INTO hospitais (CNES, CNPJ, nome, telefone, email, cpfADM, nomeADM, senha, plano) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = cnes, cnpj, nomeHospital, telefone, email, cpfADM, nomeADM, senha, plano
            
            queryLogin = "INSERT INTO usuarios (CPF, nome, senha, cargo) VALUES(%s, %s, %s, 'ADM')"
            valoresLogin = cpfADM, nomeADM, senha
        
            cursor.execute(query, valores)
            
            cursor.execute(queryLogin, valoresLogin)
        
            conn.commit()
            
            print("\nSalvando informações...")
            
            time.sleep(20)
        
            print("""
        -------------------------------
        Cadastro realizado com sucesso!
        -------------------------------
        """)


def fazerLogin():
    global tentativa, nome_usuario, cargo
    
    while tentativa < 5:
        entradaLogin = input("Digite seu CPF: ")
        entradaSenha = input("Digite sua senha: ")

        query = "SELECT nome, cargo FROM usuarios WHERE CPF = %s AND senha = %s"
        valores = entradaLogin, entradaSenha
        
        cursor.execute(query, valores)
        resultado = cursor.fetchone()

        if resultado:
            
            nome_usuario = resultado['nome']
            cargo = resultado['cargo']
            
            print(f"""\n
------------------------------------      
        Bem vindo {nome_usuario}!
------------------------------------    
                  """)
            
            home()
            
            return  # sai da função
        else:
            tentativa += 1
            print(f"Usuário ou senha incorretos. Tentativa {tentativa}/5\n")

    print("Número de tentativas excedido! Voltando ao menu.\n")
    tentativa = 0  # reseta para poder tentar de novo


def home():
    print(r"""
-- O que deseja fazer hoje? -- 

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
            return

    while True:
        match opcao:
            case "1":
                estoque()
            case "2":
                compras()
            case "3":
                descarte()
            case "4":
                gerenciarUsuarios()
            case "5":
                sair()
            case _:
                print("Erro! Tente novamente")


def gerenciarUsuarios():
    print("\nGerenciamento de Usuários aqui!\n")
    home()
    return


def estoque():
    print("\nEstoque aqui!\n")
    home()
    return

def compras():
    print("\nCompras aqui!\n")
    home()
    return

def descarte():
    print("\nDescarte aqui!\n")
    home()
    return

def sair():
    print("\nEncerrando Programa...\n")
    
    cursor.close
    
    conn.close
    
    import sys
    sys.exit()


def pedir_input(texto): # função para validar input igual a zero e retorna para menu inicial
    valor = input(texto)
    if valor == "0":
        print("\nVoltando a o Menu Inicial...\n")
        return None
    return valor

if __name__ == "__main__":
    main()
