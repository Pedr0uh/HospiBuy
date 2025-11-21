from conexao import cursor

login = ""  # variavel login vazia
senha = ""  # variavel senha vazia
nome_usuario = ""
cargo = ""
tentativa = 0  # contador global para tentativas


def fazerLogin():
    global tentativa, nome_usuario, cargo
    
    while tentativa < 5:
        entradaLogin = input("Digite seu CPF: ")
        entradaSenha = input("Digite sua senha: ")

        query = "SELECT nome, cargo FROM usuario WHERE cpf = %s AND senha = %s"
        valores = entradaLogin, entradaSenha
        
        cursor.execute(query, valores)
        resultado = cursor.fetchone()

        if resultado:
            return {"nome": resultado['nome'], "cargo": resultado['cargo']} 
        
        else:
            tentativa += 1
            print(f"Usuário ou senha incorretos. Tentativa {tentativa}/5\n")

    print("Número de tentativas excedido! Voltando ao menu.\n")
    tentativa = 0  # reseta para poder tentar de novo
    return None