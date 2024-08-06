nivel = str(input("Digite o nível do seu acesso: (ADM, USR OU GUEST) ")).strip().upper()
genero = str(input("Qual seu sexo? [M/F] ")).strip().upper()

# PRIMEIRA VERIFICAÇÃO
if nivel == "ADM" and genero == "M":
    print("Olá administrador!")
elif nivel == "ADM" and genero == "F":
    print("Olá administradora!")

# SEGUNDA VERIFICAÇÃO
if nivel == "USR" and genero == "M":
    print("Olá usuário!")
elif nivel == "USR" and genero == "F":
    print("Olá usuária!")

# TERCEIRA VERIFICAÇÃO
if nivel == "GUEST":
    print("Olá visitante!")

if not nivel == "USR" and not nivel == "ADM" and not nivel == "GUEST":
    print("Olá desconhecido(a)")
