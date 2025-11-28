
def descarte():
    while True:
        print("""
Selecione o tipo de descarte:

1 - Resíduos Infectantes
2 - Resíduos Químicos
3 - Rejeitos Radioativos
4 - Resíduos Comuns
5 - Perfurocortantes
6 - Voltar ao menu principal
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "6":
            print("Voltando ao menu principal...")
            break

        sku = input("Informe o SKU do item para descarte: ").strip()

        match opcao:
            case "1":
                print(f"Descarte selecionado: Resíduos Infectantes | SKU: {sku}")
            case "2":
                print(f"Descarte selecionado: Resíduos Químicos | SKU: {sku}")
            case "3":
                print(f"Descarte selecionado: Rejeitos Radioativos | SKU: {sku}")
            case "4":
                print(f"Descarte selecionado: Resíduos Comuns | SKU: {sku}")
            case "5":
                print(f"Descarte selecionado: Perfurocortantes | SKU: {sku}")
            case _:
                print("Opção inválida, tente novamente.")

    
    
