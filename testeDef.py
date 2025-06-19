def soma_digitos(numero):
   n= int(input("Digite um número inteiro: "))
   soma = 0
   for digito in str(n):
       soma += int(digito)
   return soma
print("A soma dos dígitos é:", soma_digitos(0))