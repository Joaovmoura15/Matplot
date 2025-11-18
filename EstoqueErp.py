import matplotlib.pyplot as plt

# Estoque geral
estoque = {}

# Cadastrar produto
def cadastrar_produto():
    print("\n=== Cadastro de Produto ===")
    nome = input("Nome do produto: ").strip()

    if nome in estoque:
        print("Produto já cadastrado.")
        return

    categoria = input("Categoria: ").strip()
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade inicial: "))

    estoque[nome] = {
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"{nome} cadastrado com sucesso.")

# Excluir produto pelo nome
def excluir_produto():
    print("\n=== Excluir Produto ===")
    nome = input("Nome do produto para excluir: ").strip()

    if nome in estoque:
        del estoque[nome]
        print(f"{nome} removido do sistema.")
    else:
        print("Produto não encontrado.")

# Relatório geral
def relatorio_produtos():
    print("\n=== Relatório de Produtos ===")

    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'Produto':<15} {'Categoria':<12} {'Preço':<10} {'Qtd':<8} {'*'}")
    print("-" * 60)

    for nome, dados in estoque.items():
        preco = dados["preco"]
        categoria = dados["categoria"]
        quantidade = dados["quantidade"]

        alerta = "BAIXO" if quantidade < 5 else ""

        print(f"{nome:<15} {categoria:<12} R${preco:<10.2f} {quantidade:<8} {alerta}")

# Gráfico de quantidades (opcional)
def grafico_estoque():
    if not estoque:
        print("Nada para mostrar.")
        return

    nomes = list(estoque.keys())
    quantidades = [estoque[p]["quantidade"] for p in estoque]

    plt.bar(nomes, quantidades)
    plt.title("Quantidade em Estoque")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

# Menu principal
def menu():
    while True:
        print("\n=== Sistema de Estoque ===")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Relatório")
        print("4 - Gráfico")
        print("5 - Sair")

        opc = input("Escolha: ").strip()

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            excluir_produto()
        elif opc == "3":
            relatorio_produtos()
        elif opc == "4":
            grafico_estoque()
        elif opc == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
