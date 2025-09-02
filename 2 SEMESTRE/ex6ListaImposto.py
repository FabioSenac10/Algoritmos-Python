def tabela_precos():
    preco_unitario=1.99
    for quantidade in range(1, 51):
        valor_total=quantidade * preco_unitario
        print(f"{quantidade:2d} - R$ {valor_total:6.2f}")
tabela_precos()
