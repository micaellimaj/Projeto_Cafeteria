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
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )

app_logo.place(x=0, y=0)



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
    bar['value'] = 50

    valor = 50
    print(valor)
    l_percentagem = Label(frameMeio, text='{:,.2f} %'.format(valor), height=1,anchor=NW, font=('Verdana 12 '), bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)

percentagem()


# funçao para grafico bars
def grafico_bar():
    lista_categorias = ['Renda','Despesas','Saldo']
    lista_valores = [3000, 2000, 6236]

#faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60) # type: ignore
    ax = figura.add_subplot(111)
   # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9) # type: ignore
    #create a list to collect the plt.patches data

    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
       # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

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
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio) # type: ignore
    canva.get_tk_widget().place(x=10, y=70)

grafico_bar()

#funçao de resumo total
def resumo():
    valor = [500,600,420]
    
    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'),bg='#545454') # type: ignore
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total Renda Mensal    ".upper(), anchor=NW, font=('Verdana 12'),bg=co1, fg='#83a9e6') # type: ignore
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="{:,.2f}".format(valor[0]), anchor=NW, font=('arial 17'),bg=co1, fg='#545454') # type: ignore
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'),bg='#545454') # type: ignore
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total Despesas Mensais ".upper(), anchor=NW, font=('Verdana 12'),bg=co1, fg='#83a9e6') # type: ignore
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="{:,.2f}".format(valor[1]), anchor=NW, font=('arial 17'),bg=co1, fg='#545454') # type: ignore
    l_sumario.place(x=309, y=150)


    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'),bg='#545454') # type: ignore
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total Saldo do Caixa    ".upper(), anchor=NW, font=('Verdana 12'),bg=co1, fg='#83a9e6') # type: ignore
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="{:,.2f}".format(valor[2]), anchor=NW, font=('arial 17'),bg=co1, fg='#545454') # type: ignore
    l_sumario.place(x=309, y=220)

resumo()


#funcao grafico pie
def grafico_pie():
    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90) # type: ignore
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesas', 'Saldo']

    #only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90) # type: ignore
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie) # type: ignore
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


"""def main():
    janela = Tk()
    app = AppWindow(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()"""


# função para mostrar_renda

def mostrar_renda():
    # Criando uma treeview com barras de rolagem duplas
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
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

# configurações despesas
l_info = Label(frame_operacoes, text="Insira novas despesas", height=1,anchor=NW,relief="flat", font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

# categoria
l_categoria = Label(frame_operacoes, text="Categoria", height=1,anchor=NW,relief="flat", font=('Ivy 10'), bg=co1, fg=co4)
l_categoria.place(x=10, y=40)

# Pegando os categorias
categorias_funcao = ['viagens','comida']
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

l_valor_despesas = Label(frame_operacoes, text="Quantia Total", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_valor_despesas.place(x=10, y=100)
e_valor_despesas = Entry(frame_operacoes, width=14, justify='left',relief="solid")
e_valor_despesas.place(x=110, y=101)

# Botao Inserir
img_add_despesas  = Image.open('adicionar.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

botao_inserir_despesas = Button(frame_operacoes,image=img_add_despesas, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_inserir_despesas.place(x=110, y=131)


janela.mainloop()