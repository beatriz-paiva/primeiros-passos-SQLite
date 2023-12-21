import sqlite3
from create_table import DB_FILE, TABLE_NAME

usuario = "Beatriz Paiva"
nome_maquina = "ahhhhh"
ip_maquina = "192.456.45.1"
inicio= "NULL"
fim= "NULL"
reu= "NULL"
juiz= "NULL" 
num_proc= "NULL"
resultado= "NULL"
resultado_enviado = "ok"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

sql = (f'''INSERT INTO {TABLE_NAME} (
        usuario, nome_maquina, ip_maquina,
        inicio, fim, reu, juiz, num_proc,
        resultado, resultado_enviado
    )
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
)

cursor.execute(sql, (usuario, nome_maquina, ip_maquina, inicio, fim, reu, juiz, num_proc, resultado, resultado_enviado))

conn.commit()

cursor.close()
conn.close()