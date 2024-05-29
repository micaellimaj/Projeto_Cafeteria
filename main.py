from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
#from view import inserir_produto
from datetime import datetime
import mysql.connector

################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

################# criando janela ###############

root = tk.Tk()
root.title("Formulário de Inserção de Produto")
root.geometry('900x650')
root.configure(background=co9)
root.resizable(width=FALSE, height=FALSE)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9))

# ----------------------------- Frames ---------------------------------------#


frameCima = Frame(root, width=1043, height=50, bg=co1,  relief="flat",)
frameCima.grid(row=0, column=0)

# Frame para inserção de produtos (frameInserirProdutos)
frameInserirProdutos = Frame(root, width=600, height=200, bg=co2, relief="flat",background=co9)
frameInserirProdutos.grid(row=1, column=0, padx=200, pady=20, sticky=W)


# ---------------------------- imagem(LOGO)  -------------------------------- #
app_img  = Image.open('confraria_do_cafe.jpg')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" GESTÃO DE ESTOQUE", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )

app_logo.place(x=0, y=0)

# ------------------ CONEXÃO COM BANCO DE DADOS -------------------------- #

def inserir_click():
    nome_produto = entry_produto.get()
    categoria = entry_categoria.get()
    ncm = entry_ncm.get()
    estoque = entry_estoque.get()
    custo = entry_custo.get()
    data = entry_data.get()
    und = entry_und.get()
    
    # Convertendo a data para o formato correto
    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    
    # Estabelecendo conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kate1929@",
        database="bdestoque"
    )
    
    cursor = conexao.cursor()
    
    # Criando a instrução SQL com marcadores de posição
    comando = 'INSERT INTO produtos (nome_produto, categoria, ncm, estoque, custo, data, und) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    
    # Criando a tupla com os valores
    valores = (nome_produto, categoria, ncm, estoque, custo, data_formatada, und)
    
    # Executando o comando SQL
    cursor.execute(comando, valores)
    
    # Salvando as alterações no banco de dados
    conexao.commit()
    
    # Fechando o cursor e a conexão
    cursor.close()
    conexao.close()

# -------------------------- FORMULÁRIO -------------------------- #

# Criando os widgets
tk.Label(frameInserirProdutos, text="nome_produto:").grid(row=0, column=0)
entry_produto = tk.Entry(frameInserirProdutos, width=50)
entry_produto.grid(row=0, column=1)

tk.Label(frameInserirProdutos, text="Categoria:").grid(row=1, column=0)
entry_categoria = tk.Entry(frameInserirProdutos, width=50)
entry_categoria.grid(row=1, column=1)

tk.Label(frameInserirProdutos, text="NCM:").grid(row=2, column=0)
entry_ncm = tk.Entry(frameInserirProdutos, width=50)
entry_ncm.grid(row=2, column=1)

tk.Label(frameInserirProdutos, text="Estoque:").grid(row=3, column=0)
entry_estoque = tk.Entry(frameInserirProdutos, width=50)
entry_estoque.grid(row=3, column=1)


tk.Label(frameInserirProdutos, text="Custo:").grid(row=4, column=0)
entry_custo = tk.Entry(frameInserirProdutos, width=50)
entry_custo.grid(row=4, column=1)

tk.Label(frameInserirProdutos, text="Data: ").grid(row=5, column=0)
entry_data = tk.Entry(frameInserirProdutos, width=50)
entry_data.grid(row=5, column=1)

tk.Label(frameInserirProdutos, text="Unidade:").grid(row=6, column=0)
entry_und = tk.Entry(frameInserirProdutos, width=50)
entry_und.grid(row=6, column=1)


btn_inserir = tk.Button(frameInserirProdutos, width=50, text="Inserir", command=inserir_click)
btn_inserir.grid(row=7, column=0, columnspan=2, pady=10)



# Iniciando o loop principal da aplicação
root.mainloop()