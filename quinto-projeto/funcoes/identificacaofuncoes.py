# ESTRUTURA BÁSICA COMANDO DEF
# def <identificador da funcao> (<parametros(s)>):
#     <código que será executado>
#     return <dado que será retornado, caso seja necessário>

# Um “Python Package” em Python tem a função de apontar para o PyCharm um pacote
# em que teremos arquivos que poderão ser importados por outros projetos.
# Para criá-lo, clique com o botão direito sobre o diretório e selecione
# a opção New/Python Package.

# Repare que, dentro do pacote gerado, foi criado um arquivo chamado “__init__.py”.
# Não discutiremos sobre esse arquivo agora e ele também não nos será útil.

def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [str(input("Equipamento: ")),
                       float(input("Valor: R$")),
                       int(input("Número Serial: ")),
                       str(input("Departamento: "))]
        lista.append(equipamento)
        resp = str(input('Digite "S" para continuar: ')).upper()


def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........:  R$", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])


def localizarNome(lista):
    busca = str(input("Digite o nome do equipamento que deseja buscar: "))
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..: R$", elemento[1])
            print("Serial.: ", elemento[2])


def depreciarPorNome(lista, porc):
    depreciacao = str(input("Digite o nome do equipamento que será depreciado: "))
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: R$", elemento[1])
            elemento[1] = elemento[1] * (1 - porc / 100)
            print("Novo valor: ", elemento[1])


def excluirPorSerial(lista):
    serial = int(input("Digite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens excluídos"


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
