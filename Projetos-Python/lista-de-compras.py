lista_compras = []
unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]

while True: #Loop para o Menu
    print("\n=== GERENCIAMENTO DE COMPRAS ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Pesquisar produtos")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        produto = input("Digite o nome do produto: ").strip()
        if produto: 
            lista_compras.append(produto)
            print(f"O produto {produto} foi adicionado!")
        else: 
            print("Nome inválido. Tente novamente.")
    
    elif opcao == "2":
        if lista_compras == []:
            print("A lista está vazia")
        else: 
            produto = input("Digite o nome do produto a remover: ").strip()
            if produto in lista_compras:
                lista_compras.remove(produto)
                print(f"O '{produto} foi removido da lista")
            else:
                print(f"O {produto} não está na lista")
    
    elif opcao == "3":
        if lista_compras == []:
            print("A lista de compra está vazia")
        else: 
            print("\nProdutos na lista:")
            for i, produto in enumerate(lista_compras, 1):
                print(f"{i}. {produto}")
                
    elif opcao == "4":
        print("Saindo do programa")
        break
    
    else: 
        print("Opção inválida! Tente novamente")