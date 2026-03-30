dados_fixos = ("Curso: Introdução à Programação", "Duração: 4 semanas", "Carga horária: 40 horas", "Nível: Iniciante")
opcao = -1

print(f"{dados_fixos[0]} | {dados_fixos[2]} | {dados_fixos[3]}")
while opcao != 4:
    print("1. Cadastrar participante")
    print("2. Listar participantes")
    print("3. Mostrar análises")
    print("4. Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do participante: ")
        idade = int(input("Digite a idade do participante: "))
        horas_estudo = int(input("Digite a quantidade de horas de estudo: "))
        area_interesse = input("Digite a área de interesse: ")
        
        participantes = []
        
        participantes.append({
            'nome': nome,
            'idade': idade,
            'horas_estudo': horas_estudo,
            'area_interesse': area_interesse
        })
        
        print(f"Participante {nome} cadastrado com sucesso!")
        
    elif opcao == 2:
        print("Participantes cadastrados: ")
        if len(participantes) == 0:
            print("Nenhum participante cadastrado.")
        else:
            for i, aluno in enumerate(participantes):
                print(f"{i + 1}. {aluno['nome']} | Idade: {aluno['idade']} | Horas de Estudo: {aluno['horas_estudo']} | Área de Interesse: {aluno['area_interesse']}")
    
    elif opcao == 3:
        print("Análise dos participantes:")
        if len(participantes) == 0:
            print("Nenhum participante cadastrado para análise.")
        else:
            
            lista_idade = []
            lista_horas = []
            
            for aluno in participantes:
                lista_idade.append(aluno['idade'])
                lista_horas.append(aluno['horas_estudo'])
        
            maiores_idade = sum(1 for idade in lista_idade if idade >= 18)
            media_horas_estudo = sum(lista_horas) / len(lista_horas) 

        print(f"Quantidade de participantes maiores de idade: {maiores_idade}")
        print(f"Média de horas de estudo: {media_horas_estudo:.2f}")
            
        for aluno in participantes:
            if aluno['horas_estudo'] >= 5:
                print(f"Participante {aluno['nome']} tem um bom desempenho.")
    
    elif opcao == 4:
        print("Saindo do sistema. Até mais!")
    
    else: 
        print("Opção inválida, tente novamente.")