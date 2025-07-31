from conectar import conexao, meu_cursor

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