from tkinter import *
from tkinter import Tk, ttk

#impotando Pillow
from PIL import Image, ImageTk

# importando barra de progresso do Tlinter
from tkinter.ttk import Progressbar

#importando Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib..figure import Fihure

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

# criando frames para divisao de tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0,column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1,column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1,relief="flat")
frameBaixo.grid(row=2,column=0, pady=0,padx=10, sticky=NSEW)

# Trabalhando no frame de cima

# acessando a imagem
app_imag = Image.open('confraria do cafe.jpg')
app_imag_resized = app_imag.resize((45, 45))
app_imag_tk = ImageTk.PhotoImage(app_imag)
app_logo = Label(frameCima, image=app_imag, text=" Orçamento pessoal", width=900,compound=LEFT, padx=5,relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# percentagem------------------------------

def porcentagem():
    1_nome = Label(frameMeio, text="Porcentagem da Receita gasta", height=1,anchor=NM, font=('Verdana 12'), bg=co1, fg=co4)
    1_nome.place(x=7, y=5)

    style =ttk.style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressBar", background='#daed6b')
    style.configure("TProgressBar", thickness=25)
    bar =Progressbar(frameMeio, length=180,style=black.Horizontal.TProgressBar)

    bar.place(x=10,y=35)
    bar['value'] = 50

    valor = 50

    1_porcentagem = Label(frameMeio, text="{:,2f}%".format(valor),anchor=NM, font=('Verdana 12'), bg=co1, fg=co4)
    1_porcentagem.place(x=200, y=35)

porcentagem()

janela.mainloop()
