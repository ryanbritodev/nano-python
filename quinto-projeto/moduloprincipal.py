from funcoes.identificacaofuncoes import *

minhaLista = []
print("Preenchendo...")
preencherInventario(minhaLista)
print("Exibindo...")
exibirInventario(minhaLista)

print("Pesquisando...")
localizarNome(minhaLista)
print("Alterando...")
depreciarPorNome(minhaLista, 20)

print("Excluindo...")
print(excluirPorSerial(minhaLista)) # Função possui retorno, por isso está dentro do print()
print("Exibindo...")
exibirInventario(minhaLista)

print("Resumindo...")
resumirValores(minhaLista)
