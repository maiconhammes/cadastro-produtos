produtos = []

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")

    produtos.append({
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    })

    cont = input("Deseja continuar? (s/n): ")
    if cont.lower() != 's':
        break

print("\n--- Produtos Cadastrados ---")
for p in produtos:
    print(f"{p['categoria']} - {p['nome']}: R${p['preco']:.2f}")
