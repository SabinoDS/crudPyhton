import mysql.connector

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="88888888",
  database="bdsabino",
)

cursor = conexao.cursor()

# CREATE 

nome_produto = "produto_1"
preco = 5

comando = f'INSERT INTO vendas (nome_produto, preco) VALUES ("{nome_produto}",{preco})'
cursor.execute(comando)
conexao.commit()

# READ

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() 
print(resultado) 

# UPDATE 

nome_produto = "produto_1"
preco = 10

comando = f'UPDATE vendas SET preco = {preco} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# DELETE

nome_produto = "produto_1"

comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
