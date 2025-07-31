import tkinter as tk
from tkinter import ttk
from AppBD import AppBD

class PrincipalBD:
    def __init_(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Gestão de Produtos")

        #Componentes da Interface Gráfica
        self.lblCodigo = tk.Label(root, text="Código")
        self.lblCodigo.grid(row=0, column=0)
        self.txtCodigo = tk.Entry(root)
        self.txtCodigo.grid(row=0, column=1)

        self.lblNome = tk.Label(root, text="Nome")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblPreco = tk.Label(root, text="Preco")
        self.lblPreco.grid(row=2, column=0)
        self.txtPreco = tk.Entry(root)
        self.txtPreco.grid(row=2, column=1)

        self.btnCadastrar = tk.Button(root, text="Cadastrar", command=self.fCadastrarProduto)
        self.btnCadastrar.grid(row=3, column=0)
        self.btnAtualizar = tk.Button(root, text="Atualizar", command=self.fAtualizarProduto)
        self.btnAtualizar.grid(row=3, column=1)
        self.btnExcluir = tk.Button(root, text="Excluir", command=self.fExcluirProduto)
        self.btnExcluir.grid(row=4, column=0)
        self.btnLimpar = tk.Button(root, text="Limpar", command=self.fLimparTela)
        self.btnLimpar.grid(row=4, column=1)

        self.tree = ttk.Treeview(root, columns=("CODIGO", "NOME", "PRECO"), show="headings")
        self.tree.heading("CODIGO", text="Código")
        self.tree.heading("NOME", text="Nome")
        self.tree.heading("PRECO", text="Preço")
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.bind("<ButtonRelease-1>", self.apresentarRegistrosSelecionados)

        self.carregarDadosIniciais()

    def fCadastrarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.inserir_dados(nome, preco)
        self.tree.insert("", "end", values=(codigo, nome, preco))
        self.fLimparTela()

    def fAtualizarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.atualizar_dados(codigo, nome, preco)
        self.fLimparTela()
        self.carregarDadosIniciais()

    def fExcluirProduto(self):
        codigo = self.txtCodigo.get()
        self.db.excluir_dados(codigo)
        self.fLimparTela()
        self.carregarDadosIniciais()

    def fLimparTela(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)

    def apresentarRegistrosSelecionados(self, event):
        item = self.tree.selection()[0]
        valores = self.tree.item(item, "values")
        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.insert(tk.END, valores[0])
        self.txtNome.delete(0, tk.END)
        self.txtNome.insert(tk.END, valores[1])
        self.txtPreco.delete(0, tk.END)
        self.txtPreco.insert(tk.END, valores[2])

    def carregarDadosIniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        registros = self.db.selecionar_dados()
        for registro in registros:
            self.tree.insert("", "end", values=registro)

#Criando a Interface Gráfica
root = tk.Tk()
app_bd = AppBD()
app_gui = PrincipalBD(root, app_bd)
root.mainloop()