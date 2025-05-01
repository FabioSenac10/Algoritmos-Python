popA = 80000
taxaA = 3.0

popB = 200000
taxaB = 1.5

ano = 0
while popA < popB:
    ano += 1
    popA = int((1 + (taxaA / 100)) * popA)
    popB = int((1 + (taxaB / 100)) * popB)

print("População do país A:", popA)
print("População do país B:", popB)
print("Número de anos necessários:", ano)
