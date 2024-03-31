# importando SQL Lite
import sqlite3 as lite


# %%
# Criando Conexão
con = lite.connect('cafeteria.db')

# Criando tabela de categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Criando tabela de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receita(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

# Criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")

