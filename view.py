# importando SQLite
import sqlite3 as lite
import pandas as pd
from datetime import datetime
import sys

# Criando conexao
con = lite.connect('dados.db')

def inserir_produto(produto):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Produtos (descricao, categoria, NCM, Und, estoque, custo, data) VALUES (?,?,?,?,?,?,?)"
        cur.execute(query, produto)

# Função para deletar produto
def deletar_produto(codigo):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Produtos WHERE codigo = ?"
        cur.execute(query, (codigo,))



