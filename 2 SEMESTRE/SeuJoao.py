import datetime
clientes = []
produtos = []
vendedores = []
vendas = []

while True:
    print("\n======================= MENU DE OPÇÕES =======================")
    print("1 - CADASTRO DE CLIENTE")
    print("2 - CADASTRO DE PRODUTO")
    print("3 - CADASTRO DE VENDEDOR")
    print("4 - REGISTRAR VENDA")
    print("5 - EXIBIR RELATÓRIO DE VENDAS")
    print("0 - SAIR")

    try:
        opcao = int(input("DIGITE SUA OPÇÃO: "))
    except ValueError:
        print("DIGITE UMA OPÇÃO VÁLIDA! Por favor, insira um número.")
        continue

    if opcao == 0:
        print("SAIR")
        break

    elif opcao == 1:
        print("\nCADASTRO DE CLIENTE")
        while True:
            nome = input("DIGITE O NOME DO CLIENTE: ")
            if nome.replace(" ", "").isalpha():
                break
            else:
                print("NOME INVÁLIDO! Por favor, digite apenas letras.")
        
        while True:
            cpf = input("DIGITE O CPF (SOMENTE NÚMEROS): ")
            if cpf.isdigit() and len(cpf) == 11:
                break
            else:
                print("CPF INVÁLIDO. O CPF deve conter 11 dígitos numéricos.")

        endereco = input("DIGITE O ENDEREÇO COMPLETO: ")
        
        while True:
            fone = input("DIGITE O TELEFONE COM DDD (SOMENTE NÚMEROS): ")
            if fone.isdigit():
                break
            else:
                print("DIGITE SOMENTE NÚMEROS.")

        clientes.append({
            "nome": nome,
            "cpf": cpf,
            "endereco": endereco,
            "fone": fone
        })
        print("\nCLIENTE CADASTRADO COM SUCESSO!")

    elif opcao == 2:
        print("\nCADASTRO DE PRODUTO")
        while True:
            nome = input("DIGITE O NOME DO PRODUTO: ")
            if nome:
                break
            else:
                print("NOME INVÁLIDO! O nome não pode ser vazio.")

        while True:
            codigo = input("CÓDIGO DO PRODUTO (SOMENTE NÚMEROS): ")
            if codigo.isdigit():
                break
            else:
                print("DIGITE SOMENTE NÚMEROS.")
        
        while True:
            categoria = input("DIGITE A CATEGORIA DO PRODUTO (ELÉTRICA, HIDRÁULICA, ACABAMENTO, FERRAGEM, REVESTIMENTO): ")
            if categoria.replace(" ", "").isalpha():
                break
            else:
                print("CATEGORIA INVÁLIDA! Digite apenas letras.")
        
        unidade_medida = input("DIGITE A UNIDADE DE MEDIDA (KG, M², M³, QUANTIDADE, LITROS, MILHEIRO): ")
        
        while True:
            try:
                preco_custo = float(input("PREÇO DE CUSTO: "))
                break
            except ValueError:
                print("VALOR INVÁLIDO. Digite somente números.")
        
        while True:
            try:
                preco_venda = float(input("PREÇO DE VENDA: "))
                break
            except ValueError:
                print("VALOR INVÁLIDO. Digite somente números.")
        
        while True:
            try:
                estoque = int(input("QUANTIDADE EM ESTOQUE: "))
                break
            except ValueError:
                print("QUANTIDADE INVÁLIDA. Digite somente números inteiros.")

        while True:
            try:
                minimo = int(input("ESTOQUE MÍNIMO: "))
                break
            except ValueError:
                print("VALOR INVÁLIDO. Digite somente números inteiros.")
        
        promocao = None
        if input("TEM PROMOÇÃO? (S/N): ").strip().upper() == 'S':
            while True:
                try:
                    desc = float(input("DESCONTO (%) NA PROMOÇÃO: "))
                    break
                except ValueError:
                    print("DIGITE UM VALOR VÁLIDO.")
            
            while True:
                data_str = input("DATA DE VALIDADE (YYYY-MM-DD): ")
                try:
                    validade = datetime.datetime.strptime(data_str, '%Y-%m-%d').date()
                    break
                except ValueError:
                    print("FORMATO INVÁLIDO. Use o formato YYYY-MM-DD.")
            
            promocao = {"desconto": desc, "validade": validade}
        
        produtos.append({
            "nome": nome,
            "codigo": codigo,
            "categoria": categoria,
            "unidade_medida": unidade_medida,
            "preco_custo": preco_custo,
            "preco_venda": preco_venda,
            "estoque": estoque,
            "minimo": minimo,
            "promocao": promocao
        })
        print("\nPRODUTO CADASTRADO COM SUCESSO.")

    elif opcao == 3:
        print("\nCADASTRO DE VENDEDOR")
        while True:
            nome = input("DIGITE O NOME DO VENDEDOR: ")
            if nome.replace(" ", "").isalpha():
                break
            else:
                print("NOME INVÁLIDO! Digite apenas letras.")

        while True:
            cpf_vendedor = input("DIGITE O CPF DO VENDEDOR (SOMENTE NÚMEROS): ")
            if cpf_vendedor.isdigit() and len(cpf_vendedor) == 11:
                break
            else:
                print("CPF INVÁLIDO. O CPF deve conter 11 dígitos numéricos.")
        
        while True:
            try:
                comissao = float(input("DIGITE O VALOR DA COMISSÃO (Ex: 5 para 5%): "))
                break
            except ValueError:
                print("VALOR INVÁLIDO. Digite somente números.")

        vendedores.append({
            "nome": nome,
            "cpf_vendedor": cpf_vendedor,
            "comissao": comissao
        })
        print("VENDEDOR CADASTRADO COM SUCESSO.")

    elif opcao == 4: