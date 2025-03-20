#fr
# len=Conta caractres na string
a="fabio"
print(len(a))

# Capitalize=Aumenta o tamanho primeira letra
a="fabio"
print(a.capitalize())

# upper=aumenta o texto
a="fabio"
print(a.upper())

# casefold=diminui o texto
a="FABIO"
print(a.casefold())

# islower=identifica se o texto é minusculo. Se é FALSO ou VERDADEIRO
a="FABIO"
print(a.islower())

# ISDIGIT= Verifica se possui somente números inteiros
a="123456"
print(a.isdigit())

# Função Replace= troca todas as ocorrencias de uma string por outra em uma mesma string
a="Fabio Camargo"
print(a.replace("Camargo","Soares"))
      
###########################################
a="Fabio-Soares-Camargo"
print(a.split("-"))

# find=localiza onde começa a palvra pesquisada
a="Fabio Soares Camargo"
print(a.find("Camargo"))

# Função in=verifica se uma substring é parte de outra string
a="Fabio Soares Camargo"
print("Camargo"in a)

# count= conta a quantidade de frequencia da palavra ou letra pesquisada
a="Fabio Soares Camargo"
print(a.count("a"))

# Mostra a posição da pesquisa feita
s="Olá, mundo!"
print(s[0])
print(s[2])
print(s[6])

# Printa a posição do elemento. Não imprime a ultima posição, sempra -1 posição
s="Olá, mundo!"
print(s[1:3]) #lá

# marca até onde quer
s="Olá, mundo!"
print(s[:3]) #Conta 0,1,2

# string=(" olá mundo")
# lista=["abc", 123, @]

lista1=[10, 120, 30]
lista2=["span", "bunger", "swallow"]
print(lista1, lista2)

#
frutas= ["banana, laranja, morango"]
print([1, 2]+[3,4])
print(frutas+[6,7,8])

# max= maior valor
# min= menor valor
# sum= soma todos os valores
a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a))

# Fatia a lista
# a=0 b=2 c=3 d=4 f=5
uma_lista=["a", "b", "c", "d", "f"]
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])

# Litas Mutáveis- Alteração de lista
frutas= ["banana","maçã", "cereija"]
frutas[0]= "pera"
frutas[-1]= "laranja"
print(frutas)

# Mutação de lista
uma_lista=["a","b","c","d","e","f"]
uma_lista[1:3]=["x","y"]
print(uma_lista)

# Lista Mutáveis- Inserir elemento na lista
uma_lista=["a","d","f"]
uma_lista[1:1]=["b","c"]#posição onde será adicionada
print(uma_lista)
uma_lista[4:4]=["e"]
print(uma_lista)

# deletando elemento de uma lista
a=["um", "dois", "três"]
del a[1]
print(a)
lista=["a","b","c","d","e","f"]
del lista[1:5]
print(lista)