import string
import random
import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        master.title("Gerador de Senhas Fortes")
        master.geometry("300x150")
        master.resizable(False, False)

        # Define um estilo para a janela e para os widgets
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TLabel', font=('Arial', 12), foreground='#333')
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), foreground='#fff', background='#007bff')

        # Criação do Frame
        self.frame = ttk.Frame(master, padding=10)
        self.frame.pack(fill='both', expand=True)

        # Label da senha
        self.label_password = ttk.Label(self.frame, text="Senha:")
        self.label_password.pack()

        # Campo de entrada da senha
        self.entry_password = ttk.Entry(self.frame, width=30)
        self.entry_password.pack(pady=5)

        # Botão para gerar a senha
        self.button_generate = ttk.Button(self.frame, text="Gerar Senha", command=self.generate_password)
        self.button_generate.pack(pady=10)

        # Texto informativo
        self.label_info = ttk.Label(self.frame, text="Clique em 'Gerar Senha' para gerar uma senha aleatória e forte.")
        self.label_info.pack()

    def generate_password(self):
        # Define o conjunto de caracteres possíveis para a senha
        chars = string.ascii_letters + string.digits + string.punctuation

        # Define o comprimento da senha
        length = 16

        # Gera a senha aleatória
        password = ''.join(random.choice(chars) for i in range(length))

        # Define a senha no campo de entrada de texto
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, password)


root = tk.Tk()
app = App(root)
root.mainloop()
