while True:
    nome=input("Digite seu nome: ")
    if len (nome)<=3:
     print("Nome deve ter mais que 3 caracteres ")
    idade=int(input("Digite sua idade: "))
    if idade<=0 and idade>=150:
     print("Idade deve estar entre 0 e 150 anos")
    sexo=input("Digite seu sexo(F= feminino, M-masculino e O=outro): ")
    if sexo!="F" and sexo!="f" and sexo!="M" and sexo!="m" and sexo!="O" and sexo!="o":
     print("Digite uma opção valida")
    est_civil=input("Estado civil(S=Solteiro, C=Casado), V=viúvo e D=Divorciado: ")
    if est_civil!="S" and est_civil!="s" and est_civil!="C" and est_civil!="c" and est_civil!="V" and est_civil!="v" and est_civil!="D" and est_civil!="d":
     print("Digite uma opção vãlida.")
    print(nome, idade, sexo, est_civil)
    break