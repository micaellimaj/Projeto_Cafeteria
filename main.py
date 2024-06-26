from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
#from view import inserir_produto
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkinter import simpledialog
from tkcalendar import DateEntry
from datetime import date


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
root.title("Formulário de Inserção de Produtos da Confraria do Café")
root.geometry('900x450')
root.configure(background=co9)
root.resizable(width=FALSE, height=FALSE)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9))

# ----------------------------- Frames ---------------------------------------#


# Frame para a parte superior
frameCima = tk.Frame(root, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2)  # Mantém o frameCima na parte superior e atravessa as colunas

# Frame para inserção de produtos (frameInserirProdutos), do lado direito
frameInserirProdutos = tk.Frame(root, width=600, height=200, bg=co2, relief="flat", background=co9)
frameInserirProdutos.grid(row=1, column=1, padx=20, pady=20, sticky="ew")  # Posiciona o frameInserirProdutos do lado direito

# Frame para o lado esquerdo
frameEsquerda = tk.Frame(root, width=400, height=200, bg=co1, relief="flat")
frameEsquerda.grid(row=1, column=0, padx=20, pady=20, sticky="ew")  # Posiciona o frameEsquerda do lado esquerdo

# Configurando o gerenciamento de geometria para a janela
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

# ---------------------------- imagem(LOGO)  -------------------------------- #
app_img  = Image.open('confraria_do_cafe.jpg')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" GESTÃO DE ESTOQUE", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )

app_logo.place(x=0, y=0)

# ---------------------------- imagem(cadastro)  -------------------------------- #

app_img2 = Image.open('cafeterias.jpg')
app_img2 = app_img2.resize((450, 250)) 
app_img2 = ImageTk.PhotoImage(app_img2)

app_logo2 = tk.Label(frameEsquerda, image=app_img2, bg=co1, fg=co4)
app_logo2.image = app_img2  


app_logo2.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')


# ------------------ CONEXÃO COM BANCO DE DADOS -------------------------- #

def limpar_formulario():
    entry_produto.delete(0, tk.END)  # Limpa o campo de entrada do produto
    dropdown_categoria.set(categorias[0])  # Define a categoria padrão novamente
    spinbox_unidade.delete(0, tk.END)  # Limpa o campo de entrada da unidade
    spinbox_custo.delete(0, tk.END)  # Limpa o campo de entrada do custo
    entry_data.delete(0, tk.END)  # Limpa o campo de entrada da data


def inserir_click():
    nome = entry_produto.get()
    categoria = dropdown_categoria.get()
    unidade = spinbox_unidade.get()
    custo = spinbox_custo.get()
    data = entry_data.get()
    limpar_formulario()
    
    # Estabelecendo conexão com o banco de dados


    

    # Micael:

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kate1929@",
        database="bdestoque"
    )

    # Wendel:
    
    ''''conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tuasenha",
        database="bdestoque"
    )
'''
    cursor = conexao.cursor()

    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    
    # Criando a instrução SQL com marcadores de posição
    comando = 'INSERT INTO produtos (nome, categoria, unidade, custo, data) VALUES (%s, %s, %s, %s, %s)'
    
    # Criando a tupla com os valores
    valores = (nome, categoria, unidade, custo, data_formatada)
    
    # Executando o comando SQL
    cursor.execute(comando, valores)
    
    # Salvando as alterações no banco de dados
    conexao.commit()
    
    # Fechando o cursor e a conexão
    cursor.close()
    conexao.close()

    messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")

# Função para remover um produto

def remover_produto():
    try:
        # Conectando ao banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kate1929@",
            database="bdestoque"
        )
        cursor = conexao.cursor()
        
        # Selecionando o ID do último produto inserido
        cursor.execute("SELECT MAX(idprodutos) AS ultimo_id FROM produtos")
        resultado = cursor.fetchone()
        ultimo_id = resultado[0] if resultado[0] is not None else 1
        
        # Deletando o produto com o ID encontrado
        comando = 'DELETE FROM produtos WHERE idprodutos = %s'
        cursor.execute(comando, (ultimo_id,))
        conexao.commit()
        
        cursor.close()
        conexao.close()
        
        # Informando o usuário que o produto foi removido com sucesso
        messagebox.showinfo(title="Sucesso", message=f"Último produto removido com sucesso.")
    except Exception as e:
        # Informando o usuário em caso de erro
        messagebox.showerror(title="Erro", message=str(e))
    finally:
        # Fechando a conexão com o banco de dados
        if 'cursor' in locals() or 'cursor' in globals():
            cursor.close()
        if 'conexao' in locals() or 'conexao' in globals():
            conexao.close()




# -------------------------- FORMULÁRIO -------------------------- #

# Adicionando um label para inserir o nome do produto
tk.Label(frameInserirProdutos, text="Nome:").grid(row=0, column=0)
entry_produto = tk.Entry(frameInserirProdutos, width=50)
entry_produto.grid(row=0, column=1)

# Adicionando um label e um dropdown para inserir a categoria
tk.Label(frameInserirProdutos, text="Categoria:").grid(row=1, column=0)
categorias = ["alimento", "bebida", "limpeza"]
dropdown_categoria = tk.StringVar(root)
dropdown_categoria.set(categorias[0])  # Definindo a categoria padrão
dropdown_menu = tk.OptionMenu(frameInserirProdutos, dropdown_categoria, *categorias)
dropdown_menu.config(width=44)
dropdown_menu.grid(row=1, column=1)


# Adicionando um label e um Spinbox para inserir a unidade
tk.Label(frameInserirProdutos, text="Unidade:").grid(row=3, column=0)
spinbox_unidade = tk.Spinbox(frameInserirProdutos, from_=1, to=100, width=48)
spinbox_unidade.grid(row=3, column=1)

# Adicionando um label e um Spinbox para inserir custo
tk.Label(frameInserirProdutos, text="Custo (R$):").grid(row=4, column=0)
spinbox_custo = tk.Spinbox(frameInserirProdutos, from_=1.0, to=100.0, increment=0.50, format="%.2f", width=48)
spinbox_custo.grid(row=4, column=1)

# Adicionando um label -para inserir data
tk.Label(frameInserirProdutos, text="Data: ").grid(row=5, column=0)
entry_data = tk.Entry(frameInserirProdutos, width=50)
entry_data.grid(row=5, column=1)

# Adicionando botão inserir produtos
btn_inserir = tk.Button(frameInserirProdutos, width=50, text="Inserir produtos", command=inserir_click)
btn_inserir.grid(row=7, column=0, columnspan=2, pady=10)

# Botão para remover produtos
btn_remover = tk.Button(frameInserirProdutos, width=50, text="Remover útimo produto inserido", command=remover_produto)
btn_remover.grid(row=8, column=0, columnspan=2, pady=10)

# Função para limpar o formulário
limpar_formulario()

# Iniciando o loop principal da aplicação
root.mainloop()