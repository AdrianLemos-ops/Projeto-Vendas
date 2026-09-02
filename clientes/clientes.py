from dados.banco import clientes


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")

    cliente = {
        "nome": nome,
        "cpf": cpf
    }

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    print("\n--- CLIENTES CADASTRADOS ---")

    for cliente in clientes:
        print("Nome:", cliente["nome"])
        print("CPF:", cliente["cpf"])
        print("----------------------------")