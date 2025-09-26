cand1=0
cand2=0
cand3=0
cand4=0
nulo=0
branco=0

total_eleitores=int(input("Digite o total de eleitores: "))
contador=1

while contador<=total_eleitores:
    print(f"\nEleitor {contador}:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Candidato 4")
    print("5 - Voto nulo")
    print("6 - Voto em branco")
    print("0 - Encerrar votação antecipadamente")
    
    voto=int(input("Digite o número do seu candidato: "))

    if voto==1:
        cand1+=1
    elif voto==2:
        cand2+=1
    elif voto==3:
        cand3+=1
    elif voto==4:
        cand4+=1
    elif voto==5:
        nulo+=1
    elif voto==6:
        branco+=1
    elif voto==0:
        print("Votação encerrada.")
        break
    else:
        print("Voto inválido!")
    
    contador += 1

# Exibe o resultado da votação
print("\nResultado da eleição:")
print("Candidato 1:", cand1, "voto")
print("Candidato 2:", cand2, "voto")
print("Candidato 3:", cand3, "voto")
print("Candidato 4:", cand4, "voto")
print("Votos nulos:", nulo)
print("Votos em branco:", branco)
