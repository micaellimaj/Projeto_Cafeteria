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
    categoria = dropdown_categoria.get()
    ncm = entry_ncm.get()
    estoque = spinbox_estoque.get()
    custo = spinbox_custo.get()
    data = entry_data.get()
    unidade = dropdown_unidade.get()
    
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
    valores = (nome_produto, categoria, ncm, estoque, custo, data_formatada, unidade)
    
    # Executando o comando SQL
    cursor.execute(comando, valores)
    
    # Salvando as alterações no banco de dados
    conexao.commit()
    
    # Fechando o cursor e a conexão
    cursor.close()
    conexao.close()

# -------------------------- FORMULÁRIO -------------------------- #

# Criando os widgets
tk.Label(frameInserirProdutos, text="Nome:").grid(row=0, column=0)
entry_produto = tk.Entry(frameInserirProdutos, width=50)
entry_produto.grid(row=0, column=1)

tk.Label(frameInserirProdutos, text="Categoria:").grid(row=1, column=0)
categorias = ["Alimento", "Bebida", "Limpeza"]
dropdown_categoria = tk.StringVar(root)
dropdown_categoria.set(categorias[0])  # Definindo a categoria padrão
dropdown_menu = tk.OptionMenu(frameInserirProdutos, dropdown_categoria, *categorias)
dropdown_menu.config(width=44)
dropdown_menu.grid(row=1, column=1)

tk.Label(frameInserirProdutos, text="NCM:").grid(row=2, column=0)
entry_ncm = tk.Entry(frameInserirProdutos, width=50)
entry_ncm.grid(row=2, column=1)

# Adicionando um label e um Spinbox para inserir o estoque
tk.Label(frameInserirProdutos, text="Estoque:").grid(row=3, column=0)
spinbox_estoque = tk.Spinbox(frameInserirProdutos, from_=1, to=100, width=48)
spinbox_estoque.grid(row=3, column=1)


tk.Label(frameInserirProdutos, text="Custo (R$):").grid(row=4, column=0)
spinbox_custo = tk.Spinbox(frameInserirProdutos, from_=1.0, to=100.0, increment=0.50, format="%.2f", width=48)
spinbox_custo.grid(row=4, column=1)

tk.Label(frameInserirProdutos, text="Data: ").grid(row=5, column=0)
entry_data = tk.Entry(frameInserirProdutos, width=50)
entry_data.grid(row=5, column=1)

# Adicionando um label e um dropdown para selecionar a unidade
tk.Label(frameInserirProdutos, text="Unidade:").grid(row=6, column=0)
unidades = ["FD", "UM", "UN", "LTA", "CX", "MÇ", "FD", "PTE", "CT", "PT", "GFA", "KG"]
dropdown_unidade = tk.StringVar(root)
dropdown_unidade.set(unidades[0])  # Definindo a unidade padrão
dropdown_menu_unidade = tk.OptionMenu(frameInserirProdutos, dropdown_unidade, *unidades)
dropdown_menu_unidade.config(width=44)
dropdown_menu_unidade.grid(row=6, column=1)


btn_inserir = tk.Button(frameInserirProdutos, width=50, text="Inserir", command=inserir_click)
btn_inserir.grid(row=7, column=0, columnspan=2, pady=10)



# Iniciando o loop principal da aplicação
root.mainloop()