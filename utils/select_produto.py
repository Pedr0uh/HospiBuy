from conexao import cursor

def select_produto(busca):
   
    if busca not in ['sku', 'descricao', 'tipo', 'localizacao', 'lote']:
        print("Critério de busca inválido.")
        return None
    
    valor = input(f"Digite o {busca} do produto que deseja buscar:").strip()

    if busca in ['descricao', 'tipo', 'localizacao', 'lote']:
        operador = 'LIKE'
        parametro = f"%{valor}%"
    else:
        operador = '='
        parametro = valor

    select_query = f"SELECT * FROM produto WHERE {busca} {operador} %s" 
    cursor.execute(select_query, (parametro,))

    resultado = cursor.fetchall()

    if resultado:
        print("\nItem encontrado:\n")

        for item in resultado:
            print("---------------------------------------------------------------------------------------------------------------------")
            print(f"SKU: {item['sku']} | "
            f"Descricao: {item['descricao']} | "
            f"Tipo: {item['tipo']} | "
            f"Local: {item['localizacao']} | "
            f"Quantidade: {item['quantidade']} | "
            f"lote: {item['lote']}")
            print("---------------------------------------------------------------------------------------------------------------------")

    else:
        print("Produto não encontrado.")
        return None

    return resultado