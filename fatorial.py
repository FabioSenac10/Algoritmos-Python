FATORIAL
numero=int(input("Digite o fatorial: "))
valor=1
for n in range(numero, 1,-1):
  valor=valor*n
print("O valor do fatorial de ",numero," é ",valor)

SEQUENCIA 
n=int(input("Digite o número de termos da sequência: "))
a=1
b=1
for i in range(n):
  print(a, end=" ")
  a, b = b, a + b
