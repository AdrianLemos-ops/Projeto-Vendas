from services.persistencia_service import (
    carregar_produtos,
    carregar_clientes,
    carregar_vendas,   
)

from services.estoque_service import EstoqueService

def main():
    print("=== SISTEMA DE VENDAS ===")

    service = EstoqueService()

    produtos = carregar_produtos()
    clientes = carregar_clientes()
    vendas = carregar_vendas()

    for produto in produtos:
        service.produtos.inserir_fim(produto)

    for cliente in clientes:
        service.clientes.inserir_fim(cliente)

    for venda in vendas:
        service.vendas.enqueue(venda)

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Remover cliente")
        print("5 - Cadastrar produto")
        print("6 - Listar produtos")
        print("7 - Buscar produto")
        print("8 - Atualizar estoque")
        print("9 - Remover produto")
        print("10 - Listar produtos em ordem inversa")
        print("11 - Listar produtos ordenados por ID")
        print("12 - Buscar produto por ID com Busca Binária")
        print("13 - Realizar venda simples de exemplo")
        print("14 - Visualizar fila de vendas")
        print("15 - Visualizar primeira venda da fila")
        print("16 - Valor total do estoque")
        print("17 - Valor total das vendas")
        print("18 - Clientes e valores totais gastos")
        print("19 - Cliente que mais gastou")
        print("20 - Produto mais vendido")
        print("21 - Desfazer última operação")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Sistema encerrado.")
            break

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")

            cliente = service.cadastrar_cliente(nome)

            print("\nCliente cadastrado com sucesso!")
            print(cliente)

        if opcao == "2":
            clientes = service.listar_clientes()

            print("\n=== CLIENTES ===")

            for cliente in clientes:
                print(cliente)
        
        if opcao == "3":
            codigo = int(input("Digite o código do cliente: "))

            cliente = service.buscar_cliente(codigo)

            if cliente is None:
                print("\nCliente não encontrado.")
            else:
                print("\nCliente encontrado!")
                print(cliente)
        
        if opcao == "4":
            codigo = int(input("Digite o código do cliente que deseja remover: "))

            resultado = service.remover_cliente(codigo)

            if resultado:
                print("\nCliente removido com sucesso!")
            else:
                print("\nCliente não encontrado.")

        if opcao == "5":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade em estoque: "))

            produto = service.cadastrar_produto(
                nome,
                preco,
                quantidade
            )

            print("\nProduto cadastrado com sucesso!")
            print(produto)

        if opcao == "6":
            produtos = service.listar_produtos()

            print("\n=== PRODUTOS ===")

            for produto in produtos:
                print(produto)
        
        if opcao == "7":
            codigo = int(input("Digite o código do produto: "))

            produto = service.buscar_produto(codigo)

            if produto is None:
                print("\nProduto não encontrado.")
            else:
                print("\nProduto encontrado!")
                print(produto)
        
        if opcao == "8":
            codigo = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite a nova quantidade em estoque: "))

            resultado = service.atualizar_estoque(
                codigo,
                quantidade
            )

            if resultado:
                print("\nEstoque atualizado com sucesso!")
            else:
                print("\nProduto não encontrado.")
            
        if opcao == "9":
            codigo = int(input("Digite o código do produto que deseja remover: "))

            resultado = service.remover_produto(codigo)

            if resultado:
                print("\nProduto removido com sucesso!")
            else:
                print("\nProduto não encontrado.")

        if opcao == "10":
            produtos = service.listar_produtos_inverso()

            print("\n=== PRODUTOS EM ORDEM INVERSA ===")

            for produto in produtos:
                print(produto)
        
        if opcao == "11":
            produtos = service.listar_produtos_ordenados()

            print("\n=== PRODUTOS ORDENADOS POR ID ===")

            for produto in produtos:
                print(produto)

        if opcao == "12":
            codigo = int(input("Digite o código do produto: "))
            produto = service.buscar_produto_binario(codigo)
            
            if produto is None:
                print("\nProduto não encontrado.")
            else:
                print("\nProduto encontrado!")
                print(produto)
            
        if opcao == "13":
            codigo_cliente = int(input("Digite o código do cliente: "))

            itens = []

            while True:
                codigo_produto = int(
                    input("Digite o código do produto: ")
                )

                quantidade = int(
                    input("Digite a quantidade: ")
                )

                produto = service.buscar_produto(codigo_produto)

                if produto is None:
                    print("\nProduto não encontrado.")
                    continue

                if quantidade <= 0:
                    print("\nA quantidade deve ser maior que zero.")
                    continue

                itens.append({
                    "codigo_produto": codigo_produto,
                    "quantidade": quantidade
                })

                continuar = input(
                    "Deseja adicionar outro produto? (s/n): "
                ).lower()

                if continuar != "s":
                    break

            venda = service.realizar_venda(
                codigo_cliente,
                itens
            )

            if venda is False:
                print("\nNão foi possível realizar a venda.")
            else:
                print("\nVenda realizada com sucesso!")
                print(venda)

        if opcao == "14":
            vendas = service.listar_vendas()

            print("\n=== FILA DE VENDAS ===")

            if not vendas:
                print("Não há vendas na fila.")
            else:
                for venda in vendas:
                    print(venda)

        if opcao == "15":
            venda = service.primeira_venda()

            if venda is None:
                print("\nNão há vendas na fila.")
            else:
                print("\n=== PRIMEIRA VENDA DA FILA ===")
                print(venda)

        if opcao == "16":
            total = service.valor_total_estoque()

            print("\n=== VALOR TOTAL DO ESTOQUE ===")
            print(f"R$ {total:.2f}")

        if opcao == "17":
            total = service.valor_total_vendas()

            print("\n=== VALOR TOTAL DAS VENDAS ===")
            print(f"R$ {total:.2f}")

        if opcao == "18":
            gastos = service.totais_gastos_por_cliente()

            print("\n=== CLIENTES E VALORES GASTOS ===")

            for cliente, total in gastos:
                print(f"{cliente} | Total gasto: R$ {total:.2f}")

        if opcao == "19":
            resultado = service.cliente_que_mais_gastou()

            if resultado is None:
                print("\nNão há vendas registradas.")
            else:
                cliente, total = resultado

                print("\n=== CLIENTE QUE MAIS GASTOU ===")
                print(cliente)
                print(f"Total gasto: R$ {total:.2f}")

        if opcao == "20":
            resultado = service.produto_mais_vendido()

            if resultado is None:
                print("\nNão há vendas registradas.")
            else:
                produto, quantidade = resultado

                print("\n=== PRODUTO MAIS VENDIDO ===")
                print(produto)
                print(f"Quantidade vendida: {quantidade}")

        if opcao == "21":
            resultado = service.desfazer_ultima_operacao()

            if resultado:
                print("\nÚltima operação desfeita com sucesso!")
            else:
                print("\nNão há operações para desfazer.")


if __name__ == "__main__":
    main()