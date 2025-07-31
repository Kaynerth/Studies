import psycopg2

#Criar conexão
conexao = psycopg2.connect(
    database="postgresDB",
    user="admin",
    password="admingamer",
    host="127.0.0.1",
    port="5432"
)

print("Conexão com o Banco de Dados aberta com sucesso!")

#Criação do Cursor
meu_cursor = conexao.cursor()