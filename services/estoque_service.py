from algoritmos.ordenacao import ordenar_produtos_por_id
from algoritmos.busca_binaria import buscar_produto_por_id

def listar_produtos(produtos):
    produtos_ordenados = ordenar_produtos_por_id(produtos)
    return produtos_ordenados

def buscar_produto(produtos, codigo):
    produtos_ordenados = ordenar_produtos_por_id(produtos)
    return buscar_produto_por_id(produtos_ordenados, codigo)

def atualizar_estoque(produtos, codigo, quantidade):
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        return False

    produto.atualizar_estoque(quantidade)
    return True

def remover_produto(produtos, codigo):
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        return False


    produtos.remove(produto)
    return True
