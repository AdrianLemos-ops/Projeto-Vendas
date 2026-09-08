from services.persistencia_service import (
    carregar_produtos,
    carregar_clientes,
    carregar_vendas
)

from services.estoque_service import listar_produtos, buscar_produto, atualizar_estoque


def main():
    print("Sistema de Vendas")

    produtos = carregar_produtos()
    clientes = carregar_clientes()
    vendas = carregar_vendas()

    produto = buscar_produto(produtos, 1)

    if produto:
        print("Produto encontrado:", produto)

    resultado = atualizar_estoque(produtos, 1, 15)

    print("Estoque atualizado:", resultado)

    for produto in produtos:
        print(produto)


if __name__ == "__main__":
    main()