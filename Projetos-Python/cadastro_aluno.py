opcao = -1
contador = 0
alunos = []

class Aluno:
    def __init__(self, nome, disciplina, turno):
        self.nome = nome
        self.disciplina = disciplina
        self.turno = turno

print("Bem-vindo ao sistema de gerenciamento de alunos!")
input("Pressione Enter para continuar")
nome_usuario = input("Digite o seu nome: ")

while opcao != 0:
    print("--- MENU ---")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Retirar aluno")
    print("0. Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Cadastro de aluno selecionado, {nome_usuario}.")
        nome = input("Digite o nome do aluno: ")
        disciplina = input("Digite a disciplina do aluno: ")
        turno = input("Digite o turno do aluno: ")
        aluno = Aluno(nome, disciplina, turno)
        print(f"Aluno {aluno.nome} cadastrado com sucesso!")
        alunos.append(aluno)

    
    elif opcao == 2:
        print(f"Listar alunos selecionado, {nome_usuario}.")
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for i, aluno in enumerate(alunos):
                print(f"[{i + 1}]: {aluno.nome} ({aluno.disciplina}) - {aluno.turno}")

    elif opcao == 3:
        print(f"Retirar aluno selecionado, {nome_usuario}.")
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado para retirar")
        else:
            for i, aluno in enumerate(alunos):
                print(f"[{i + 1}]: {aluno.nome} ({aluno.disciplina}) - {aluno.turno}")
            numero_aluno = int(input("Digite o número do aluno a ser retirado: "))
            if numero_aluno < 1 or numero_aluno > len(alunos):
                print("Número inválido, tente novamente.")
            else:
                aluno_retirado = alunos.pop(numero_aluno - 1)
                print(f"Aluno {aluno_retirado.nome} retirado com sucesso!")
                    
    elif opcao == 0:
        print(f"Saindo do sistema. Até mais, {nome_usuario}!")
    else:
        print(f"Opção inválida, {nome_usuario}, tente novamente.")
        
    contador += 1
    print(f"Total de interações no menu: {contador}")