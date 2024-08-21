import time

usuarios = {}

opcao = str(input("""== O que deseja realizar? ==
< I > - Inserir um usuário
< P > - Pesquisar um usuário
< E > - Excluir um usuário
< L > - Listar um usuário
< S > - Sair
\nOpção: """)).strip().upper()[0]

while True:
    if opcao == "I":
        chave = str(input("\nDigite o login: ")).strip().upper()
        usuarios[chave] = [str(input("Digite o nome: ")).strip().upper(),
                           str(input("Digite a última data de acesso: ")).strip(),
                           str(input("Digite a última estação acessada: ")).strip().upper()]
        print("\nUsuário cadastrado com sucesso!\n")
        opcao = str(input("""== O que deseja realizar? ==
< I > - Inserir um usuário
< P > - Pesquisar um usuário
< E > - Excluir um usuário
< L > - Listar um usuário
< S > - Sair
\nOpção: """)).strip().upper()[0]
    elif opcao == "P":
        pesquisa = str(input("\nDigite o login do usuário para consultar seus dados: ")).strip().upper()
        if usuarios.get(pesquisa) is None:
            print("\nUsuário não encontrado!\n")
        else:
            print(f"\nDados do usuário {pesquisa}: {usuarios.get(pesquisa)}\n")
        opcao = str(input("""== O que deseja realizar? ==
< I > - Inserir um usuário
< P > - Pesquisar um usuário
< E > - Excluir um usuário
< L > - Listar um usuário
< S > - Sair
\nOpção: """)).strip().upper()[0]
    elif opcao == "E":
        excluir = str(input("\nDigite o login do usuário que deseja excluir: ")).strip().upper()
        if usuarios.get(excluir) is None:
            print("\nUsuário não encontrado!\n")
        else:
            del usuarios[excluir]
            print("\nUsuário excluído com sucesso!\n")
        opcao = str(input("""== O que deseja realizar? ==
< I > - Inserir um usuário
< P > - Pesquisar um usuário
< E > - Excluir um usuário
< L > - Listar um usuário
< S > - Sair
\nOpção: """)).strip().upper()[0]
    elif opcao == "L":
        for chave, valor in usuarios.items():
            print("Objeto......")
            print("Login: ", chave)
            print("Dados: ", valor)
    elif opcao == "S":
        print("\nEncerrando programa...")
        time.sleep(2)
        print("Programa encerrado!")
        break
    else:
        print("\nOpção inválida! Tente novamente\n")
        opcao = str(input("""== O que deseja realizar? ==
< I > - Inserir um usuário
< P > - Pesquisar um usuário
< E > - Excluir um usuário
< L > - Listar um usuário
< S > - Sair
\nOpção: """)).strip().upper()[0]
        continue
