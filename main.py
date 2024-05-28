from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from view import inserir_produto

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

"""
janela = Tk ()
janela.title ("CONFRARIA CAFÉ")
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9)) # Modify the font of the body

"""
root = tk.Tk()
root.title("Formulário de Inserção de Produto")
root.geometry('900x650')
root.configure(background=co9)
root.resizable(width=FALSE, height=FALSE)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9))

################# Frames ####################

frameCima = Frame(root, width=1043, height=50, bg=co1,  relief="flat",)
frameCima.grid(row=0, column=0)

# Frame para inserção de produtos (frameInserirProdutos)
frameInserirProdutos = Frame(root, width=600, height=200, bg=co2, relief="flat")
frameInserirProdutos.grid(row=1, column=0, padx=200, pady=20)

"""
frameMeio = Frame(janela,width=1043, height=361,bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela,width=1043, height=300,bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

frame_gra_2 = Frame(frameMeio, width=580, height=250,bg=co2)
frame_gra_2.place(x=415, y=5)

"""

# abrindo imagem
app_img  = Image.open('confraria_do_cafe.jpg')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" GESTÃO DE ESTOQUE", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )

app_logo.place(x=0, y=0)

"""

# Labels para os campos
l_descricao = Label(frameMeio, text="Descrição:", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=10)

l_categoria = Label(frameMeio, text="Categoria:", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_categoria.place(x=10, y=40)

l_ncm = Label(frameMeio, text="NCM:", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_ncm.place(x=10, y=70)

l_und = Label(frameMeio, text="Unidade de Medida:", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_und.place(x=10, y=100)

l_estoque = Label(frameMeio, text="Estoque:", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_estoque.place(x=10, y=130)

l_custo = Label(frameMeio, text="Custo:", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_custo.place(x=10, y=160)

l_data = Label(frameMeio, text="Data:", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_data.place(x=10, y=190)

# Caixas de entrada para os campos
descricao_entry = Entry(frameMeio, width=30, font=('Verdana 10'), bg=co1, fg=co4)
descricao_entry.place(x=150, y=10)

categoria_entry = Entry(frameMeio, width=30, font=('Verdana 10'), bg=co1, fg=co4)
categoria_entry.place(x=150, y=40)

ncm_entry = Entry(frameMeio, width=30, font=('Verdana 10'), bg=co1, fg=co4)
ncm_entry.place(x=150, y=70)

und_entry = Entry(frameMeio, width=30, font=('Verdana 10'), bg=co1, fg=co4)
und_entry.place(x=150, y=100)

estoque_entry = Entry(frameMeio, width=30, font=('Verdana 10'), bg=co1, fg=co4)
estoque_entry.place(x=150, y=130)

custo_entry = Entry(frameMeio, width=30, font=('Verdana 10'), bg=co1, fg=co4)
custo_entry.place(x=150, y=160)

data_entry = Entry(frameMeio, width=30, font=('Verdana 10'), bg=co1, fg=co4)
data_entry.place(x=150, y=190)

# Função para inserir produto

# Botão para adicionar produto
botao_inserir_despesas = Button(frameMeio, text="Adicionar", command=inserir_produto, width=80, overrelief=RIDGE, font=('Verdana 7 bold'), bg=co1, fg=co0)
botao_inserir_despesas.place(x=110, y=220)


"""


def inserir_click():
    descricao = entry_descricao.get()
    categoria = entry_categoria.get()
    ncm = entry_ncm.get()
    und = entry_und.get()
    estoque = entry_estoque.get()
    custo = entry_custo.get()
    data = entry_data.get()
    
    # Verificando se todos os campos foram preenchidos
    if descricao and categoria and ncm and und and estoque and custo and data:
        produto = (descricao, categoria, ncm, und, estoque, custo, data)
        inserir_produto(produto)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
# Criando os widgets
tk.Label(frameInserirProdutos, text="Descrição:").grid(row=0, column=0)
entry_descricao = tk.Entry(frameInserirProdutos)
entry_descricao.grid(row=0, column=1)

tk.Label(frameInserirProdutos, text="Categoria:").grid(row=1, column=0)
entry_categoria = tk.Entry(frameInserirProdutos)
entry_categoria.grid(row=1, column=1)

tk.Label(frameInserirProdutos, text="NCM:").grid(row=2, column=0)
entry_ncm = tk.Entry(frameInserirProdutos)
entry_ncm.grid(row=2, column=1)

tk.Label(frameInserirProdutos, text="Unidade:").grid(row=3, column=0)
entry_und = tk.Entry(frameInserirProdutos)
entry_und.grid(row=3, column=1)

tk.Label(frameInserirProdutos, text="Estoque:").grid(row=4, column=0)
entry_estoque = tk.Entry(frameInserirProdutos)
entry_estoque.grid(row=4, column=1)

tk.Label(frameInserirProdutos, text="Custo:").grid(row=5, column=0)
entry_custo = tk.Entry(frameInserirProdutos)
entry_custo.grid(row=5, column=1)

tk.Label(frameInserirProdutos, text="Data:").grid(row=6, column=0)
entry_data = tk.Entry(frameInserirProdutos)
entry_data.grid(row=6, column=1)

btn_inserir = tk.Button(frameInserirProdutos, text="Inserir", command=inserir_click)
btn_inserir.grid(row=7, column=0, columnspan=2, pady=10)



# Iniciando o loop principal da aplicação
root.mainloop()