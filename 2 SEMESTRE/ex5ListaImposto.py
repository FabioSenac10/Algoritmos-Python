def SomaIposto(taxaImposto,custo):
    imposto=custo*(taxaImposto/100)
    Valor_novo=custo+imposto
    return Valor_novo

taxa= float(input("Digite a taxa de juros (%): "))
custo=float(input("Digite o custo do produto(R$): "))

valor_final=SomaIposto(taxa,custo)
print(f"O valor final do produto com imposto é: R$ {valor_final:.2f}")