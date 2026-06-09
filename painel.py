import tkinter as tk
from tkinter import messagebox, ttk

dados = []

def enviar_dados():

    confirm_nome = nome.get()
    confirm_idade = idade.get()
    confirm_estado = estado.get()

    if confirm_nome and confirm_idade and confirm_estado:

        dados.append((confirm_nome, confirm_idade, confirm_estado))

        messagebox.showinfo("Sucesso!", f"Dados Enviados e Salvo na Lista!!\n \nNome: {confirm_nome} \nIdade: {confirm_idade} \nEstado: {confirm_estado}")

        tabela.insert("", tk.END, values=(confirm_nome, confirm_idade, confirm_estado))

        nome.delete(0, tk.END)
        idade.delete(0, tk.END)
        estado.delete(0, tk.END)

    else:

        messagebox.showwarning("Aviso","Algum campo não preeenchido")

def acessar_lista():

    jan_list = tk.Tk()
    jan_list.title("LISTA")
    jan_list.geometry('600x400')

    titulo_list = tk.Label(jan_list, text="Registro", font=("Arial", 25))
    titulo_list.pack(pady=10)
    
    colunas = ("Nome", "Idade", "Estado")
    tabela_lista = ttk.Treeview(jan_list, columns=colunas, show="headings")

    tabela_lista.heading("Nome", text="Nome")
    tabela_lista.heading("Idade", text="Idade")
    tabela_lista.heading("Estado", text="Estado")

    for itens in dados:

        tabela_lista.insert("", tk.END, values=(itens))

    tabela_lista.pack(expand=True, fill=tk.BOTH)
    
janela = tk.Tk()
janela.title("Listagem de Nomes")
janela.geometry("1440x900") 
janela.configure(bg='#94CCF2')


titulo = tk.Label(janela, text="Bem vindo(a)!!", font=("Arial", 25), bg='#94CCF2')
titulo.pack(pady=10)

subtxt = tk.Label(janela, text="Insira seus dados abaixo 👇", font=("Times New Roman", 18), bg='#94CCF2')
subtxt.pack(pady=10)


tk.Label(janela, text="Nome: ", font=("Arial", 12), bg='#94CCF2').pack(pady=5)
nome = tk.Entry(janela, width=25, bg='#B0B0B0')
nome.pack(pady=10)

tk.Label(janela, text="Idade: ", font=("Arial", 12), bg='#94CCF2').pack(pady=5)
idade = tk.Entry(janela, width=25, bg='#B0B0B0')
idade.pack(pady=10)

tk.Label(janela, text="Estado:", font=("Arial", 12), bg='#94CCF2').pack(pady=5)
estado = tk.Entry(janela, width=25, bg='#B0B0B0')
estado.pack(pady=10)


botoes = tk.Frame(janela, bg='#94CCF2')
botoes.pack(pady=15)

botao = tk.Button(botoes, text="Enviar", font=("Arial", 18), bg='#12C712', command=enviar_dados)
botao.pack(side=tk.LEFT, padx=10)    

lista = tk.Button(botoes, text="Lista", font=("Arial", 18), bg='#12C712', command=acessar_lista)
lista.pack(side=tk.LEFT, padx=10)   


janela.mainloop()