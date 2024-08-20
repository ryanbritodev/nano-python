inventario = list()
resposta = "S"
while resposta == "S":
    inventario.append(str(input("Equipamento: ")))
    inventario.append(float(input("Valor: R$")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input('Digite [S] para continuar: ')
print("Encerrando programa...")

for elemento in inventario:
    print(elemento)
