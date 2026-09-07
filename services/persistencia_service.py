import csv
from models.produto import produto_from_csv_row

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