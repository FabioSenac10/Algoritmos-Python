while True:
    opcao=input("Digite a operação desejada: M para multiplicação, A para adição, D para divisão e S para subtração: \n")
    if opcao=="M" or opcao=="m":
      n1=float(input("Digite o primeiro número: "))
      n2=float(input("Digite o segundo número: "))
      mult=n1*n2
      print(mult)
    elif opcao=="A" or opcao=="a":
      n1=float(input("Digite o primeiro número: "))
      n2=float(input("Digite o segundo número: "))
      soma=n1+n2
      print(soma)
    elif opcao=="D" or opcao=="d":
      n1=float(input("Digite o primeiro número: "))
      n2=float(input("Digite o segundo número: "))
      div=n1/n2
      print(div)
    elif opcao=="S" or opcao=="s":
      n1=float(input("Digite o primeiro número: "))
      n2=float(input("Digite o segundo número: "))
      subt=n1-n2
      print(subt)
    elif opcao=="X" or opcao=="x":
      print("Encerramento")
      break
    else:
      print("Opção invalido")