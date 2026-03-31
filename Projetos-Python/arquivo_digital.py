#Código "Memória Viva" para o curso de Introdução ao Python pela WoMakersCode

import os
mulheres_programadoras = []

def validar_texto(texto):
    if not texto or not all(c.isalpha() or c.isspace() for c in texto):
        return False
    return True

def verificar_nome_cadastrado(nome):
    if os.path.exists("memoria_mulheres_tech.txt"):
        with open("memoria_mulheres_tech.txt", mode="r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.startswith("Nome:"):
                    nome_arquivo = linha.split(":", 1)[1].strip()
                    if nome_arquivo.lower() == nome.lower():
                        return True
    return False
                    

def exibir_historico():
    print("\nHistórico de Mulheres Tech Cadastradas:\n")
    if os.path.exists("memoria_mulheres_tech.txt"):
        with open("memoria_mulheres_tech.txt", mode="r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
            for linha in conteudo:
                print(linha.strip())
    else:
        print("Nenhuma mulher tech cadastrada ainda.")

def busca_por_nome(nome):
    if os.path.exists("memoria_mulheres_tech.txt"):
        with open("memoria_mulheres_tech.txt", mode="r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            for i in range(len(linhas)):
                if linhas[i].startswith("Nome:"):
                    nome_arquivo = linhas[i].split(":", 1)[1].strip()

                    if nome.lower() in nome_arquivo.lower():
                        print("\nMulher Tech encontrada:\n")

                        j = i
                        while j < len(linhas) and not linhas[j].startswith("-"):
                            print(linhas[j].strip())
                            j += 1

                        return

        print("Mulher tech não encontrada.")
    else:
        print("Nenhuma mulher tech cadastrada ainda.")

def quantidade_mulheres():
    if os.path.exists("memoria_mulheres_tech.txt"):
        with open("memoria_mulheres_tech.txt", mode="r", encoding="utf-8") as arquivo:
            total_mulheres = sum(1 for linha in arquivo if "Nome:" in linha)
            print(f"Total de mulheres tech cadastradas: {total_mulheres}")
    else:
        print("Nenhuma mulher tech cadastrada ainda.")
        
def anos_contribuicao():
    if os.path.exists("memoria_mulheres_tech.txt"):
        anos = []

        with open("memoria_mulheres_tech.txt", mode="r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.startswith("Ano:"):
                    ano = int(linha.split(":")[1].strip())
                    anos.append(ano)

        if anos:
            print(f"Ano mais antigo: {min(anos)}")
            print(f"Ano mais recente: {max(anos)}")
        else:
            print("Nenhum ano registrado.")
    else:
        print("Nenhuma mulher tech cadastrada ainda.")
        
print("Arquivo digital - Memória Viva: Mulheres na Tecnologia")

while True:

    print("\n1. Cadastrar Mulher Tech")
    print("2. Listar histórico")
    print("3. Buscar por nome")
    print("4. Exibir estatísticas")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        
        print("\nCadastro de Mulher Tech\n")
        nome = input("Digite o nome da mulher tech: ")
        
        if not validar_texto(nome): #verifica se o nome contém apenas letras e espaços, se conter números ou estiver vazio, retorna mensagem e volta para o início do loop
            print("Entrada inválida. Por favor, escreva apenas letras e espaços para o nome.")
            continue
        
        ja_cadastrada = verificar_nome_cadastrado(nome) #verifica se o nome já está cadastrado, se estiver, retorna mensagem e volta para o início do loop
        
        if ja_cadastrada:
            print("Essa mulher tech já está cadastrada. Por favor, cadastre outra.")
            continue
        else:
            
            area = input("Digite a área de atuação: ")
            if not validar_texto(area): #verifica se a área contém apenas letras e espaços, se conter números, retorna mensagem e volta para o início do loop
                print("Entrada inválida. Por favor, escreva apenas letras e espaços para a área.")
                continue
            
            contribuicao = input("Descreva a contribuição dela para a tecnologia: ")
            if not validar_texto(contribuicao): #verifica se a contribuição contém apenas letras e espaços, se conter números, retorna mensagem e volta para o início do loop
                print("Entrada inválida. Por favor, escreva apenas letras e espaços para a contribuição.")
                continue
            
            try:
                ano = int(input("Digite o ano da contribuição: "))
            except ValueError: #verifica se o ano é um número inteiro, se não for, retorna mensagem e volta para o início do loop
                print("Entrada inválida. Por favor, escreva apenas números para o ano.")
                continue
        
        mulheres_programadoras.append({
            'nome': nome,
            'area': area,
            'contribuicao': contribuicao,
            'ano': ano
        })
        
        with open("memoria_mulheres_tech.txt", mode="a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"Área: {area}\n")
            arquivo.write(f"Contribuição: {contribuicao}\n")
            arquivo.write(f"Ano: {ano}\n")
            arquivo.write("-" * 20 + "\n")
        
        print(f"{nome} cadastrada com sucesso!")
        
    elif opcao == "2":
        exibir_historico()
    
    elif opcao == "3":
        print("\nBusca por Nome\n")
        nome_busca = input("Digite o nome da mulher tech que deseja buscar: ")
        busca_por_nome(nome_busca)
    
    elif opcao == "4":
        print("\nEstatísticas\n")
        quantidade_mulheres()
        anos_contribuicao()
        
    elif opcao == "5":
        print("Este arquivo existe porque histórias importam. Mulheres sempre estiveram presentes na tecnologia. E agora, você também faz parte dessa transformação.")
        break
    
    else: 
        print("Opção inválida. Por favor, escolha uma opção válida.")