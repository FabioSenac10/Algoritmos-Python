# RANGE (INTERVALO)
# RANGE (Inicio, fim,  passo o valor colocado no final (1,9,2)) pula de 2 em 2.
for i in range (1,10):
    print(i)
####################################################
# ITERADOR
i = 0
while i < 10:  # Agora o loop roda ao menos uma vez
    print(i)
    i = i + 1
print("Fim do loop")  # Corrigido com parênteses
########################################################
lista=[10,20,30,40,55,66,77,88,99]
x=0
while x<len(lista):
    print(x, lista[x])
    x+=1
##########################################################
# For para percorrer  listas
lista=["MBA", "NBA", "CPF", "USP", "BAUM", "LULA", "BOZO"]
for x in lista:
    print(x)
###########################################################
#CONVERTER DECIMAL PARA BINÁRIO-CALCULADORA DE DECIMAL PARA BINÁRIO
import os
valor=float(input("Digite um valor em decimal para converter para binário: "))
valor_binario=[]

while valor>0:
    novovalor=valor%2
    novovalor=int(novovalor)
    print("Resto: ", novovalor)

    valor=valor/2
    print("Dividendo: ", valor)
    valor=int(valor)
    valor_binario.insert(0, novovalor)
    print("Número binário final:", ''.join(map(str, valor_binario))) #map=Interador, *join junta tudo sem virgula
    print(valor_binario)
    print(valor)

#########################################################
valor=input("Digite um número em binário: ")
valor_decimal=[]

x=len(valor)
for i in valor:
    x=x-1
    if i=="1":
        z=2**x
        valor_decimal.append(z)
        print(valor_decimal)
        print("Decimal: ", sun(valor_decimal) ) # SUN= SOMA

