from services.persistencia_service import (
    carregar_produtos,
    carregar_clientes,
    carregar_vendas,
    salvar_produtos,
    salvar_clientes,
    salvar_vendas
)

from services.estoque_service import (
    listar_produtos,
    buscar_produto,
    atualizar_estoque
)

from models.venda import Venda

def main():
    print("=== SISTEMA DE VENDAS ===")

    produtos = carregar_produtos()
    clientes = carregar_clientes()
    vendas = carregar_vendas()

    print("\n--- Cadastro do cliente ---")

    nome_cliente = input("Digite seu nome: ")

    novo_codigo = 1

    if clientes:
        novo_codigo = max(cliente.codigo for cliente in clientes) + 1

    from models.cliente import Cliente

    cliente = Cliente(novo_codigo, nome_cliente)
    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")
    print(cliente)

    print("\n--- Produtos disponíveis ---")

    produtos = listar_produtos(produtos)

    for produto in produtos:
        print(produto)

    print("\n--- Compra ---")

    itens = []

    while True:
        codigo_produto = int(
            input("Digite o código do produto que deseja comprar: ")
        )

        quantidade = int(
            input("Digite a quantidade que deseja comprar: ")
        )

        produto = buscar_produto(produtos, codigo_produto)

        if produto is None:
            print("Produto não encontrado.")
            continue

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        if quantidade > produto.quantidade:
            print("Quantidade indisponível em estoque.")
            continue

        subtotal = quantidade * produto.preco

        itens.append({
            "codigo_produto": produto.codigo,
            "quantidade": quantidade,
            "preco_unitario": produto.preco
        })

        print("\nProduto:", produto.nome)
        print("Quantidade:", quantidade)
        print(f"Subtotal: R$ {subtotal:.2f}")

        continuar = input(
            "\nDeseja comprar outro produto? (s/n): "
        ).lower()

        if continuar != "s":
            break

    total = 0

    for item in itens:
        total += item["quantidade"] * item["preco_unitario"]

    print("\n=== RESUMO DA COMPRA ===")
    print(f"Total da compra: R$ {total:.2f}")

    print("\n--- Atualizando estoque ---")

    for item in itens:
        produto = buscar_produto(produtos, item["codigo_produto"])

        nova_quantidade = produto.quantidade - item["quantidade"]

        atualizar_estoque(
            produtos,
            produto.codigo,
            nova_quantidade
        )

    print("Estoque atualizado com sucesso!")

    print("\n--- Registrando venda ---")

    novo_codigo_venda = 1

    if vendas:
        novo_codigo_venda = max(venda.codigo for venda in vendas) + 1

    venda = Venda(
        novo_codigo_venda,
        cliente.codigo,
        itens,
        total
    )

    vendas.append(venda)

    print("Venda registrada com sucesso!")
    print(venda)

    salvar_produtos(produtos)
    salvar_clientes(clientes)
    salvar_vendas(vendas)

    print("Dados salvos com sucesso!")

    print("\n--- Estoque após a compra ---")

    for produto in produtos:
        print(produto)


if __name__ == "__main__":
    main()