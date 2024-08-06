nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))
doenca = str(input("Suspeita de doença infectocontagiosa? [S/N] ")).strip().upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca == "S":
        print(f"Encaminhe o paciente {nome} para sala AMARELA")
    elif doenca == "N":
        print(f"Encaminhe o paciente {nome} para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM [S] ou NÃO [N]")
if idade < 65:
    print("Paciente SEM prioridade")
    if doenca == "S":
        print(f"Encaminhe o paciente {nome} para sala AMARELA")
    elif doenca == "N":
        print(f"Encaminhe o paciente {nome} para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM [S] ou NÃO [N]")
