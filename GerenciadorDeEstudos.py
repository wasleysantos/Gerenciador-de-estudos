class GerenciadorDeEstudos:
    def __init__(self):
        self.disciplinas = [  
            
            "Gestão Organizacional",
            "Gestão Governamental e Governança Pública",
            "Políticas Públicas",
            "Gerência e Suporte da Tecnologia da Informação",
            "Desenvolvimento de Software",
            "Inteligência Artificial",
            
        ]
        self.topicos = {disciplina: [] for disciplina in self.disciplinas}

    def adicionar_topico(self, index_disciplina, descricao_topico, prioridade=1):
        disciplina = self.disciplinas[index_disciplina]
        self.topicos[disciplina].append((descricao_topico, prioridade))
        self.topicos[disciplina].sort(key=lambda x: x[1])

    def listar_disciplinas(self):
        print("Disciplinas:")
        for i, disciplina in enumerate(self.disciplinas, 1):
            print(f"{i}. {disciplina}")

    def listar_topicos_disciplina(self, index_disciplina):
        disciplina = self.disciplinas[index_disciplina]
        print(f"Disciplina: {disciplina}")
        for descricao, prioridade in self.topicos[disciplina]:
            print(f"  Tópico: {descricao}, Prioridade: {prioridade}")

def main():
    gerenciador = GerenciadorDeEstudos()

    while True:
        print("\n-------------------------------------------")
        print("Menu:                                     |")
        print("1. Listar disciplinas                     |")
        print("2. Tópicos de uma disciplina              |")
        print("3. Adicionar tópico a uma disciplina      |")
        print("4. Sair                                   |")
        print("-------------------------------------------")
        escolha = input("Escolha uma opção: ")
        

        if escolha == '1':
            gerenciador.listar_disciplinas()
        elif escolha == '2':
            gerenciador.listar_disciplinas()
            index_disciplina = int(input("Digite o número da disciplina: ")) - 1
            gerenciador.listar_topicos_disciplina(index_disciplina)
        elif escolha == '3':
            gerenciador.listar_disciplinas()
            index_disciplina = int(input("Digite o número da disciplina: ")) - 1
            descricao = input("Digite a descrição do tópico: ")
            prioridade = int(input("Digite a prioridade do tópico (número inteiro): "))
            gerenciador.adicionar_topico(index_disciplina, descricao, prioridade)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
