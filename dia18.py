class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✓" if self.concluida else " "
        return f"[{status}] {self.titulo} - {self.descricao}"


class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)
        print(f"Tarefa '{titulo}' adicionada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada.")
        else:
            print("\n--- SUAS TAREFAS ---")
            for indice, tarefa in enumerate(self.tarefas):
                print(f"{indice + 1}. {tarefa}")

    def marcar_tarefa_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            print(f"Tarefa '{self.tarefas[indice].titulo}' marcada como concluída!")
        else:
            print("Número de tarefa inválido.")

    def deletar_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            titulo = self.tarefas[indice].titulo
            self.tarefas.pop(indice)
            print(f"Tarefa '{titulo}' deletada com sucesso!")
        else:
            print("Número de tarefa inválido.")


if __name__ == "__main__":
    gerente = GerenciadorDeTarefas()
    
    gerente.adicionar_tarefa("Estudar Python", "Praticar conceitos de POO")
    gerente.adicionar_tarefa("Comprar mantimentos", "Leite, ovos e pão")
    
    gerente.listar_tarefas()
    
    gerente.marcar_tarefa_concluida(0)
    gerente.listar_tarefas()
    
    gerente.deletar_tarefa(1)
    gerente.listar_tarefas()