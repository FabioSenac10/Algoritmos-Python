cadastro = []
while True:
    print("\n===== MENU =====")
    print("1 - CADASTRO DE CLIENTE")
    print("2 - CONSULTAR DADOS")
    print("3 - SAIR")
    print("================\n")
    try:
        opcao = int(input("DIGITE SUA OPÇÃO: "))
    except ValueError:
        print("DIGITE UMA OPÇÃO VÁLIDA!")
        continue

    if opcao == 3:
        print("SAIR")
        break

    elif opcao == 1:
        print(f"\nCADASTRO DO CLIENTE:")
        nome = input("DIGITE SEU NOME: ").strip().upper()
        if not nome.replace(" ", "").isalpha():
           print("NOME INVÁLIDO! DIGITE APENAS LETRAS.")
           continue
        try:
            idade=int(input("DIGITE SUA IDADE: "))
        except ValueError:
            print("DIGITE SOMENTE NÚMEROS")
            continue
        sexo=input("DIGITE SEU SEXO: ")
        if not sexo.replace(" ", "").isalpha():
           print("NOME INVÁLIDO! DIGITE APENAS LETRAS.")
           continue
        try:
            cpf = int(input("DIGITE SEU CPF: "))
        except ValueError:
            print("DIGITE SOMENTE NÚMEROS")
            continue
        endereco= input("DIGITE SEU ENDEREÇO: ")
        cidade=input("DIGITE SUA CIDADE: ")
        estado=input("DIGITE SEU ESTADO: ")
        cadastro.append({
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
            "cpf": cpf,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado
        })
        print("Cadastro realizado com sucesso!")
    elif opcao == 2:
       if not cadastro:
        print("NENHUM CADASTRO ENCONTRADO.")
        continue

    nome_busca = input("DIGITE O NOME PARA CONSULTA: ").strip().upper()
    encontrado = False

    for pessoa in cadastro:
        if pessoa["nome"] == nome_busca:
            print("\n--- DADOS DO CLIENTE ---")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Sexo: {pessoa['sexo']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"Cidade: {pessoa['cidade']}")
            print(f"Estado: {pessoa['estado']}")
            print("------------------------")
            encontrado = True
            break

    if not encontrado:
        print(f"NENHUM CLIENTE COM O NOME '{nome_busca}' FOI ENCONTRADO.")