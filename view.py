# importando SQLite
import sqlite3 as lite
import pandas as pd
from datetime import datetime
import sys
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conectando ao banco de dados MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kate1929@",
    database="meubanco"
)



def inserir_produto(produto):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Produtos (descricao, categoria, NCM, Und, estoque, custo, data) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, produto)
        messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")


# Função para deletar produto
def deletar_produto(codigo):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Produtos WHERE codigo = %s"
        cur.execute(query, (codigo,))
        print("Produto deletado com sucesso!")



