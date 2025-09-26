############# FUNÇÃO #################
def hello():
 print("Olá")
hello()
# def: Palavra-chave que indica a definição de uma função.
# nome_da_funcao: Nome descritivo que indica o que a função faz.
# parametros: Valores que a função recebe para processar (opcional).
# return: Palavra-chave que indica o valor que a função devolve após sua execução (opcional).

##### Parametros/Variaveis
def hello(nome):
 print("Olá", nome) # NOME é o parametro
hello("Fabio")

############# PARAMETROS ##############
def hello(nome):
 print("Seja bem-vindo", nome) # NOME é o parametro
a=input("DIGITE SEU NOME: ")
hello(a) 
#############################################
def hello(nome, idade):# NOME e idade são parametros
 print("Olá", nome, "\nSua idade é: ", idade ) 
hello("Fabio", 30) # Fabio e 30 são argumentos

################ FUNÇÃO DE SAÍDA ##############
def calcular_pgto(qud_horas, valor_horas):
    horas=float(qud_horas)
    taxa=float(valor_horas)
    if horas <= 40:
      salario = horas * taxa
    else:
      horas_excendentes= horas - 40
      salario = (40 * taxa) + (horas_excendentes * taxa * 1.5)
    print("Seu salário é: R$", salario)
calcular_pgto(45, 10) # 45 é a quantidade de horas e 10 é o valor por hora

################ COMANDO RETURN #############################
def soma(a, b):
    resultado = a + b
    return resultado  # Retorna o resultado da soma

