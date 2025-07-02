def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos
lista = input("Digite os elementos da lista separados por vírgula: ").split(",")
print("Elementos únicos:", elementos_unicos(lista))