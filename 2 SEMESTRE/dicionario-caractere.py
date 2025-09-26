###### DICIONÁRIO
tradutor={}
tradutor["pineapple"]="abacaxi"
tradutor["apple"]="maçã"
tradutor["orange"]="laranja"
print(type(tradutor))
print(tradutor)

### PODE SER ESCRITA NA MESMA LINHA OU UM ABAIXO DO OUTRO ####
tradutor={}
tradutor={"pineapple":"abacaxi","apple":"maçã","orange":"laranja"} # USA-SE CHAVE {}
print(type(tradutor))
print(tradutor)

######### FAZER PESQUISA POR CHAVE #####
tradutor={}
tradutor={"pineapple":"abacaxi","apple":"maçã","orange":"laranja"} 
print(type(tradutor))
print(tradutor["apple"])

###### DELETAR ITEM #######
tradutor={}
tradutor={"pineapple":"abacaxi","apple":"maçã","orange":"laranja"} 
print(tradutor)
del (tradutor ["apple"])
print(tradutor)

##### POP #####
tradutor={}
tradutor = {"pineapple": "abacaxi", "apple": "maçã", "orange": "laranja"} 
print(tradutor.pop("apple"))  # Remove a chave "apple" e imprime seu valor
print(tradutor)   

#####  CLEAN  ####### remover todos os itens, ou seja, ele esvazia o dicionário.
dados = {
    "nome": "Ana","idade": 25,"cidade": "Rio de Janeiro"}

print("Antes de limpar:", dados)
dados.clear() # Limpando o dicionário
print("Depois de limpar:", dados)

#### COMANDO IN ######## busca se é verdadeiro ou falso
tradutor={}
tradutor={"pineapple":"abacaxi","apple":"maçã","orange":"laranja"} 
print("apple" in tradutor)

###### VALUES ##### IMPRIME OS VALORES DO DICIONÁRIO
tradutor={}
tradutor={"pineapple":"abacaxi","apple":"maçã","orange":"laranja"} 
print("apple" in tradutor)

###### EDITANDO VALOR DA CHAVE #######
tradutor={}
tradutor={"pineapple":"abacaxi","apple":"maçã","orange":"laranja"} # USA-SE CHAVE {}
print(tradutor)
tradutor=["apple"]="goiaba"
print(tradutor)

###### DICIONÁRIO DE DICIONÁRIO #####
aluno = {
    "nome": "João","idade": 17,"notas": {                    ##### um dicionário foi incluido dentro de uma chave
        "matematica": 8.5,
        "portugues": 7.0,
        "historia": 9.2
    }
}
print("Nota de Matemática:", aluno["notas"]["matematica"]) # Acessando uma nota específica

####### GET ###########
aluno = {
    "nome": "João","idade": 17,"notas": {                    ##### um dicionário foi incluido dentro de uma chave
        "matematica": 8.5,
        "portugues": 7.0,
        "historia": 9.2
    }
}
print(aluno.get ("fisica", "materia não encontrada"))

########## Tratamento de excessão ####################
# Try- testa o bloco/erro
# Except- Trata o erro
# Else- não deu erro
# Finally- 

a=int(input("Digite um texto: ")) # int só pode ser usado com números

##### Try e except ######
try:
 a=int(input("Digite um texto: "))
except:
 print("Digite somente números ")

##### MULTIPLAS EXECUÇÕES ######
try:
 a=int(input("Digite um texto: "))
except ValueError:
 print("Digite somente números")
except:
 print("Erro desconhecido")

 ##### FINALLY  ########## executa mesmo com erro
try:
 a=int(input("Digite um texto: "))
except ValueError:
 print("Digite somente números")
except:
 print("Erro desconhecido")
finally:
 print("Final do algoritmo")

 # 26/05
 ############ OPEN ########################
 #    r=leitura
 f=open("file.txt", "r") # r- Abre um arquivopara leitura, o arquivo deve estar dentro da pasta
 
 # a-Acrescentar, abre um arquivo para anexar, cria o arquivo se ele não existir
 z=open("file.txt","a")
z.write(", E NUNCA TERÁ.") # TEXTO A SER INCORPORADO
z=open("file.txt", "r")
print(z.read())
z.close()
######################################
z=open("file.txt","a")
x=input("DIGITE SEU NOME=- ")
z.write(x) # TEXTO A SER INCORPORADO
z=open("file.txt", "r")
print(z.read())
z.close()

####################### "encoding="utf-8" ########################
z=open("file.txt","a",encoding="utf-8" )
z.write(", E NUNCA TERÁ.") # TEXTO A SER INCORPORADO
z=open("file.txt", "r")
print(z.read())
z.close()

#### W- Cria um arquivo ou subscreve o conteudo #####
f=open("file.txt","w")

###### x-Cria o arquivo , se ele existir ocorre ERRO #########
f=open("file.txt","x")

###### rt ######
f=open("aaa.jpg","rt")
print(f.read())

########### WITH OPEN ##########
with open("cadastro.txt","a")as x:
    x.write("NovoCadastro\n")

###### READLINE ######
with open("cadastro.txt","r") as f:
 linhas=f.readlines()
 print(linhas[2]) # LINHA A SER PRINTADA

####### WITH OPEN -BUSCAS ########
with open("cadastro.txt","r") as f:
 for linha in f:
  if "joão" in linha.lower(): # BUSCA PELA PALAVRA JOÃO
   print(linha)

##### DELETAR LINHA-WITH OPEN ###########
with open("cadastro.txt","r") as f:
 linhas=f.readlines()
 # REMOVE A LINHA 2(TERCEIRA LINHA)
 print(linhas[2])
 del linhas [2]
 with open("cadastro.txt","w") as f:
  f.writelines(linhas)

