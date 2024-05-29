import mysql.connector

# Conectando ao banco de dados MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kate1929@",
    database="meubanco"
)

# Criando tabela de produtos
with con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Produtos(
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descricao TEXT,
            categoria TEXT,
            NCM INT,
            Und TEXT,
            estoque INT,
            custo INT,
            data DATE
        )
    """)
# data DATE