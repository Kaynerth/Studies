import psycopg2

#Criar Conexão
conexao = psycopg2.connect(
    database="postgresDB",
    user="admin",
    password="admingamer",
    host="127.0.0.1",
    port="5432"
)

print("Conexão com o Banco de Dados aberta com sucesso")

#Criação do Cursor
meu_cursor = conexao.cursor()

if __name__ == "__main__":
    #Criação da Tabela
    meu_cursor.execute("""
        CREATE TABLE IF NOT EXISTS PRODUTO (
            CODIGO SERIAL PRIMARY KEY,
            NOME VARCHAR(100), NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL
    );
""")
    
#Just in Case
conexao.commit()
print("Tabela criada com sucesso!")
conexao.close()