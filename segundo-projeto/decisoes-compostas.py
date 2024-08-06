nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a idade: "))
doenca = str(input("Suspeita de doença infecto-contagiosa? [SIM/NÃO] ").strip().upper())
if idade >= 65 and doenca == "SIM":
    print(f"O paciente {nome} será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca == "SIM":
    print(f"O paciente {nome} será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca == "NÃO":
    print(f"O paciente {nome} será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca == "NÃO":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectcontagiosa com SIM ou NÃO")
