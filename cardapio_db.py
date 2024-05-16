import sqlite3

#crio a conexão com o banco de dados
conn = sqlite3.connect('cardapio.db')

#cria um cursor
cursor = conn.cursor()

#checa se a tabela 'cardapio' existe
cursor.execute('''SELECT count(name) FROM sqlite_master WHERE
               type="table" and name = "cardapio"''')

#se a tabela não existir crie-a
if cursor.fetchone()[0] == 0:
    cursor.execute('''
        CREATE TABLE cardapio(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            descricao TEXT,
            pedido TEXT,
            disponivel INTEGER DEFAULT 1
        )
    ''')

    conn.commit()

while True:
    nome = input("Nome do item (digite 'sair' para sair): ")
    if nome == 'sair':
        break
    preco = float(input("preco do item: "))
    descricao = input("descrição do item: ")
    pedido = int(input("Pedido ( 1 - Cozinha, 2 - Bar) "))
    pedido = "Cozinha" if pedido == '1' else 'Bar'

    cursor.execute(f'''
        INSERT INTO cardapio (nome, preco, descricao, pedido)
        VALUES ('{nome}', {preco}, '{descricao}', '{pedido}')
    ''')
    
    conn.commit()

conn.close()