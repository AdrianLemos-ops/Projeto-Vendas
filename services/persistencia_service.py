import csv
from models.produto import produto_from_csv_row
from models.cliente import cliente_from_csv_row
from models.venda import venda_from_csv_row

def salvar_produtos(produtos):
    caminho = "data/produtos.csv"

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["codigo", "nome", "preco", "quantidade"])

        for produto in produtos:
            escritor.writerow(produto.to_csv_row())

def carregar_produtos():
    caminho = "data/produtos.csv"

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            produtos = []

            for linha in leitor:
                produtos.append(produto_from_csv_row(linha))

            return produtos

def salvar_clientes(clientes):
    caminho = "data/clientes.csv"

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["codigo", "nome"])

        for cliente in clientes:
            escritor.writerow(cliente.to_csv_row())


def carregar_clientes():
    caminho = "data/clientes.csv"

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        clientes = []

        for linha in leitor:
            clientes.append(cliente_from_csv_row(linha))

        return clientes

def salvar_vendas(vendas):
    caminho = "data/vendas.csv"

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["codigo", "codigo_cliente", "itens", "valor_total"])

        for venda in vendas:
            escritor.writerow(venda.to_csv_row())

def carregar_vendas():
    caminho = "data/vendas.csv"

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        vendas = []

        for linha in leitor:
            vendas.append(venda_from_csv_row(linha))

        return vendas