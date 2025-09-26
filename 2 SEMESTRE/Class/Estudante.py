class Estudante: ## Nome da classe
    def __init__(self, nome, idade, nota): ## Método
        self.nome=nome  ##Atributo
        self.idade=idade  ##Atributo
        self.nota=nota  ##Atributo

    def get_grade(self):
        print(self.nota)

e1=Estudante("luis", 20,10)
e2=Estudante("Isabela", 20,10)
print(e1.nome)
