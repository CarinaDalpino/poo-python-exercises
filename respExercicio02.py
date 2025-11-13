class aluno:
    def __init__(self, nome, matricula, curso, disciplina=None, notas=None):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplina = disciplina
        self.notas = notas if notas is not None else []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def status(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
        
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.2)
print(f"Média: {aluno.calcular_media()}")
print(f"Status: {aluno.status()}")






        

    
  
