from services.persistencia_service import (
    carregar_produtos,
    carregar_clientes,
    carregar_vendas
)

from services.estoque_service import listar_produtos


def main():
    print("Sistema de Vendas")

    produtos = carregar_produtos()
    clientes = carregar_clientes()
    vendas = carregar_vendas()

    produtos = listar_produtos(produtos)

    for produto in produtos:
        print(produto)


if __name__ == "__main__":
    main()