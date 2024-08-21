usuarios = {
    "Chaves": ["Chaves Silva", "21/08/2024", "Recep_01"],
    "Quico": ["Enrico Flores", "03/06/2024", "Raiox_02"],
    "Quico": ["Enrico Flores", "03/06/2024", "Raiox_03"]
}

# Adicionando itens no dicionário
# Caso os itens sejam repetidos (como a chave Quico e Florinda, com uma mesma chave, o objeto que estiver na linha mais abaixo vai sobrescrever
# o item acima dele, seguindo essa lógica sucessivamente

usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"] = ["Florinda Flores", "26/11/2016", "Recep_01"]

print(usuarios)
print("##############========#########")
print("Dados Chaves:", usuarios.get("Chaves"))
print("Dados Chapolin:", usuarios.get("Chapolim"))


# Caso pesquisemos um valor que não está presente na lista,
# o console do Python retornará "None", representando um valor
# que não foi encontrado dentro do dicionário.

# print(usuarios["Chaves"][0]) <--- Como acessar
