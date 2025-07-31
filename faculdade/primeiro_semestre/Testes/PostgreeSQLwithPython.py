import psycopg2
from psycopg2 import Error

def connect_to_db():
    try:
        #Conectar ao Banco de Dados
        connection = psycopg2.connect(
            host="localhost",
            database="postgresDB",
            user="admin",
            password="admingamer"
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao Banco de Dados PostgreeSQL: {e}")
        return None
    
def create_contact(nome, telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO public."AGENDA" (nome, telefone)
            VALUES (%s, %s) RETURNING id;
            """, (nome, telefone))
            contact_id = cursor.fetchone()[0]
            conn.commit()
            print(f"Contato adicionado com ID: {contact_id}")
        except Error as e:
            print(f"Erro ao adicionar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def read_contacts():
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(
            """SELECT id, nome, telefone FROM public."AGENDA";
            """)
            contacts = cursor.fetchall()
            for contact in contacts:
                print(f"ID: {contact[0]}, Nome: {contact[1]}, Telefone: {contact[2]}")
        except Error as e:
            print(f"Erro ao ler contatos: {e}")
        finally:
            cursor.close()
            conn.close()

def update_contact(contact_id, novo_nome, novo_telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            UPDATE public."AGENDA"
            SET nome = %s, telefone = %s
            WHERE id = %s;
            """, (novo_nome, novo_telefone, contact_id))
            conn.commit()
            print("Contato atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_contact(contact_id):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            DELETE FROM public."AGENDA"
            WHERE id = %s;
            """, (contact_id))
            conn.commit()
            print("Contato deletado com sucesso.")
        except Error as e:
            print(f"Erro ao deletar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def main():
    print("3. Atualizar um contato")
    print("4. Deletar um contato")
    print("5. Sair")
    choice = input("Escolha uma opção: ")

    # A partir do Python 3.10 é possível utilizar o match/case
    if choice == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        create_contact(nome, telefone)
    elif choice == "2":
        read_contacts()
    elif choice == "3":
        contact_id = int(input("Digite o ID do contato para atualizar: "))
        novo_nome = input("Nome nome: ")
        novo_telefone = input("Novo telefone: ")
        update_contact(contact_id, novo_nome, novo_telefone)
    elif choice == "4":
        contact_id = int(input("Digite o ID do contato para deletar: "))
        delete_contact(contact_id)
    elif choice == "5":
        print("Saindo...")
    else:
        print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()