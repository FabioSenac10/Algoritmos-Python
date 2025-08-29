# Exercícios Básicos (1–20)
# Crie uma função que receba um nome e imprima uma saudação personalizada.
def hello(nome):
 print("Seja bem-vindo", nome) # NOME é o parametro
a=input("DIGITE SEU NOME: ")
hello(a) 

# Crie uma função que receba dois números e retorne sua soma.
def soma():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    res = a + b
    print("A soma é:", res)
soma()

# Escreva uma função que calcule o quadrado de um número.
def verificar_par():
    numero = float(input("Digite um número: "))
    if numero%2==0:
        print("O número", numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")
verificar_par()

# Escreva uma função que verifique se um número é par.
def verificar_impar():
    numero = float(input("Digite um número: "))
    if numero%2!=0:
        print("O número", numero, "é ímpar.")
    else:
        print("O número", numero, "não é impar.")
verificar_impar()

# Escreva uma função que receba uma lista de números e retorne o maior elemento.
def maior_numero():
    lista_numeros = input("Digite uma lista de números inteiros separados por vírgula: ")
    numeros = [int(num) for num in lista_numeros.split(",")]
    maior = numeros[0] 
    for num in numeros:
        if num > maior:
            maior = num
    print("O maior número é:", maior)
maior_numero()

# Crie uma função que calcule o fatorial de um número (sem usar recursão).
def fatorial():
    numero = int(input("DIGITE UM NÚMERO: "))
    if numero < 0:
        return "DIGITE UM NÚMERO MAIOR QUE ZERO."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado
fatorial_resultado = fatorial()
print("O fatorial é:", fatorial_resultado)

# Crie uma função que receba um número e retorne True se ele for primo.
def num_primo():
    numero = int(input("Digite um número: "))
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
if num_primo():
    print("O número é primo.")
else:
    print("O número não é primo.")


# Crie uma função que inverta uma string.
def inverter_string():
    texto = input("Digite uma string: ")
    texto_invertido = texto[::-1]
    print("String invertida:", texto_invertido)

# Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.
def nomes_digitados5letras():
    lista = input("DIGITE OS NOMES SEPARADOS POR VIRGULA: ")
    return [nome.strip() for nome in lista.split(",") if len(nome.strip()) > 5]

print(nomes_digitados5letras())

# Escreva uma função que conte quantas vogais há em uma string.
def contar_vogais():
    texto = input("Digite uma string: ")
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    print("Quantidade de vogais:", contador)

# Crie uma função que receba um número e retorne uma lista com todos os divisores dele.
def divisores():
    numero = int(input("Digite um número inteiro: "))
    lista_divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            lista_divisores.append(i)
    print(f"Divisores de {numero}: {lista_divisores}")

# Crie uma função que converta graus Celsius para Fahrenheit.
def celsius_para_fahrenheit()
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")
    
# Crie uma função que receba uma string e retorne a mesma string sem espaços.
def remove_espaco():
  lista_de_strings = ["Ana", "Pedro", "São Paulo", "Guerra"]
  lista_sem_espacos = [item.replace(" ", "") for item in lista_de_strings]
  return lista_sem_espacos
resultado = remove_espaco()
print(resultado)

# Crie uma função que receba uma lista e retorne a média dos elementos.
def media_lista():
    lista_numeros = input("Digite uma lista de números separados por vírgula: ")
    numeros = [float(num) for num in lista_numeros.split(",")]
    media = sum(numeros) / len(numeros)
    print("A média é:", media)

# Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.
def verificar_palindromo():
    palavra = input("Digite uma palavra: ")
    palavra_invertida = palavra[::-1]
    if palavra.lower() == palavra_invertida.lower():
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")

# Crie uma função que gere uma lista com os n primeiros números pares.
def numeros_pares(n):
    return [i for i in range(2, n * 2 + 1, 2)]

# Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).
def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Crie uma função que calcule a área de um retângulo (base × altura).
def area_retangulo():
    altura = float(input("Digite a altura do retângulo: "))
    base = float(input("Digite a base do retângulo: "))
    area = base * altura
    print("A área do retângulo é:", area)
area_retangulo()

# Crie uma função que retorne o menor valor entre três números.
def menor_valor():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    c = float(input("Digite o terceiro número: "))
    menor = min(a, b, c)
    print("O menor valor é:", menor)
menor_valor()

# Escreva uma função que simule o lançamento de um dado de 6 faces (use random.randint).
def lancamento_dado():
    import random
    resultado = random.randint(1, 6)
    print("O resultado do lançamento do dado é:", resultado)
lancamento_dado()

# 🟡 Exercícios Intermediários (21–40)
# Crie uma função que receba uma lista de números e retorne uma nova lista com os números elevados ao quadrado.
def elevar_ao_quadrado(lista):
    return [numero ** 2 for numero in lista]
entrada = input("Digite os números separados por espaço: ")
numeros = [int(x) for x in entrada.split()]
resultado = elevar_ao_quadrado(numeros)
print("Números ao quadrado:", resultado)

# Crie uma função que calcule a soma dos dígitos de um número inteiro.
def soma_digitos(numero):
   n= int(input("Digite um número inteiro: "))
   soma = 0
   for digito in str(n):
       soma += int(digito)
   return soma
print("A soma dos dígitos é:", soma_digitos(0))

# Escreva uma função que receba uma frase e retorne a quantidade de palavras.
def contar_palavras(frase):
    if not frase:
        return 0
    frase = frase.strip()
    palavras = frase.split()
    return len(palavras)
frase_digitada = input("Digite uma frase: ")
print("Quantidade de palavras:", contar_palavras(frase_digitada))

# Crie uma função que substitua todas as vogais de uma string por "*".
def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    for vogal in vogais:
        frase = frase.replace(vogal, "*")
    return frase
frase_digitada = input("Digite uma frase: ")
print("Frase com vogais substituídas:", substituir_vogais(frase_digitada))

# Crie uma função que receba uma lista e retorne os elementos únicos (sem usar set).
def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos
lista = input("Digite os elementos da lista separados por vírgula: ").split(",")
print("Elementos únicos:", elementos_unicos(lista))

# Crie uma função que receba uma lista e um número n, e retorne os n maiores valores da lista.
def n_maiores(lista, n):
    if n > len(lista):
        return "O valor de n é maior que o tamanho da lista."
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada[:n]
lista_numeros = input("Digite os números separados por vírgula: ").split(",")
print("Os 3 maiores números são:", n_maiores(lista_numeros, 3))

# Escreva uma função que calcule a área de um triângulo (base × altura ÷ 2).
# Crie uma função recursiva para calcular o fatorial de um número.
# Crie uma função recursiva que calcule o n-ésimo número da sequência de Fibonacci.
# Escreva uma função que embaralhe os caracteres de uma string (use random.shuffle).
# Crie uma função que simule uma calculadora simples (operações: +, -, *, /), com três parâmetros: número 1, número 2 e operação.
# Crie uma função que retorne os números pares de uma lista usando list comprehension.
# Escreva uma função que recebe um número decimal e retorna sua representação binária.
# Escreva uma função que receba uma lista e retorne um dicionário com a contagem de cada elemento.
# Crie uma função que receba uma data (dia, mês, ano) e diga se ela é válida (considere apenas datas do calendário gregoriano, sem considerar anos bissextos).
# Escreva uma função que identifique o segundo maior número em uma lista.
# Crie uma função que receba uma lista de strings e retorne a maior delas.
# Escreva uma função que calcule a distância entre dois pontos (x1, y1) e (x2, y2).
# Crie uma função que receba o valor de uma compra e retorne o valor com 10% de desconto.
# Crie uma função que calcule juros compostos: montante = capital * (1 + taxa) ** tempo.

# 🔴 Exercícios Avançados (41–50)
# Crie uma função decoradora que registre o tempo de execução de outra função.
# Crie uma função que retorne uma função interna (closure) que acumula valores.
# Crie uma função que receba um CPF em formato string e valide-o.
# Escreva uma função que leia um arquivo texto e conte quantas palavras ele possui.
# Crie uma função que use filter() e lambda para filtrar números maiores que 10 de uma lista.
# Escreva uma função que utilize zip para unir duas listas em um dicionário.
# Escreva uma função que leia uma matriz (lista de listas) e retorne sua transposta.
# Crie uma função que gere senhas seguras com letras, números e símbolos (use random.choice).
# Crie uma função que detecte anagramas entre duas palavras.
# Crie uma função que verifique se uma Sudoku 9x9 está corretamente preenchida (sem números repetidos por linha, coluna e região 3x3).
