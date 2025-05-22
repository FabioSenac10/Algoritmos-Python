cliente=[]
passagem=[]
aviao=[]
tripulacao=[]
while True:
    print("MENU DE OPÇÕES")
    print("1 - CADASTRO DE CLIENTE 1")
    print("2 - CADASTRO DE PASSAGEM 2")
    print("3 - CADASTRO DO AVIÃO 3")
    print("4 - CADASTRO DA TRIPULAÇÃO 4")
    opcao=int(input("DIGITE SUA OPÇÃO: "))
    if opcao==1:
     while True: 
      print(f"\nCADASTRO DO CLIENTE:")
    nome=input("DIGITE SEU NOME: ")
    sobrenome=input("DIGITE SEU SOBRENOME: ")
    try:
     rg=input("DIGITE SEU RG: ")
    except:
     print("DIGITE SOMENTE NÚMEROS ")
    try:
     cpf=int(input("DIGITE SEU CPF: "))
    except:
      print("DIGITE SOMENTE NÚMEROS")
    endereco=input("DIGITE SEU ENDEREÇO: ")
    try:
     fone=int(input("DIGITE SEU TELEFONE COM DDD: "))
    except:
      print("DIGITE SOMENTE NÚMEROS ")
    try:
     idade=input("DIGITE SUA IDADE: ")
    except:
     print("DIGITE SOMENTE NÚMEROS")
    elif opcao==2:
    destino=input("DIGITE SEU DESTINO: ")
    origem=input("DIGITE SEU LOCAL DE ORIGEM: ")
    duracao=input("DIGITE A DURAÇÃO DO VÔO: ")
    valor_passagem

