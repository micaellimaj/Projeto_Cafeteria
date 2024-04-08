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

        # percentagem------------------------------

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

def main():
    janela = Tk()
    app = AppWindow(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()
