equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(str(input("Equipamento: ")))
    valores.append(float(input("Valor: R$")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(str(input("Departamento: ")))
    resposta = str(input('Digite "S" para continuar: ')).strip().upper()

for indice in range(0, len(equipamentos)):
    print("\nEquipamento.....: ", (indice + 1))
    print("Nome............: ", equipamentos[indice])
    print("Valor...........: ", valores[indice])
    print("Serial..........: ", seriais[indice])
    print("Departamento....: ", departamentos[indice])

danificado = str(input("\nAlgum equipamento está danificado? [S/N] ")).strip().upper()
if danificado == "S":
    serial = int(input("Informe o serial para deletar o equipamento da lista: "))
    for indice in range(0, len(seriais)):
        if serial == seriais[indice]:
            del seriais[indice]
            del equipamentos[indice]
            del valores[indice]
            del departamentos[indice]
            break
else:
    print("Obrigado por informar!")

depreciacao = str(input("\nDigite o nome do equipamento que será depreciado: "))

for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.:", seriais[indice])
