import sqlite3

#conecta a base de dados
conn = sqlite3.connect('example.db')

#cria um cursor
cursor = conn.cursor()

#cria uma tabela (nome da tabela, tipo de dado)
#tipos de dados: NULL, INTEGER, REAL, TEXT, BLOB
#cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
#conn.commit()

#insiro uma informção na tabela
#cursor.execute("INSERT INTO users (name) VALUES ('John')")
#conn.commit()

#atualizo um dado
#cursor.execute("UPDATE users SET name = 'Jane' WHERE id = 3")
#conn.commit()

#seleciona todos os dados da tabela e mostra eles
#cursor.execute("SELECT * FROM users")
#print(cursor.fetchall())

#seleciona os dados que tem como nome Jane
#cursor.execute("SELECT * FROM users WHERE name = 'Jane'")
#print(cursor.fetchall())

#deleta um dado da tabela
#cursor.execute("DELETE FROM users WHERE name = 'Jane'")
#conn.commit()

#fecha a conexão
conn.close()