from services.persistencia_service import (
    carregar_produtos,
    carregar_clientes,
    carregar_vendas
)


def main():
    print("Sistema de Vendas")

    produtos = carregar_produtos()
    clientes = carregar_clientes()
    vendas = carregar_vendas()

    for produto in produtos:
        print(produto)


if __name__ == "__main__":
    main()