from tkinter import *
from tkinter import Tk, ttk

#impotando Pillow
#! pip install tkcalendar
# (instalação terminal : pip install pillow)
from PIL import Image, ImageTk

# importando barra de progresso do Tlinter
from tkinter.ttk import Progressbar

#importando Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

import sys

# importando funcoes da view (bar_valores, inserir_categoria,tabela)
from view import inserir_receita, inserir_gastos, deletar_receitas, ver_categorias, percentagem_valor, ver_gastos, deletar_gastos, inserir_categoria,bar_valores, tabela, pie_valores, ver_gastos, bar_valores,percentagem_valor
from tkinter import messagebox

################# cores ###############
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']
# criando janela
janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9))



# criando frames para divisao de tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0,column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1,column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1,relief="flat")
frameBaixo.grid(row=2,column=0, pady=0,padx=10, sticky=NSEW)

frame_gra_pie = Frame(frameMeio, width=580, height=250,bg=co2)
frame_gra_pie.place(x=415, y=5)


# Trabalhando no frame de cima

# abrindo imagem
app_img  = Image.open('confraria do cafe.jpg')
app_img = app_img.resize((65, 65))
app_img = ImageTk.PhotoImage(app_img)

# --------------------------------------------  FUNÇÕES ------------------------------



# --------------------------------------------  FUNÇÕES ------------------------------

app_logo = Label(frameCima, image=app_img, text=" Financeiro Cafeteria", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )

app_logo.place(x=0, y=0)

# definindo tree como global
global tree
# inserir categoria
def inserir_categoria_b():
    nome = e_categoria.get()

    lista_inserir = [nome]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    # passado para a função inserir gastos presente na view
    inserir_categoria(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
    e_categoria.delete(0, 'end')

    # pegando os valores de categoria
    categorias_funcao = ver_categorias()
    categoria = []
    for i in categorias_funcao:
        categoria.append(i[1])

    # atualizando a lista de categorias
    combo_categoria_despesas['values'] = (categoria)

# função inserir receitas
def inserir_receitas_b():
    nome = 'Receita'
    data = e_cal_receitas.get()
    quantia = e_valor_receitas.get()
    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # chamando a funçao inserir Receitas presente na view
    inserir_receita(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_cal_receitas.delete(0, 'end')
    e_valor_receitas.delete(0, 'end')
    


# Função inserir Despesas

def inserir_receitas_b():
    nome = combo_categoria_despesas.get()
    data = e_cal_despesas.get()
    quantia = e_valor_despesas.get()
    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # chamando a funçao inserir despesas presente na view
    inserir_gastos(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    combo_categoria_despesas.delete(0,'end')
    e_cal_despesas.delete(0, 'end')
    e_valor_despesas.delete(0, 'end')


    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

# função deletar
def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]       

        if nome =='Receita':
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')

        # atualizando dados
            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

        else:
            deletar_gastos([valor])
            messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')

        # atualizando dados
            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

    except IndexError:
        messagebox.showinfo('Erro, selecione um dos dados na tabela')

#funcao inserir receitas
def inserir_receitas_b():# parei aqui----------------------------------
    nome = 'Receita'
    data = e_cal_receitas.get()
    quantia = e_valor_receitas.get()
    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    #chamando a funcao inserir Receitas presentes na view
    inserir_receitas(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
    e_cal_receitas.delete(0, 'end')
    e_valor_receitas.delete(0, 'end')
    
    # atualizando dados
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

# percentagem------------------------------
def percentagem():
    l_nome = Label(frameMeio, text="Porcentagem da receita gasta", height=1,anchor=NW, font=('Verdana 12 '), bg=co1, fg=co4)
    l_nome.place(x=7, y=5)


    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frameMeio, length=180,style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = percentagem_valor()

    valor = percentagem_valor()
    print(valor)
    l_percentagem = Label(frameMeio, text='{:,.2f} %'.format(valor), height=1,anchor=NW, font=('Verdana 12 '), bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)

percentagem()


# funçao para grafico bars
def grafico_bar():
    lista_categorias = ['Renda','Despesas','Saldo']
    lista_valores = bar_valores()

#faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60) 
    ax = figura.add_subplot(111)
   # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    #create a list to collect the plt.patches data

    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
       # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    
# Primeiro, defina os ticks no eixo x
    ax.set_xticks(range(len(lista_categorias)))

    ax.set_xticklabels(lista_categorias,fontsize=16)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio) # type: ignore
    canva.get_tk_widget().place(x=10, y=70)

grafico_bar()

# funcao de resumo total
def resumo():

    valor =  bar_valores()

    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total lucro Mensal    ".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=35)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[0]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total Despesas Mensais".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=115)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[1]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=150)

    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Total Saldo da Caixa    ".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=190)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[2]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=220)

resumo()


#funcao grafico pie
def grafico_pie():
    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = pie_valores()[1]
    lista_categorias = pie_valores()[0]

    #only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)

    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0  , column=0)
    
grafico_pie()

# ------------- criando frames para tabelas -------------------------
frame_renda = Frame(frameBaixo, width=300, height=250,bg=co1)
frame_renda.grid(row=0,column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250,bg=co1)
frame_operacoes.grid(row=0,column=1, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250,bg=co1)
frame_configuracao.grid(row=0,column=2, padx=5)

# tabela renda mensal

app_tabela = Label(frameMeio, text="Tabela Receitas e Despesas", anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
app_tabela.place(x=5, y=309)



# função para mostrar_renda

def mostrar_renda():
    # Criando uma treeview com barras de rolagem duplas
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela()

    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # Ajusta a largura da coluna de acordo com a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostrar_renda()

# configurações despesas--------------------------------- PARTE 10
l_info = Label(frame_operacoes, text="Insira novas despesas", height=1,anchor=NW,relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

# categoria
l_categoria = Label(frame_operacoes, text="Categoria", height=1,anchor=NW,relief="flat", font=('Ivy 10'), bg=co1, fg=co4)
l_categoria.place(x=10, y=40)

# Pegando os categorias
categorias_funcao = ver_categoria()
categorias = []

for i in categorias_funcao:
    categorias.append(i[1])

combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=10,font=('Ivy 10'))
combo_categoria_despesas['values'] = (categorias)
combo_categoria_despesas.place(x=110, y=41)

# Despesas --------------------------------

l_cal_despesas = Label(frame_operacoes, text="Data", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_cal_despesas.place(x=10, y=70)
e_cal_despesas = DateEntry(frame_operacoes, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
e_cal_despesas.place(x=110, y=71)

# Valor -------------------------------------------

l_valor_despesas = Label(frame_operacoes, text="Valor Total", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_valor_despesas.place(x=10, y=100)
e_valor_despesas = Entry(frame_operacoes, width=14, justify='left',relief="solid")
e_valor_despesas.place(x=110, y=101)

# Botao Inserir
img_add_despesas  = Image.open('adicionar.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

botao_inserir_despesas = Button(frame_operacoes, command=inserir_receitas_b, image=img_add_despesas, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_inserir_despesas.place(x=110, y=131)

# Botao Excluir -----------------------
l_n_categoria = Label(frame_operacoes, text="Excluir ação", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_n_categoria.place(x=10, y=190)

img_delete = Image.open('lixeira.png')  # Correção aqui
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

botao_deletar = Button(frame_operacoes, command= deletar_dados,image=img_delete, compound=LEFT, anchor=NW, text=" Deletar".upper(), width=80, overrelief=RIDGE, font=('ivy 7 bold'), bg=co1, fg=co0)
botao_deletar.place(x=110, y=190)  # Correção aqui

# configurações Receitas ----------------------------------- PARTE 11

l_info = Label(frame_configuracao, text="Insira novas Receitas", height=1, anchor=NW, relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)
4
# Calendario --------------------------------

l_cal_receitas = Label(frame_configuracao, text="Data", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_cal_receitas.place(x=10, y=40)
e_cal_receitas = DateEntry(frame_configuracao, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
e_cal_receitas.place(x=110, y=41)

# Valor -------------------------------------------

l_valor_receitas = Label(frame_configuracao, text="Valor Total", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_valor_receitas.place(x=10, y=70)
e_valor_receitas = Entry(frame_configuracao, width=14, justify='left',relief="solid")
e_valor_receitas.place(x=110, y=71)

# Botao Inserir
img_add_receitas  = Image.open('adicionar.png')
img_add_receitas = img_add_receitas.resize((17,17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)
botao_inserir_receitas = Button(frame_configuracao, command= inserir_receitas_b, image=img_add_receitas, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_inserir_receitas.place(x=110, y=111)

# Operação Nova Categoria ----------------------------------- 

l_info = Label(frame_configuracao, text="Categoria", height=1, anchor=NW, relief="flat", font=('Ivy 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=160)

e_categoria = Entry(frame_configuracao, width=14, justify='left',relief="solid")
e_categoria.place(x=110, y=160)

# Botao Inserir
img_add_categoria  = Image.open('adicionar.png')
img_add_categoria = img_add_categoria.resize((17,17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
botao_inserir_categoria = Button(frame_configuracao, command=inserir_categoria_b,image=img_add_categoria, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_inserir_categoria.place(x=110, y=190)

#Função controle de despesas
import tkinter as tk
from tkinter import messagebox
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Função para inserir despesas no banco de dados
def inserir_despesa():
    descricao = descricao_entry.get()
    valor = float(valor_entry.get())

    conn = sqlite3.connect('despesas.db')
    c = conn.cursor()
    c.execute("INSERT INTO despesas (descricao, valor) VALUES (?, ?)", (descricao, valor))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Despesa inserida com sucesso.")

# Função para exibir o gráfico de despesas
def exibir_grafico():
    conn = sqlite3.connect('despesas.db')
    c = conn.cursor()
    c.execute("SELECT descricao, valor FROM despesas")
    data = c.fetchall()
    conn.close()

    despesas = [row[0] for row in data]
    valores = [row[1] for row in data]

    plt.figure(figsize=(6, 4))
    plt.bar(despesas, valores)
    plt.xlabel('Despesas')
    plt.ylabel('Valor')
    plt.title('Gráfico de Despesas')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Exibir o gráfico na interface
    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Configuração da interface gráfica
window = tk.Tk()
window.title("Controle de Despesas Pessoais")

descricao_label = tk.Label(window, text="Descrição:")
descricao_label.pack()
descricao_entry = tk.Entry(window)
descricao_entry.pack()

valor_label = tk.Label(window, text="Valor:")
valor_label.pack()
valor_entry = tk.Entry(window)
valor_entry.pack()

inserir_button = tk.Button(window, text="Inserir Despesa", command=inserir_despesa)
inserir_button.pack()

exibir_grafico_button = tk.Button(window, text="Exibir Gráfico", command=exibir_grafico)
exibir_grafico_button.pack()

window.mainloop()

#Controle de despesas pessoais
import matplotlib.pyplot as plt

def registrar_despesas():
    despesas = {}
    while True:
        data = input("Digite a data (DD/MM/AAAA) ou 'sair' para terminar: ")
        if data.lower() == 'sair':
            break
        valor = float(input("Digite o valor da despesa: "))
        despesas[data] = valor
    return despesas

def mostrar_grafico(despesas):
    datas = list(despesas.keys())
    valores = list(despesas.values())

    plt.bar(datas, valores, color='blue')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.title('Despesas Pessoais Diárias')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("Bem-vindo ao aplicativo de controle de despesas pessoais!")
    despesas = registrar_despesas()
    print("\nDespesas registradas com sucesso!")
    mostrar_grafico(despesas)

if __name__ == "__main__":
    main()

janela.mainloop ()