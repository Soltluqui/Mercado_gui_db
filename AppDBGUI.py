import tkinter as tk
import AppDB as db

class AppDBGUI(tk.Tk):  
    def __init__(self):
        super().__init__()
        self.title("AppDB GUI")
        self.resizable(False, False)
        self.geometry("400x400")
        self.selecionar_dados()
        self.botoes()
        self.inserir_dados()
        self.atualizar_dados()
        self.deletar_dados()

    def selecionar_dados(self):
        self.sel_dados = tk.Listbox(self, background="white", width=45, height=10, font=("consolas",10))
        self.sel_dados.place(relx=0.5, rely=0.75, anchor="center")
        self.button = tk.Button(self, text="Selecionar Dados", command=self.dados_on_click)
        self.button.place(relx=0.5, rely=0.1, anchor="w")

    def dados_on_click(self):
        self.sel_dados.delete(0, tk.END)
        dados = db.AppDB().selecionar_dados()
        for dado in dados:
            self.sel_dados.insert(tk.END, f"ID: {dado[0]:2} - Nome: {dado[1]:10} - Preço: {dado[2]:5}")
        
    def botoes(self):
        self.codigo_button = tk.Label(self, text="Codigo", font=("consolas", 10))
        self.codigo_button.place(relx=0.1, rely=0.1, anchor="w")
        self.entry_codigo = tk.Entry(self, text="Dados", font=("consolas", 10), width=10)
        self.entry_codigo.place(relx=0.25, rely=0.1, anchor="w")

        self.nome_button = tk.Label(self, text="Nome", font=("consolas", 10))
        self.nome_button.place(relx=0.1, rely=0.2, anchor="w")
        self.entry_nome = tk.Entry(self, text="Dados2", font=("consolas", 10), width=10)
        self.entry_nome.place(relx=0.25, rely=0.2, anchor="w")
        
        self.preco_button = tk.Label(self, text="Preço", font=("consolas", 10))
        self.preco_button.place(relx=0.1, rely=0.3, anchor="w")
        self.entry_preco = tk.Entry(self, text="Dados3", font=("consolas", 10), width=10)
        self.entry_preco.place(relx=0.25, rely=0.3, anchor="w")

    def inserir_dados(self):
        self.inserir_button = tk.Button(self, text="Inserir Dados", command=self.inserir_on_click)
        self.inserir_button.place(relx=0.5, rely=0.2, anchor="w")

    def inserir_on_click(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        db.AppDB().inserir_dados(nome, preco)
        self.dados_on_click()

    def atualizar_dados(self):
        self.inserir_button = tk.Button(self, text="Atualizar Dados", command=self.atualizar_on_click)
        self.inserir_button.place(relx=0.5, rely=0.3, anchor="w")

    def atualizar_on_click(self):
        codigo = self.entry_codigo.get()
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        db.AppDB().atualizar_dados(codigo, nome, preco)
        self.dados_on_click()

    def deletar_dados(self):
        self.inserir_button = tk.Button(self, text="Deletar Dados", command=self.deletar_on_click)
        self.inserir_button.place(relx=0.5, rely=0.4, anchor="w")

    def deletar_on_click(self):
        codigo = self.entry_codigo.get()
        db.AppDB().deletar_dados(codigo)
        self.dados_on_click()

if __name__ == "__main__":
    app = AppDBGUI()
    app.mainloop()
