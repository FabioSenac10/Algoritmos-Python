def filtrar_nomes_digitados():
    lista = input("DIGITE OS NOMES SEPARADOS POR VIRGULA: ")
    return [nome.strip() for nome in lista.split(",") if len(nome.strip()) > 5]

print(filtrar_nomes_digitados())
