num_pessoas=int(input("Digite a quantidade de pesoas: "))
somaidade=0
pessoas=[]
for i in range(num_pessoas):
    idade=int(input(f"Digite a idade {i+1}:"))
    somaidade+=idade
    media=somaidade/num_pessoas
    print("A média é  ",media)

if media<=25:
    print("A turma é jovem")
elif media<=60:
    print("A turma é adulta")
else:
    print("A turma é idosa")
       