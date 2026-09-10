from algoritmos.ordenacao import ordenar_produtos_por_id
from algoritmos.busca_binaria import buscar_produto_por_id

from estruturas.lse import LSE
from estruturas.lde import LDE
from estruturas.fila import Fila
from estruturas.pilha import Pilha

from models.cliente import Cliente
from models.produto import Produto
from models.venda import Venda

from services.persistencia_service import (
    salvar_produtos,
    salvar_clientes,
    salvar_vendas
)

class EstoqueService:
    def __init__(self):
        self.clientes = LSE()
        self.produtos = LDE()
        self.vendas = Fila()
        self.historico = Pilha()

    def salvar_dados(self):
        salvar_clientes(self.clientes.listar())
        salvar_produtos(self.produtos.listar())
        salvar_vendas(self.vendas.listar())

    def gerar_proximo_codigo_cliente(self):
        if self.clientes.is_empty():
            return 1
        
        clientes = self.clientes.listar()

        maior_codigo = 0

        for cliente in clientes:
            if cliente.codigo > maior_codigo:
                maior_codigo = cliente.codigo

        return maior_codigo + 1
    
    def cadastrar_cliente(self, nome):
        codigo = self.gerar_proximo_codigo_cliente()
        cliente = Cliente(codigo, nome)
        self.clientes.inserir_fim(cliente)
        self.historico.push(("cadastrar_cliente", cliente))
        self.salvar_dados()
        return cliente
     
    def listar_clientes(self):
        return self.clientes.listar()
    
    def buscar_cliente(self, codigo):
        return self.clientes.buscar(codigo)
    
    def remover_cliente(self, codigo):
        cliente = self.clientes.remover(codigo)

        if cliente is None:
            return False
        
        self.historico.push(("remover_cliente", cliente))

        self.salvar_dados()

        return True
    
    def gerar_proximo_codigo_produto(self):
        if self.produtos.is_empty():
            return 1
        
        produtos = self.produtos.listar()

        maior_codigo = 0

        for produto in produtos:
            if produto.codigo > maior_codigo:
                maior_codigo = produto.codigo

        return maior_codigo + 1
    
    def cadastrar_produto(self, nome, preco, quantidade):
        codigo = self.gerar_proximo_codigo_produto()

        produto = Produto(codigo, nome, preco, quantidade)

        self.produtos.inserir_fim(produto)

        self.historico.push(("cadastrar_produto", produto))

        self.salvar_dados()

        return produto
        
    def listar_produtos(self):
        return self.produtos.listar()
    
    def buscar_produto(self, codigo):
        produtos = self.produtos.listar()
        
        for produto in produtos:
            if produto.codigo == codigo:
                return produto
        
        return None
    
    def buscar_produto_binario(self, codigo):
        produtos = self.produtos.listar()
        produtos_ordenados = ordenar_produtos_por_id(produtos)
        
        return buscar_produto_por_id(produtos_ordenados, codigo)
    
    def atualizar_estoque(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)

        if produto is None:
            return False
        
        quantidade_anterior = produto.quantidade

        produto.atualizar_estoque(quantidade)

        self.historico.push(
            ("atualizar_estoque", produto, quantidade_anterior)
        )

        self.salvar_dados()

        return True
    
    def remover_produto(self, codigo):
        produto = self.produtos.remover(codigo)

        if produto is None:
            return False
        
        self.historico.push(("remover_produto", produto))

        self.salvar_dados()

        return True
    
    def listar_produtos_inverso(self):
        return self.produtos.listar_inverso()
    
    def listar_produtos_ordenados(self):
        produtos = self.produtos.listar()
        return ordenar_produtos_por_id(produtos)
    
    def gerar_proximo_codigo_venda(self):
        if self.vendas.is_empty():
            return 1
        
        vendas = self.vendas.listar()

        maior_codigo = 0

        for venda in vendas:
            if venda.codigo > maior_codigo:
                maior_codigo = venda.codigo

        return maior_codigo + 1
    
    def realizar_venda(self, codigo_cliente, itens):
        cliente = self.buscar_cliente(codigo_cliente)

        if cliente is None:
            return False
        
        if not itens:
            return False

        produtos_venda = []

        for item in itens:
            produto = self.buscar_produto(item["codigo_produto"])

            if produto is None:
                return False
            
            if item["quantidade"] <= 0:
                return False

            quantidade_total = item["quantidade"]

            for outro_item in itens:
                if outro_item is not item:
                    if outro_item["codigo_produto"] == item["codigo_produto"]:
                        quantidade_total += outro_item["quantidade"]

            if quantidade_total > produto.quantidade:
                return False

            produtos_venda.append(produto)

        itens_venda = []

        for item, produto in zip(itens, produtos_venda):
            item_venda = {
                "codigo_produto": produto.codigo,
                "quantidade": item["quantidade"],
                "preco_unitario": produto.preco
            }

            itens_venda.append(item_venda)

        codigo_venda = self.gerar_proximo_codigo_venda()

        for item, produto in zip(itens, produtos_venda):
            produto.atualizar_estoque(
                produto.quantidade - item["quantidade"]
            )
        

        venda = Venda(codigo_venda, codigo_cliente, itens_venda)

        self.vendas.enqueue(venda)

        self.historico.push(("realizar_venda", venda, produtos_venda))

        self.salvar_dados()

        return venda
    
    def listar_vendas(self):
        return self.vendas.listar()
    
    def primeira_venda(self):
        if self.vendas.is_empty():
            return None
        
        return self.vendas.front()
    
    def valor_total_estoque(self):
        total = 0

        produtos = self.produtos.listar()

        for produto in produtos:
            total += produto.quantidade * produto.preco

        return total
    
    def valor_total_vendas(self):
        total = 0

        vendas = self.vendas.listar()

        for venda in vendas:
            total += venda.valor_total

        return total
    
    def totais_gastos_por_cliente(self):
        resultados = []

        clientes = self.clientes.listar()

        for cliente in clientes:
            total = 0 

            vendas = self.vendas.listar()

            for venda in vendas:
                if venda.codigo_cliente == cliente.codigo:
                    total += venda.valor_total

            resultados.append((cliente, total))

        return resultados
    
    def cliente_que_mais_gastou(self):
        resultados = self.totais_gastos_por_cliente()

        if len(resultados) == 0:
            return None
        
        maior_total = resultados[0]

        for resultado in resultados:
            if resultado[1] > maior_total[1]:
                maior_total = resultado

        return maior_total
    
    def produto_mais_vendido(self):
        vendas = self.vendas.listar()
        totais_por_produto = {}

        for venda in vendas:
            for item in venda.itens:
                codigo_produto = item["codigo_produto"]

                if codigo_produto not in totais_por_produto:
                    totais_por_produto[codigo_produto] = item["quantidade"]

                else:
                    totais_por_produto[codigo_produto] += item["quantidade"]

        maior_codigo = None
        maior_quantidade = 0

        for codigo, quantidade in totais_por_produto.items():
            if quantidade > maior_quantidade:
                maior_quantidade = quantidade
                maior_codigo = codigo

        if maior_codigo is None:
            return None
        
        produto = self.buscar_produto(maior_codigo)

        return produto, maior_quantidade
    
    def desfazer_ultima_operacao(self):
        if self.historico.is_empty():
            return False
        
        operacao = self.historico.pop()
        tipo = operacao[0]

        if tipo == "cadastrar_cliente":
            cliente = operacao[1]
            self.clientes.remover(cliente.codigo)
            self.salvar_dados()
            return True
        
        if tipo == "cadastrar_produto":
            produto = operacao[1]
            self.produtos.remover(produto.codigo)
            self.salvar_dados()
            return True
        
        if tipo == "remover_cliente":
            cliente = operacao[1]
            self.clientes.inserir_fim(cliente)
            self.salvar_dados()
            return True
        
        if tipo == "remover_produto":
            produto = operacao[1]
            self.produtos.inserir_fim(produto)
            self.salvar_dados()
            return True
        
        if tipo == "atualizar_estoque":
            produto = operacao[1]
            quantidade_anterior = operacao[2]
            produto.atualizar_estoque(quantidade_anterior)
            self.salvar_dados()
            return True
        
        if tipo == "realizar_venda":
            venda = operacao[1]
            produtos_venda = operacao[2]

            for item, produto in zip(venda.itens, produtos_venda):
                produto.atualizar_estoque(
                    produto.quantidade + item["quantidade"]
                )

            vendas = self.vendas.listar()
            nova_fila = []

            for venda_fila in vendas:
                if venda_fila is not venda:
                    nova_fila.append(venda_fila)

            self.vendas = Fila()

            for venda_fila in nova_fila:
                self.vendas.enqueue(venda_fila)

            self.salvar_dados()
            return True

            

    
    

