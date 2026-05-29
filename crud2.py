#IMPORTA AS FUNÇOES
from funcoes import *



try:
    while True:
        menu()

        escolha = ler_inteiro("Escolha uma Opçâo: ")


        if escolha == 1:
            nome = str(input("Qual seu nome: "))
            idade = ler_inteiro("Qual sua idade: ")
            email = str(input("Qual seu email: "))
            senha = input("Qual sua senha: ")
            criar_usuario(nome, idade, email, senha)

        elif escolha == 2:

            listar_usuario()

        elif escolha == 3:

            id_usuario = ler_inteiro("Digite o ID do usuário: ")
            novo_nome = str(input("Novo nome: "))
            nova_idade = ler_inteiro("Nova idade: ")
            novo_email = str(input("Novo email: "))
            novo_senha = input("Nova senha: ")

            atualizar_usuario(id_usuario, novo_nome, nova_idade, novo_email, novo_senha)

        elif escolha == 4:

            id_usuario = ler_inteiro("Digite o ID para deletar: ")

            deletar_usuario(id_usuario)


        elif escolha == 5:
            
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            login_usuario(email, senha)


        elif escolha == 6:

            print("[yellow]Saindo do sistema...[/]")
            break

        else:

            print("[red]Opção inválida![/]")
finally:
    fechar_conexao()