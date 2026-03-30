dados_fixos = ("Curso: Introdução à Programação", "Duração: 4 semanas", "Carga horária: 40 horas", "Nível: Iniciante")
opcao = -1
participantes = []

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
        while idade < 0:
            print("Idade inválida, tente novamente.")
            idade = int(input("Digite a idade do participante: "))
        
        horas_estudo = int(input("Digite a quantidade de horas de estudo: "))
        while horas_estudo < 0:
            print("Quantidade de horas de estudo inválida, tente novamente.")
            horas_estudo = int(input("Digite a quantidade de horas de estudo: "))
        
        area_interesse = input("Digite a área de interesse: ")
        
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
            for i, aluno in enumerate(participantes, start=1):
                print(f"{i}. {aluno['nome']} | Idade: {aluno['idade']} | Horas de Estudo: {aluno['horas_estudo']} | Área de Interesse: {aluno['area_interesse']}")
    
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
            
        print("Participantes com bom desempenho de estudo: ")
        for aluno in participantes:
            if aluno['horas_estudo'] >= 5:
                print(f"{aluno['nome']} - Horas de Estudo: {aluno['horas_estudo']}")
        
        print("Áreas de interesse dos participantes: ")

        areas = []
        for aluno in participantes:
            if aluno['area_interesse'] not in areas:
                areas.append(aluno['area_interesse'])
                
        for area in areas:
            print(f"- {area}")

    elif opcao == 4:
        print("Saindo do sistema. Até mais!")
    
    else: 
        print("Opção inválida, tente novamente.")