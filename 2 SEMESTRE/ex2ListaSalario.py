def salario(horas_trabalhadas, valor_hora):
        if horas_trabalhadas <= 40:
            salario = horas_trabalhadas * valor_hora
        else:
            salario_base = 40 * valor_hora
            horas_extras = horas_trabalhadas - 40
            salario_extras = horas_extras * (valor_hora * 1.5)
            salario = salario_base + salario_extras
        return salario
horas = float(input("Digite as horas trabalhadas: "))
valor = float(input("Digite o valor da hora: "))
print(f"Salário a receber: R$ {salario(horas, valor):.2f}")


