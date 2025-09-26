while True:
    nome=input("Digite seu nome: ")
    senha=input("Digite sua senha: ")
    if nome!=senha:
     print("Acesso liberado")
    else:
       print("Erro, senha não pode ser igual o nome.")
    break