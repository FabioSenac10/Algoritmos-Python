import os

# ----------------- Listas globais -----------------
clientes = []
veiculos = []
ordens_servico = []

# ----------------- Funcoes de inicializacao -----------------
def verificar_existencia(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w') as f:
            pass

def carregar_dados():
    arquivos = ['clientes.txt', 'veiculos.txt', 'ordens_servico.txt']
    for arquivo in arquivos:
        verificar_existencia(arquivo)

    clientes.clear()
    veiculos.clear()
    ordens_servico.clear()

    with open('clientes.txt', 'r') as f:
        for linha in f:
            clientes.append(linha.strip().split(';'))
    with open('veiculos.txt', 'r') as f:
        for linha in f:
            veiculos.append(linha.strip().split(';'))
    with open('ordens_servico.txt', 'r') as f:
        for linha in f:
            ordens_servico.append(linha.strip().split(';'))

def salvar_dados():
    with open('clientes.txt', 'w') as f:
        for c in clientes:
            f.write(';'.join(c) + '\n')
    with open('veiculos.txt', 'w') as f:
        for v in veiculos:
            f.write(';'.join(v) + '\n')
    with open('ordens_servico.txt', 'w') as f:
        for o in ordens_servico:
            f.write(';'.join(o) + '\n')

# ----------------- Funcoes de busca -----------------
def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente[0] == cpf:
            return cliente
    return None

def buscar_veiculo_por_placa(placa):
    for veiculo in veiculos:
        if veiculo[0] == placa:
            return veiculo
    return None

def buscar_os_por_numero(numero_os):
    for os in ordens_servico:
        if os[0] == numero_os:
            return os
    return None

# ----------------- Validacoes -----------------
def entrada_numerica(msg, tipo=int, minimo=None, maximo=None):
    while True:
        valor = input(msg)
        try:
            valor_convertido = tipo(valor)
            if minimo is not None and valor_convertido < minimo:
                print(f"Valor deve ser maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor_convertido > maximo:
                print(f"Valor deve ser menor ou igual a {maximo}.")
                continue
            return valor_convertido
        except ValueError:
            print("❌ Entrada inválida. Tente novamente.")

# ----------------- Cadastro -----------------
def cadastrar_cliente():
    cpf = input("CPF (somente números): ")
    if not cpf.isdigit():
        print("❌ CPF inválido.")
        return
    if buscar_cliente_por_cpf(cpf):
        print("⚠️ CPF já cadastrado.")
        return
    nome = input("Nome completo: ")
    telefone = input("Telefone (somente números): ")
    if not telefone.isdigit():
        print("❌ Telefone inválido.")
        return
    clientes.append([cpf, nome, telefone])
    salvar_dados()
    print("✅ Cliente cadastrado com sucesso.")

def cadastrar_veiculo():
    placa = input("Placa: ")
    if buscar_veiculo_por_placa(placa):
        print("⚠️ Placa já cadastrada.")
        return
    modelo = input("Modelo: ")
    ano = entrada_numerica("Ano: ", int, 1900, 2100)
    cpf = input("CPF do proprietário: ")
    if not cpf.isdigit():
        print("❌ CPF inválido.")
        return
    if not buscar_cliente_por_cpf(cpf):
        print("❌ Cliente não encontrado.")
        return
    veiculos.append([placa, modelo, str(ano), cpf])
    salvar_dados()
    print("✅ Veículo cadastrado com sucesso.")

def cadastrar_ordem_servico():
    numero_os = input("Número da OS: ")
    if buscar_os_por_numero(numero_os):
        print("⚠️ Número da OS já existe.")
        return
    descricao = input("Descrição do serviço: ")
    valor = entrada_numerica("Valor: ", float, 0)
    cpf = input("CPF do cliente: ")
    if not cpf.isdigit():
        print("❌ CPF inválido.")
        return
    placa = input("Placa do veículo: ")
    if not buscar_cliente_por_cpf(cpf):
        print("❌ Cliente não encontrado.")
        return
    if not buscar_veiculo_por_placa(placa):
        print("❌ Veículo não encontrado.")
        return
    ordens_servico.append([numero_os, descricao, f"{valor:.2f}", cpf, placa])
    salvar_dados()
    print("✅ Ordem de serviço cadastrada com sucesso.")

# ----------------- Consulta -----------------
def listar_clientes():
    print("\n📋 Lista de Clientes:")
    for c in clientes:
        print(f"CPF: {c[0]} | Nome: {c[1]} | Telefone: {c[2]}")

def listar_veiculos():
    print("\n🚗 Lista de Veículos:")
    for v in veiculos:
        print(f"Placa: {v[0]} | Modelo: {v[1]} | Ano: {v[2]} | CPF: {v[3]}")

def listar_ordens_servico():
    print("\n🧾 Lista de Ordens de Serviço:")
    for o in ordens_servico:
        print(f"Nº: {o[0]} | Desc: {o[1]} | Valor: {o[2]} | CPF: {o[3]} | Placa: {o[4]}")

def consultar_veiculos_por_cpf():
    cpf = input("Digite o CPF do cliente: ")
    encontrados = [v for v in veiculos if v[3] == cpf]
    if encontrados:
        for v in encontrados:
            print(f"Placa: {v[0]} | Modelo: {v[1]} | Ano: {v[2]}")
    else:
        print("❌ Nenhum veículo encontrado.")

def consultar_os():
    opcao = input("Consultar por (1) CPF ou (2) Número da OS: ")
    if opcao == '1':
        cpf = input("Digite o CPF: ")
        encontrados = [o for o in ordens_servico if o[3] == cpf]
    else:
        numero_os = input("Digite o número da OS: ")
        encontrados = [o for o in ordens_servico if o[0] == numero_os]
    if encontrados:
        for o in encontrados:
            print(f"Nº: {o[0]} | Desc: {o[1]} | Valor: {o[2]} | CPF: {o[3]} | Placa: {o[4]}")
    else:
        print("❌ Nenhuma ordem encontrada.")

# ----------------- Edicao -----------------
def editar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf)
    if not cliente:
        print("❌ Cliente não encontrado.")
        return
    novo_nome = input("Novo nome: ")
    novo_telefone = input("Novo telefone (somente números): ")
    if not novo_telefone.isdigit():
        print("❌ Telefone inválido.")
        return
    cliente[1], cliente[2] = novo_nome, novo_telefone
    salvar_dados()
    print("✅ Cliente atualizado.")

def editar_veiculo():
    placa = input("Digite a placa do veículo: ")
    veiculo = buscar_veiculo_por_placa(placa)
    if not veiculo:
        print("❌ Veículo não encontrado.")
        return
    novo_modelo = input("Novo modelo: ")
    novo_ano = entrada_numerica("Novo ano: ", int, 1900, 2100)
    veiculo[1], veiculo[2] = novo_modelo, str(novo_ano)
    salvar_dados()
    print("✅ Veículo atualizado.")

def editar_ordem_servico():
    numero_os = input("Digite o número da OS: ")
    os = buscar_os_por_numero(numero_os)
    if not os:
        print("❌ Ordem não encontrada.")
        return
    nova_desc = input("Nova descrição: ")
    novo_valor = entrada_numerica("Novo valor: ", float, 0)
    os[1], os[2] = nova_desc, f"{novo_valor:.2f}"
    salvar_dados()
    print("✅ Ordem de serviço atualizada.")

# ----------------- Exclusao -----------------
def excluir_cliente():
    cpf = input("Digite o CPF do cliente: ")
    global clientes, veiculos, ordens_servico
    if not buscar_cliente_por_cpf(cpf):
        print("❌ Cliente não encontrado.")
        return
    clientes = [c for c in clientes if c[0] != cpf]
    veiculos = [v for v in veiculos if v[3] != cpf]
    ordens_servico = [o for o in ordens_servico if o[3] != cpf]
    salvar_dados()
    print("✅ Cliente e dados relacionados excluídos.")

def excluir_veiculo():
    placa = input("Digite a placa do veículo: ")
    if not buscar_veiculo_por_placa(placa):
        print("❌ Veículo não encontrado.")
        return
    global veiculos
    veiculos = [v for v in veiculos if v[0] != placa]
    ordens_servico[:] = [o for o in ordens_servico if o[4] != placa]
    salvar_dados()
    print("✅ Veículo excluído.")

def excluir_ordem_servico():
    numero_os = input("Digite o número da OS: ")
    if not buscar_os_por_numero(numero_os):
        print("❌ Ordem não encontrada.")
        return
    global ordens_servico
    ordens_servico = [o for o in ordens_servico if o[0] != numero_os]
    salvar_dados()
    print("✅ Ordem de serviço excluída.")

# ----------------- Menu principal -----------------
def menu():
    carregar_dados()
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar cliente")
        print("2. Cadastrar veículo")
        print("3. Cadastrar ordem de serviço")
        print("4. Listar clientes")
        print("5. Listar veículos")
        print("6. Listar ordens de serviço")
        print("7. Consultar veículos por CPF")
        print("8. Consultar ordens de serviço")
        print("9. Editar cliente")
        print("10. Editar veículo")
        print("11. Editar ordem de serviço")
        print("12. Excluir cliente")
        print("13. Excluir veículo")
        print("14. Excluir ordem de serviço")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1': cadastrar_cliente()
            elif opcao == '2': cadastrar_veiculo()
            elif opcao == '3': cadastrar_ordem_servico()
            elif opcao == '4': listar_clientes()
            elif opcao == '5': listar_veiculos()
            elif opcao == '6': listar_ordens_servico()
            elif opcao == '7': consultar_veiculos_por_cpf()
            elif opcao == '8': consultar_os()
            elif opcao == '9': editar_cliente()
            elif opcao == '10': editar_veiculo()
            elif opcao == '11': editar_ordem_servico()
            elif opcao == '12': excluir_cliente()
            elif opcao == '13': excluir_veiculo()
            elif opcao == '14': excluir_ordem_servico()
            elif opcao == '0': break
            else: print("❌ Opção inválida.")
        except Exception as e:
            print("⚠️ Erro inesperado:", e)

# Executa o menu
menu()
