produtos = []
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produto = {"nome": nome, "preco": preco}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\nLista de Produtos:")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}")

def menu():
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()





