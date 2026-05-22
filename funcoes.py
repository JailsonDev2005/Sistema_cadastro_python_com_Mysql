#MELHORA A SAIDA DO TERMINAL
from rich import print
#CAIXAS PAINÉIS ESTILIZADAS NO TERMINALp
from rich.panel import Panel
#TABELAS BONITAS E ORGANIZADAS
from rich.table import Table
#PERMITE USAR O BANCO DE DADOS MYSQL
import mysql.connector
#PARA VALIDAR FORMATOS COMO EMAIL   
import re

import bcrypt




#CRIA UM BANCO DE DADOS
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="seu_banco"
)

cursor = conn.cursor()


#CRIA TABELA NO BANCO USANOD O MÓDULO
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL
)
""")


#SALVA AS ALTERAÇOES NO BANCO DE DADOS
conn.commit()


#CRIPTOGRAFA A SENHA
def criptografar_senha(senha):
    senha_byte = senha.encode('utf-8')

    salt = bcrypt.gensalt()

    hash_senha = bcrypt.hashpw(senha_byte, salt)

    return hash_senha.decode('utf-8')


#VALIDA EMAIL GMAIL
def validar_gmail(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

    if re.match(padrao, email):
        return True
    
    return False


#CRIA UM MENU NO TERMINAL
def menu():

    conteudo = "Cadastro"
    conteudo += "\n1. Criar cadastro"
    conteudo += "\n2. Ler cadastro"
    conteudo += "\n3. Atualizar cadastro"
    conteudo += "\n4. Deletar cadastro"
    conteudo += "\n5. Sair"
    menu = Panel(conteudo, title="Sistema Cadastro", width=28, expand=False)
    print(menu)


#INSERE UM USURÁRIO NA TABELA
def criar_usuario(nome, idade, email, senha):

    senha = criptografar_senha(senha)

    if not validar_gmail(email):
        print("[red]Digite um Gmail válido![/]")
        return


    cursor.execute(
        "INSERT INTO usuarios (nome, idade, email, senha)    VALUES (%s, %s, %s, %s)",
        (nome, idade, email, senha)
    )

    conn.commit()

    print("[green]Cadastro realizado com sucesso![/]")


#MOSTRA OS USUÁRIOS DE FROMA ORGANIZADA
def listar_usuario():
    cursor.execute("SELECT id, nome, idade, email FROM usuarios")

    usuarios = cursor.fetchall()

    if not usuarios:
        print("[yellow]Nenhum usuário cadastrado[/]")
        return

    table = Table(title="Lista de Usuários")
    table.add_column("ID", style="cyan")
    table.add_column("Nome", style="green")
    table.add_column("Idade", style="yellow")
    table.add_column("Email", style="magenta")

    for usuario in usuarios:
        table.add_row(
            str(usuario[0]),
            usuario[1],
            str(usuario[2]),
            usuario[3]
        )

    print(table)

#ATUALIZAR OS DADOS DE UM USUÁRIO JA EXISTENTE
def atualizar_usuario(id_usuario, nome, idade, email, senha):

    if not validar_gmail(email):
        print("[red]Digite um Gmail válido![/]")
        return

    senha = criptografar_senha(senha)

    cursor.execute("""
        UPDATE usuarios
        SET nome = %s, idade = %s, email = %s, senha = %s
        WHERE id = %s
    """, (nome, idade, email, senha, id_usuario))

    conn.commit()

    if cursor.rowcount == 0:
        print("[red]Usuário não encontrado[/]")
    else:
        print("[green]Cadastro atualizado![/]")


#REMOVE UM USUÁRIO DO BANCO DE DADOS
def deletar_usuario(id_usuario):

    cursor.execute(
        "DELETE FROM usuarios WHERE id = %s",
        (id_usuario,)
    )

    conn.commit()


    if cursor.rowcount == 0:
        print("[red]Usuário não encontrado[/]")
    else:
        print("[green]Cadastro deletado![/]")

#GARANTI QUE O USUÁRIO DIGITE UM NÚMERO INTEIRO VÁLIDO
def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("[red]Digite apenas números[/]")


#FECHA A CONEXÃO COM O BANCO DE DADOS
def fechar_conexao():
    cursor.close()
    conn.close()
