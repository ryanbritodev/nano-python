nome = str(input("Digite seu nome: "))
idade = int(input("Digite a idade: "))
doenca = str(input("Suspeita de doença infectocontagiosa? [S/N] ")).strip().upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca == "S":
    print("Encaminhe o paciente para sala AMARELA")
elif doenca == "N":
    print("Encaminhe o paciente para sala BRANCA")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    sexo = str(input("Digite o gênero do paciente: [M/F] ")).strip().upper()
    if sexo == "F" and idade > 10:
        gravidez = str(input("A paciente está grávida? [S/N] ")).strip().upper()
        if gravidez == "S":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
