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
    
    elif opcao==1:
        print(f"\nCADASTRO DO CLIENTE:")
        nome = input("DIGITE SEU NOME: ")
        if nome.isdigit():
            print("NOME INVÁLIDO! NÃO DIGITE NÚMEROS.")
        else:
            break
        sobrenome = input("DIGITE SEU SOBRENOME: ")
        if sobrenome.isdigit():
            print("NOME INVÁLIDO! NÃO DIGITE NÚMEROS.")
        else:
            break
        rg=input("DIGITE SEU RG: ")
        try:
            cpf=int(input("DIGITE SEU CPF: "))
        except:
            print("DIGITE SOMENTE NÚMEROS")

        endereco=input("DIGITE SEU ENDEREÇO: ")
        try:
            fone=int(input("DIGITE SEU TELEFONE COM DDD: "))
        except:
            print("DIGITE SOMENTE NÚMEROS ")
            continue
        try:
           idade=input("DIGITE SUA IDADE: ")
        except:
            print("DIGITE SOMENTE NÚMEROS")
            continue
        cliente.append({
            "nome": nome,
            "sobrenome": sobrenome,
            "rg": rg,
            "cpf": cpf,
            "endereco": endereco,
            "telefone": fone,
            "idade": idade
        })
    elif opcao==2:
        print("\nCADASTRO DE PASSAGEM:")
        destino=input("DIGITE SEU DESTINO: ")
        origem=input("DIGITE SEU LOCAL DE ORIGEM: ")
        try:
            duracao=input("DIGITE A DURAÇÃO DO VÔO: ")
        except:
            print("DIGITE SOMENTE NÚMEROS")
            continue
        try:
            valor_passagem=float(input("DIGITE O VALOR DA PASSAGEM:"))
        except:
            print("DIGITE SOMENTE NÚMEROS")
            continue
        desconto=valor_passagem*0.95
        print("O valor da passagem com desconto de 5% é R$ ",desconto)
        passagem.append({
        "destino":destino,
        "origem":origem,
        "duração":duracao,
        "valor Passagem":valor_passagem,
        "desconto":desconto
         })
    elif opcao==3:
        print("\nCADASTRO AVIÃO")
        modelo=input("DIGITE O MODELO DO AVIÃO: ")
        ano=int(input("DIGITE O ANO DE FABRICAÇÃO DO AVIÃO: "))
        try:
           hora_voo=int(input("DIGITE O TEMPO DE VÔO DA AERONAVE(HORAS): "))
        except:
           print("DIGITE SOMENTE NÚMEROS")
        cor=input("DIGITE A COR DA AERONAVE: ")
        if cor.isdigit():
            print("COR INVÁLIDA! NÃO DIGITE NÚMEROS.")
        else:
            break
        try:
           quant_passageiro=int(input("DIGITE A QUANTIDADE DE PASSAGEIROS: "))
        except:
           print("DIGITE SOMENTE NÚMEROS")
           continue
        aviao.append({
        "modelo":modelo,
        "ano":ano,
        "hora_voo":hora_voo,
        "cor":cor,
        "quant_passageiro":quant_passageiro
        })
    elif opcao==4:
     print("\nCADASTRO DA TRIPULAÇÃO")
    tripulacao_atual = {}
    while True:
        print("\n--- CARGO EXERCICIDO ---")
        print("1 - PILOTO COMANDANTE")
        print("2 - COPILOTO")
        print("3 - COMISSÁRIO 1")
        print("4 - COMISSÁRIO 2")
        print("5 - COMISSÁRIO 3")
        print("0 - VOLTAR AO MENU PRINCIPAL")

        try:
            cargo=int(input("ESCOLHA O CARGO PARA CADASTRAR: "))
        except ValueError:
            print("DIGITE UMA OPÇÃO VÁLIDA!")
            continue
        if cargo==0:
            break
        nome=input("DIGITE O NOME DA PESSOA: ")
        if nome.isdigit():
            print("NOME INVÁLIDO! NÃO USE NÚMEROS.")
            continue

        if cargo==1:
            tripulacao_atual["piloto_comandante"] = nome
        elif cargo==2:
            tripulacao_atual["copiloto"] = nome
        elif cargo==3:
            tripulacao_atual["comissario1"] = nome
        elif cargo==4:
            tripulacao_atual["comissario2"] = nome
        elif cargo==5:
            tripulacao_atual["comissario3"] = nome
        else:
            print("OPÇÃO INVÁLIDA!")

    if tripulacao_atual:
        tripulacao.append(tripulacao_atual)
        print("TRIPULAÇÃO CADASTRADA COM SUCESSO!")
    else:
        print("NENHUM DADO DE TRIPULAÇÃO FOI CADASTRADO.")
        #print("\nCADASTRO DA TRIPULAÇÃO")
        #cad_tripulacao1=input("DIGITE O NOME DO PILOTO COMANDANTE: ")
        #if nome_trupu.isdigit():
        #    print("NOME INVÁLIDO! NÃO DIGITE NÚMEROS.")
        #else:
         #   break
        #copiloto=input("DIGITE O NOME DO COPILOTO: ")
        #if copiloto.isdigit():
         #   print("NOME INVÁLIDO! NÃO DIGITE NÚMEROS.")
        #else:
         #  break
        #comissario1=input("DIGITE O NOME DO PRIMEIRO COMISSÁRIO: ")
        #if comissario1.isdigit():
         #   print("NOME INVÁLIDO! NÃO DIGITE NÚMEROS.")
        #else:
         #   break
        #comissario2=input("DIGITE O NOME DO SEGUNDO COMISSÁRIO: ")
        #if comissario2.isdigit():
         #   print("NOME INVÁLIDO! NÃO DIGITE NÚMEROS.")
        #else:
         #   break
        #comissario3=input("DIGITE O NOME DO TERCEIRO COMISSÁRIO: ")
        #if comissario3.isdigit():
         #   print("NOME INVÁLIDO! NÃO DIGITE NÚMEROS.")
        #else:
         #   break