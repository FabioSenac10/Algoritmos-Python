cand1=0
cand2=0
cand3=0
nulo=0
branco=0
total_eleitores=int(input("Digite o total de eleitores: "))
contador=1
for i in range(total_eleitores):
    print(f"\nEleitor {contador}:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Voto nulo")
    print("5 - Voto em branco")
    print("0 - Encerrar votação antecipadamente")
    voto=int(input("Digite o número do seu candidato: "))
    if voto==1:
        cand1+=1
    elif voto==2:
        cand2+=1
    elif voto==3:
        cand3+=1
    elif voto==4:
        nulo+=1
    elif voto==5:
        branco+=1
    elif voto==0:
        print("Votação encerrada.")
        break
    else:
        print("Voto inválido!")
    contador += 1
print("\nResultado da eleição:")
print("Candidato 1:", cand1, "voto")
print("Candidato 2:", cand2, "voto")
print("Candidato 3:", cand3, "voto")
print("Votos nulos:", nulo)
print("Votos em branco:", branco)
if cand1>cand2 and cand1>cand3:
    print("Candidato 1 foi o campeão.")
elif cand2>cand1 and cand2>cand3:
    print("Candidato 2 foi o campeão.")
elif cand3>cand2 and cand3>cand1:
    print("Candidato 3 foi o campeão.")
elif cand1==cand2:
    print("Houve empate entre o candidato 1 e o candidato .")
elif cand1==cand3:
    print("Houve empate entre o candidato 1 e o candidato 2.")
else:
