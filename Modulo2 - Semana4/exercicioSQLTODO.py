import sqlite3

conexao = sqlite3.connect('exercicio.sqlite3')
cursor = conexao.cursor()

def criar_categoria():
    nome = input('Categoria? ')
    valores = [nome]
    
    sql = '''
    INSERT INTO categoria (nome) VALUES (?)
    '''

    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def atualizar_categoria():
    categoria = input('Qual o nome da categoria que você quer editar? ')
    nomes = input('Qual o novo nome da categoria? ')
    valores = [nomes, categoria]
    
    sql = '''
    UPDATE categoria SET nome= ? where nome= ?
    '''

    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def excluir_categoria():
    categoria = input('Qual o nome da categoria que você quer excluir? ')
    valores = [categoria]

    sql = '''
    DELETE from categoria where nome=?
    '''

    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def criar_TODO():
    nome = input('Tarefa? ')
    agenda = input('Data? ')
    categoria_id = int(input('Categoria? '))
    valores = [nome, agenda, 'NÃO CONCLUIDA', categoria_id]
    
    sql = '''
    INSERT INTO TODO (nome, agenda, status, categoria_id) VALUES (?, ?, ?, ?)
    '''
    
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def atualizar_TODO():
    identidade = input('Qual ID? ')
    nome = input('Tarefa? ')
    agenda = input('Data? ')
    categoria = int(input('Categoria? '))
    valores = [nome, agenda, categoria, identidade]
    
    sql = '''
    UPDATE TODO SET nome= ?, agenda= ?, status='NÃO CONCLUIDA', categoria_id= ? where id= ?
    '''

    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def excluir_TODO():
    categoria = input('Qual o nome da tarefa que você quer excluir? ')
    valores = [categoria]

    sql = '''
    DELETE from TODO where nome=?
    '''

    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def concluir_tarefa():
    identidade = int(input('ID? '))
    valores = [identidade]
    
    sql = '''
    UPDATE TODO SET status='CONCLUIDO' where id = ?
    '''
    
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def listar_categorias():
   
    sql = '''
    SELECT * FROM CATEGORIA
    '''
    
    retorno = cursor.execute(sql)
    for r in retorno:
        print(r)
    conexao.commit()
    conexao.close()

def listar_TODO():
   agenda = input('Qual a data? ')
   valores = [agenda]
   sql = '''
   SELECT * FROM TODO WHERE agenda = ?
   '''
    
   retorno = cursor.execute(sql, valores)
   for r in retorno:
       print(r)
   conexao.commit()
   conexao.close()

print('1 - Criar Categoria')
print('2 - Alterar Categoria')
print('3 - Excluir Categoria')
print('4 - Criar TODO')
print('5 - Alterar TODO')
print('6 - Excluir TODO')
print('7 - Listar as tarefas de uma data')
print('8 - Listar todas categorias')
print('9 - Concluir tarefa')

opcao = int(input('Escolhe um número de 1 a 9: '))
while opcao <= 0 or opcao > 9:
    print('Você digitou um número inválido.')
    opcao = int(input('Escolhe um número de 1 a 9: '))

if opcao == 1:
    print('Opção selecionada: Criar Categoria')
    criar_categoria()
elif opcao == 2:
    print('Opção selecionada: Alterar Categoria')
elif opcao == 3:
    print('Opção selecionada: Excluir Categoria')
    excluir_categoria()
elif opcao == 4:
    print('Opção selecionada: Criar TODO')
    criar_TODO()
elif opcao == 5:
    print('Opção selecionada: Alterar TODO')
    atualizar_TODO()
elif opcao == 6:
    print('Opção selecionada: Excluir TODO')
    excluir_TODO()
elif opcao == 7:
    print('Opção selecionada: Listar as tarefas de uma data')
    listar_TODO()
elif opcao == 8:
    print('Opção selecionada: Listar todas as categorias')
    listar_categorias()
elif opcao == 9:
    print('Opção selecionada: Concluir tarefa')
    concluir_tarefa()


    


