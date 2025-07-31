import tkinter
from tkinter import messagebox

def submit():
    # Recupera os dados dos campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    # Verifica qual radiobutton está selecionado
    linguagem_preferida = linguagem_var.get()

    #Imprime os dados no console
    print("Nome: ", nome)
    print("Email: ", email)
    print("Linguagem Preferida: ", linguagem_preferida)

    # Mostra uma caixa de mensagem com os dados
    messagebox.showinfo(
        "Dados Submetidos",
        f"Nome: {nome}\nEmail: {email}\nLinguagem Preferida: {linguagem_preferida}"
    )

# Cria a janela principal
root = tkinter.Tk()
root.title("Formulário de Inscrição")

# Cria um frame para conter os widgets
frame = tkinter.Frame(root)
frame.pack(padx=10, pady=10)

# Label para o campo "Nome"
nome_label = tkinter.Label(frame, text="Nome:")
nome_label.grid(row=0, column=0, sticky="e")

# Campo de entrada para "Nome"
nome_entry = tkinter.Entry(frame)
nome_entry.grid(row=0, column=1)

# Label para o campo "Email"
email_label = tkinter.Label(frame, text="Email:")
email_label.grid(row=1, column=0, sticky="e")

# Campo de entrada para "Email"
email_entry = tkinter.Entry(frame)
email_entry.grid(row=1, column=1)

# Variável para armazenar a escolha de linguagem
linguagem_var = tkinter.StringVar(value="Python")

# Radiobutton para "Python"
python_radio = tkinter.Radiobutton(frame, text="Python", variable=linguagem_var, value="Python")
python_radio.grid(row=2, column=0)

# Radiobutton para "Java"
java_radio = tkinter.Radiobutton(frame, text="Java", variable=linguagem_var, value="Java")
java_radio.grid(row=2, column=1)

# Botão de submissão
submit_button = tkinter.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

# Inicializa o loop da Gui
root.mainloop()