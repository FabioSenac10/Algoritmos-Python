############### FOR ##################
frutas=["banana", "laranja", "pera"]
for i in frutas: 
    print(i)

############## BREAK ######################
nomes=["Félix", "Evandro", "Jeandro"]
for n in nomes:
    print(n)
    if (n)=="Jeandro":    
     break

############# CONTINUE ########
nomes=["Félix", "Evandro", "Jeandro"]
for n in nomes:
    if (n)=="Jeandro":    
     continue
    print(n)

################## RANGE ##########
for x in range(6):
   print(x)

####################################
for x in range(1,6): # Imprime do 1 ao 5
   print(x)

#####################################
for x in range(2,10,2): # Imprime do 1 ao 10, mas pula de 2 em 2
  print(x)

#####################################
for x in range(100,1,-1): # Imprime do 100 ao 1, mas em ordem decrescente
  print(x)

################### FOR ANINHADO- TABUADA ######################## FOR dentro do FOR
for i in range(1,11):
   for j in range (1,11):
      print(i,"x",j,"=", i*j)
      print("---------------------")

############### FOR 1-50 IMPARES ##################
for i in range (1,50,2):
    print(i)

######### NÚMERAR TIMES #################################
times=["São Paulo", "Fortaleza", "Operário"]
cont=0
for i in times:
  cont += 1
  print(cont, "-",i)

############# Imprimir os números no intervalo de dois números ######################
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
cont = 0
for numero in range(n1 + 1, n2):
    print(numero)
    cont += numero
print("Soma total:", cont)

###################################################
for numero in range(1,21):
   print(numero)

################################################
for numero in range(1,21):
    print(numero, end=" ")


