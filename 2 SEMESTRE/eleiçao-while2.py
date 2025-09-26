cand1=0
cand2=0
cand3=0
nulo=0
branco=0

total_eleitores=int(input("Digite o total de eleitores: "))
contador=1

while contador<=total_eleitores:
    print(f"\nEleitor {contador}:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Voto nulo")
    print("Pressione apenas Enter para votar em branco")
    print("0 - Encerrar votação antecipadamente")
    voto = input("Digite o número do seu candidato: ")
    if voto=="":
        branco+=1
    elif voto=="0":
        print("Votação encerrada.")
        break
    elif voto=="1":
        cand1 +=1
    elif voto=="2":
        cand2+=1
    elif voto=="3":
        cand3+=1
    elif voto=="4":
        nulo+=1
    else:
        print("Voto inválido!")
    contador+=1
print("\nResultado da eleição:")
print("Candidato 1:", cand1, "voto(s)")
print("Candidato 2:", cand2, "voto(s)")
print("Candidato 3:", cand3, "voto(s)")
print("Votos nulos:", nulo)
print("Votos em branco:", branco)
if cand1>cand2 and cand1>cand3:
    print("Candidato 1 venceu")
elif cand1<cand2 and cand2>cand3:
    print("Candidato 2 venceu")
if cand3>cand1 and cand3>cand2:
    print("Candidato 3 venceu")
else:
    print("Haverá segundo turno entre o primeiro e o segundo candidato" )