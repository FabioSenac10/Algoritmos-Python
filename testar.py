def salvar_em_arquivo():
    with open("cadastro.txt", "w", encoding='utf-8') as arquivo:
        for pessoa in cadastro:
            linha = f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo:{pessoa['sexo']}, "
            linha += f"Endereço: {pessoa['endereco']}, Cidade: {pessoa['cidade']}, Estado: {pessoa['estado']}\n"
            linha += "-" * 90 + "\n"
            arquivo.write(linha)
    print("Dados salvos no arquivo 'cadastro.txt'.")

def consultar_dados():
    if not cadastro:
        print("Nenhum cadastro disponível.")
        return

    print("\nCampos disponíveis para consulta: nome, idade, sexo, cpf, endereco, cidade, estado")
    campo = input("Qual campo deseja consultar? ").strip().lower()

    if campo not in ['nome', 'idade', 'sexo', 'cpf', 'endereco', 'cidade', 'estado']:
        print("Campo inválido.")
        return

    for idx, pessoa in enumerate(cadastro, 1):
        print(f"{idx}. {pessoa[campo]}")
    print()

# Lista principal de cadastros
cadastro = []

# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        cadastrar_pessoa()
    elif opcao == '2':
        consultar_dados()
    elif opcao == '3':
        salvar_em_arquivo()
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
