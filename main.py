from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

################# cores ###############
co0 = "#2e2d2b"
co1 = "#feffff"
co4 = "#403d3d"
co9 = "#e9edf5"

class AppWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Orçamento Pessoal")
        self.master.geometry('900x650')
        self.master.configure(background=co9)
        self.master.resizable(width=False, height=False)

        # criando frames para divisao de tela
        self.frameCima = Frame(self.master, width=900, height=50, bg=co1, relief="flat")
        self.frameCima.grid(row=0, column=0)

        self.frameMeio = Frame(self.master, width=900, height=361, bg=co1, pady=20, relief="raised")
        self.frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.frameBaixo = Frame(self.master, width=900, height=300, bg=co1, relief="flat")
        self.frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

        # Trabalhando no frame de cima
        self.app_imag = Image.open('confraria do cafe.jpg')
        self.app_imag_resized = self.app_imag.resize((45, 45))
        self.app_imag_tk = ImageTk.PhotoImage(self.app_imag_resized)  # Usar a imagem redimensionada
        self.app_logo = Label(self.frameCima, image=self.app_imag_tk, text=" Orçamento pessoal", compound=LEFT, padx=5,relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
        self.app_logo.place(x=0, y=0)

        # porcentagem------------------------------

        self.porcentagem()

    def porcentagem(self):
        nome_1 = Label(self.frameMeio, text="Porcentagem da Receita gasta", height=1, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
        nome_1.place(x=7, y=5)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='#daed6b')  # Corrigindo o nome do estilo
        style.configure("TProgressbar", thickness=25)
        bar = ttk.Progressbar(self.frameMeio, length=180, style='black.Horizontal.TProgressbar')  # Usando ttk.Progressbar

        bar.place(x=10, y=35)
        bar['value'] = 50

        valor = 50

        porcentagem_1 = Label(self.frameMeio, text="{:,.2f}".format(valor), anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        porcentagem_1.place(x=200, y=35)

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

#funçao de resumo total
def resumo():
    valor = [500,600,420]
    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'),bg='#545454') # type: ignore
    l_linha.place(x=309, y=52)
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
    l_sumario.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="{:,.2f}".format(valor[2]), anchor=NW, font=('arial 17'),bg=co1, fg='#545454') # type: ignore
    l_sumario.place(x=309, y=220)

def grafico_pie():
    frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co0) # type: ignore
    frame_gra_pie.place(x=415, y=5)

frame_gra_pie = Frame(FrameMeio, width=580, height=250, bg=co2) # type: ignore
frame_gra_pie.place(x=415, y=5)

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
#.place(x=400, y=70)
# frameMeio
def main():
    janela = Tk()
    app = AppWindow(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()

