# importando SQLite
import sqlite3 as lite
import pandas as pd
from datetime import datetime
import sys
import tkinter as tk
from tkinter import messagebox

# Criando conexao
con = lite.connect('dados.db')

def inserir_produto(produto):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Produtos (descricao, categoria, NCM, Und, estoque, custo, data) VALUES (?,?,?,?,?,?,?)"
        cur.execute(query, produto)
        messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")

# Função para lidar com o clique do botão 'Inserir'


# Função para deletar produto
def deletar_produto(codigo):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Produtos WHERE codigo = ?"
        cur.execute(query, (codigo,))



