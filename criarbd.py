# importando SQL Lite
import sqlite3 as lite

# Criando Conexão

# Criando Conexão
con = lite.connect('dados.db')

# Criando tabela de produtos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Produtos(codigo INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT, categoria TEXT, NCM INTEGER, Und TEXT, estoque INTEGER, custo INTEGER, data DATE)")
