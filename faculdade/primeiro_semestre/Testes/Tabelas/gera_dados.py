from faker import Faker
from conectar import conexao, meu_cursor

#Configurando Gerador
fake = Faker("pt_BR")

for _ in range(10):
    nome = fake.word()
    preco = round(fake.random_number(digits=5) / 100, 2)
    print(nome, preco)
    meu_cursor.execute("""
        INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)
    """, (nome, preco))

    conexao.commit()
    print("Dados inseridos com sucesso!")
    meu_cursor.close()
    conexao.close()