from conexao import conn, cursor
from utils import pedir_input 
import time

def criarLogin():

    cnes = pedir_input("\nInsira o CNES do Hospital (sem caracteres) Ou digite 0 para voltar para o menu: ")
    if cnes is None:
        return
    
    queryVerific = "SELECT * FROM hospitais WHERE CNES = %s"
    cursor.execute(queryVerific, (cnes,))
    
    resultado = cursor.fetchone()
    
    if resultado:

        print("\n-- Hospital já cadastrado! --\n")
        return False
    

    cnpj = pedir_input("Insira o CNPJ do Hospital (sem caracteres) Ou digite 0 para voltar para o menu: : ")
    if cnpj is None:
        return False
    
    nomeHospital = pedir_input("Insira o nome do Hospital Ou digite 0 para voltar para o menu: : ")
    if nomeHospital is None:
        return False
    
    telefone = pedir_input("Insira um telefone de contato Ou digite 0 para voltar para o menu: : ")
    if telefone is None:
        return False
    
    email = pedir_input("Insira um email principal Ou digite 0 para voltar para o menu: : ")
    if email is None:
        return False
    
    cpfADM = pedir_input("Insira o CPF do administrador Ou digite 0 para voltar para o menu: : ")
    if cpfADM is None:
        return False
    
    nomeADM = pedir_input("Insira o nome do administrador Ou digite 0 para voltar para o menu: : ")
    if nomeADM is None:
        return False
    
    senha = pedir_input("Crie uma senha para o login do adminstrador Ou digite 0 para voltar para o menu: : ")
    if senha is None:
        return False
    
    plano = pedir_input("""
-- Qual plano quer assinar? -- 

    1 - Plano 1    
    2 - Plano 2
    3 - Plano 3
    0 - voltar para o menu: 
    
    """)
    if plano is None:
        return False

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
    
    time.sleep(3)
    
    return True
        
    