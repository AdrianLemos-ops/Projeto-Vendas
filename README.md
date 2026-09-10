# Projeto-Vendas

Projeto desenvolvido para a disciplina de Estrutura de Dados.

## Integrantes

* Thiago Corrêa Medeiros — RA 1134836
* Vitor Gomide — RA 1140037
* Adrian Augusto Munaretti de Lemos — RA 1139696

## Descrição

O projeto consiste em um sistema de vendas desenvolvido em Python e executado pelo terminal.

O sistema permite cadastrar e consultar clientes e produtos, atualizar o estoque, realizar vendas e consultar informações sobre as vendas realizadas.

Os dados são armazenados em arquivos CSV para que possam ser carregados novamente quando o sistema for executado.

## Estruturas de dados

Foram utilizadas as seguintes estruturas:

* LSE para os clientes;
* LDE para os produtos;
* Fila para as vendas;
* Pilha para o histórico das operações e para desfazer a última operação.

## Algoritmos

Foram utilizados:

* Ordenação por Inserção para ordenar os produtos pelo código;
* Busca Binária para realizar a busca de produtos pelo código.

## Funcionalidades

O sistema possui opções para:

* cadastrar, listar, buscar e remover clientes;
* cadastrar, listar, buscar, atualizar e remover produtos;
* realizar vendas;
* controlar o estoque;
* visualizar a fila de vendas;
* consultar o valor do estoque e das vendas;
* consultar os valores gastos pelos clientes;
* verificar o cliente que mais gastou;
* verificar o produto mais vendido;
* desfazer a última operação.

## Organização

```text
Projeto-Vendas/
├── main.py
├── models/
├── estruturas/
├── algoritmos/
├── services/
├── data/
└── README.md
```

## Execução

Para executar o sistema, abra o terminal na pasta do projeto e execute:

```text
python main.py
```
