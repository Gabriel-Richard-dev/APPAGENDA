#                                   AGENDA TELEFONICA
import sqlite3
from contextlib import closing

ask = 0
contatos = []
def CriaBanco():
    return 'create table agenda(id integer primary key autoincrement,Nome text, Telefone text, Fixo text, Trabalho text, Email text, Aniversário Text)'


def mostrar_alteração(num):
    global contatos
    list = ['Nome', 'Telefone','Fixo','Trabalho', 'Email', 'Aniversário']
    for x, nomes in enumerate(contatos[num]):
        print(f'[{x+1}] | {list[x]} {nomes}')
def novo():
    global contatos
    temp = []
    print('CRIAR NOVO CONTATO'.center(100))
    while True:    
        try:
            nome = input('\nInsira o nome do novo contato: ')
            telefone = int(input('\nInsira o número de telefone: '))
        except Exception:
            print("tente novamente!")
        else: 
            temp.append(nome)
            temp.append(telefone)
            break
    perg = ['Fixo','Trabalho', 'Email', 'Aniversário']
    for e in perg:
        ask = input(f'\nDeseja adicionar {e}? ("s" ou "n")\nResposta:').lower()
        if ask == "s":
            if e == 'Fixo' or e == 'Trabalho':
                e = int(input(f'Insira o número de {e}: '))
                temp.append(e)
            else:
                e = input(f'Insira o/a {e}')
                temp.append(e)
        else:
            e = 'Nada'
            temp.append(e)
    contatos.append(temp)
    print(contatos)
def alterar(num = -1):
    if num == -1:
        mostrar(1)
    else:
        
        while True:
            mostrar_alteração(num)
            seleção = int(input('Insira um Índice (0 p sair)\n\nSua Resposta:'))
            if seleção == 0:
                return None
            else:
                seleção -= 1
                if 1 <= seleção <= 3:
                    contatos[num][seleção] = int(input('Insira um número: '))
                else:
                    contatos[num][seleção] = input("Insira seu novo valor: ")

def opções(cield = 0):
    ask = int(input('Selecione o número do contato ou 0 para sair:'))
    if ask == 0:
        return None
    else:
        ask -= 1
        print(f'''
        \033[1;47m

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-CARTÃO DE CONTATO-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        Nome: {contatos[ask][0]}
        Aniversário: {contatos[ask][5]} | Telefone: {contatos[ask][1]} 
        

        Email: {contatos [ask][4]}
        Nº Trabalho: {contatos[ask][3]}  | Fixo: {contatos[ask][2]}

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-        
        \033[m
        \n''')
        if cield == 1:
            perg = input('Deseja editar ou sair? ("e" p editar "0" p/ sair)\nResposta:').lower()
            if perg == 'e':
                alterar(ask)
            else:
                mostrar(1)
        if cield == 2:
            perg = input('Deseja deletar ou sair? ("d" p deletar "0" p/ sair)\nResposta:').lower()
            if perg == 'd':
                contatos.remove(contatos[ask])
            else:
                mostrar(2)
def deletar():
    mostrar(2)
    
 


def mostrar(cield = 0):
    print('\033[1;41mAGENDA TELEFÔNICA\033[m'.center(100))
    for x, linhas in enumerate(contatos):
        print(f'[{x+1}] Nome: {linhas[0]} | Telefone: {linhas[1]}')
    if cield == 1:
        opções(1)
    if cield == 2:
        opções(2)

def salvar():
    global contatos
    arquivo = input('Insira o nome do arquivo: ')
    
    with open('histórico.txt', 'w') as hist:
        hist.write(arquivo)
    with sqlite3.connect(arquivo) as conexão:
        with closing(conexão.cursor()) as cursor:
            try:
                try:
                    cursor.execute('drop table agenda')
                except Exception:
                    pass
                cursor.execute(CriaBanco())
            except Exception:
                pass
            else:
                pass
            for linha in contatos:
                print(linha)
                cursor.execute('insert into agenda (Nome, Telefone, Fixo, Trabalho, Email, Aniversário) values (?, ?, ?, ?, ?, ?)', (linha))
                
def lê(nome='nada'):
    global contatos
    if nome == 'nada':
        arquivoo = input('Insira o Nome do Arquivo: ')
        with open('histórico.txt', 'w') as hist:
            hist.write(arquivoo)
    else:
        arquivoo = nome
        print('''
        HISTÓRICO ABRINDO
        ''')

    with sqlite3.connect(arquivoo) as conexão:
        with closing(conexão.cursor()) as cursor:
            cursor.execute('select * from agenda')
            resultado = cursor.fetchall()
            for e in resultado:
                contatos.append(e)

        
    

def ordenar():
    for e in range(len(contatos)-1):
        for x in range(len(contatos)-1):
            if contatos[x][0] > contatos[x+1][0]:
                contatos[x], contatos[x+1] = contatos[x+1], contatos[x]

def validação(num1, num2):
    global ask
    while True:
        try:
            ask = int(input('Insira sua escolha: '))
        except Exception:
            print('Tente novamente!')
        else:
            break
    if num1 <= ask <= num2:
        return ask
    else:
        print('tente novamente')

    

def menu():

    print(
        f'''
        1 - Criar Novo
        2 - Alterar
        3 - Deletar
        4 - Mostrar Agenda
        5 - Salvar
        6 - Abrir Outra Lista
        7 - Ordenar Lista       
                               
        \033[1;41m[ Contatos: {len(contatos)} ]\033[m
        '''
    )
    return validação(1, 7)

def histórico():
    try:
        with open('histórico.txt', "r") as hist:
            lê(hist.read())
    except Exception:
        print('Não foi possivel abrir o Histórico')
histórico()

while True:
    menu()
    if ask == 1:
        novo()
    if ask == 2:
        alterar()
    if ask == 3:
        deletar()
    if ask == 4:
        mostrar()    
    if ask == 5:
        salvar()    
    if ask == 6:
        lê()    
    if ask == 7:
        ordenar()