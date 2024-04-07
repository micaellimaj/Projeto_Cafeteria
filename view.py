# importando SQLite
import sqlite3 as lite

# Criando conexao
con = lite.connect('dados.db')


# funçoes de inseçao ---------------------------------------


# Iserir categoría
def inserir_categotia(i):
    with con:
        cur = cur.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query,i)

        #inserir receitas
def inserir_receitas(i):
    with con:
        cur = cur.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)
# Iserir Gastos
def inserir_gastos(i):
    with con:
        cur = cur.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)
# funçoes para deletar ---------------------------------------

# deletar receitas
def deletar_receitas(i):
    with con:
        cur = cur.cursor()
        query = "DELETE FROM Receitas WHERE id =?"
        cur.execute(query,i)
#deletar gastos
def deletar_gastos(i):
    with con:
        cur = cur.cursor()
        query = "DELETE FROM Gastos WHERE id =?"
        cur.execute(query,i)
# funçoes para ver dados ---------------------------------------

# ver categoria
def ver_categoria(i):
        lista_itens = []
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Categoria")
            linha = cur.fetchall()
            for i in linha:
                lista_itens.append(i)
        return lista_itens

print(ver_categoria())

# ver Receitas
def ver_receitas(i):
        lista_itens = []

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Receitas")
            linha = cur.fetchall()
            for i in linha:
                lista_itens.append(i)
        return lista_itens

#Ver gastos
def ver_gastos(i):
        lista_itens = []

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Gastos")
            linha = cur.fetchall()
            for i in linha:
                lista_itens.append(i)
        return lista_itens
