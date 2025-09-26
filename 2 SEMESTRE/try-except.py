cliente = []
passagem = []
aviao = []
tripulacao = {}

while True:
    print("\nMENU DE OPÇÕES")
    print("1 - CADASTRO DE CLIENTE")
    print("2 - CADASTRO DE PASSAGEM")
    print("3 - CADASTRO DO AVIÃO")
    print("4 - CADASTRO DA TRIPULAÇÃO")
    print("5 - EXIBIR DADOS CADASTRADOS")
    print("0 - SAIR")
    
    try:
        opcao = int(input("DIGITE SUA OPÇÃO: "))
    except ValueError:
        print("DIGITE UMA OPÇÃO VÁLIDA!")
        continue

    if opcao == 0:
        print("SAIR")
        break

    elif opcao == 1:
        print(f"\nCADASTRO DO CLIENTE:")
        nome = input("DIGITE SEU NOME: ")
        if not nome.replace(" ", "").isalpha():
           print("NOME INVÁLIDO! DIGITE APENAS LETRAS.")
           continue

        sobrenome = input("DIGITE SEU NOME: ")
        if not sobrenome.replace(" ", "").isalpha():
           print("NOME INVÁLIDO! DIGITE APENAS LETRAS.")
           continue

        rg = input("DIGITE SEU RG: ")
        try:
            cpf = int(input("DIGITE SEU CPF: "))
        except ValueError:
            print("DIGITE SOMENTE NÚMEROS")
            continue

        endereco = input("DIGITE SEU ENDEREÇO: ")
        try:
            fone = int(input("DIGITE SEU TELEFONE COM DDD: "))
        except ValueError:
            print("DIGITE SOMENTE NÚMEROS")
            continue

        idade = input("DIGITE SUA IDADE: ")
        
        cliente.append({
            "nome": nome,
            "sobrenome": sobrenome,
            "rg": rg,
            "cpf": cpf,
            "endereco": endereco,
            "telefone": fone,
            "idade": idade
        })

    elif opcao == 2:
        print("\nCADASTRO DE PASSAGEM:")
        destino = input("DIGITE SEU DESTINO: ")
        origem = input("DIGITE SEU LOCAL DE ORIGEM: ")
        duracao = input("DIGITE A DURAÇÃO DO VÔO: ")

        try:
            valor_passagem = float(input("DIGITE O VALOR DA PASSAGEM: "))
        except ValueError:
            print("DIGITE SOMENTE NÚMEROS")
            continue

        desconto = valor_passagem * 0.95
        print("O valor da passagem com desconto de 5% é R$ ", desconto)

        passagem.append({
            "destino": destino,
            "origem": origem,
            "duração": duracao,
            "valor_passagem": valor_passagem,
            "desconto": desconto
        })

    elif opcao == 3:
        print("\nCADASTRO DO AVIÃO:")
        modelo = input("DIGITE O MODELO DO AVIÃO: ")

        try:
            ano = int(input("DIGITE O ANO DE FABRICAÇÃO DO AVIÃO: "))
            hora_voo = int(input("DIGITE O TEMPO DE VÔO DA AERONAVE (HORAS): "))
            quant_passageiro = int(input("DIGITE A QUANTIDADE DE PASSAGEIROS: "))
        except ValueError:
            print("DIGITE SOMENTE NÚMEROS")
            continue

        cor = input("DIGITE A COR DA AERONAVE: ")
        if cor.isdigit():
            print("COR INVÁLIDA! NÃO DIGITE NÚMEROS.")
            continue

        aviao.append({
            "modelo": modelo,
            "ano": ano,
            "hora_voo": hora_voo,
            "cor": cor,
            "quant_passageiro": quant_passageiro
        })

    elif opcao == 4:
        while True:
            print("\n===== MENU TRIPULAÇÃO =====")
            print("1 - CADASTRAR PILOTO")
            print("2 - CADASTRAR COPILOTO")
            print("3 - CADASTRAR COMISSÁRIO")
            print("0 - VOLTAR")
            
            opcao_tripulacao = input("Escolha uma opção: ")
            if opcao_tripulacao == "0":
                break

            
            idade = input("Idade: ")
            admissao = input("Data de admissão: ")
            telefone = input("Telefone: ")
            membro = {
                "Nome": nome,
                "Idade": idade,
                "Admissão": admissao,
                "Telefone": telefone
            }

            if opcao_tripulacao == "1":
                tripulacao["Piloto"] = membro
            elif opcao_tripulacao == "2":
                tripulacao["Copiloto"] = membro
            elif opcao_tripulacao == "3":
                if "Comissarios" not in tripulacao:
                    tripulacao["Comissarios"] = []
                tripulacao["Comissarios"].append(membro)
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao == 5:
        print("\n--- DADOS CADASTRADOS ---")
        print("\nClientes:")
        for c in cliente:
            print(c)

        print("\nPassagens:")
        for p in passagem:
            print(p)

        print("\nAviões:")
        for a in aviao:
            print(a)

        print("\nTripulação:")
        for tipo, dados in tripulacao.items():
            print(f"{tipo}: {dados}")

    else:
        print("OPÇÃO INVÁLIDA!")

