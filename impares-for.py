maior = 0
menor = 0
soma = 0

for i in range(3):
    num = int(input(f"Digite o {i + 1}º número: "))
    soma += num
    if i == 0:
        maior = menor = num  # Inicializa na primeira iteração
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"A soma dos números é: {soma}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
