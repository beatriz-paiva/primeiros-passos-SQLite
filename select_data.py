import sqlite3
from create_table import DB_FILE, TABLE_NAME

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

COMMAND_NAME = "DELETE"
COLUMNS = ("id, usuario, nome_maquina, ip_maquina")

COLUMN_NAME = 'usuario'
content_column = "Beatriz Paiva"

sql = (f'''
       SELECT FROM {TABLE_NAME} WHERE {COLUMN_NAME} = ?
       '''
)

# sql = (f'''
#        DELETE FROM {TABLE_NAME} WHERE {COLUMN_NAME} = ? 
#        '''
# )

#sql = (f'''
#       UPDATE {TABLE_NAME} SET usuario = "beatriz costa" WHERE {COLUMN_NAME} = ? 
#       '''
#)

cursor.execute(sql, [content_column])

# pegar todos - usar o fectchall()
# for row in cursor.fetchall():
    
#     id, usuario, nome_maquina, ip_maquina, inicio, fim, reu, juiz, num_proc, resultado, resultado_enviado = row
#     #só funciona se todas as tuplas estiverem com algo
#     print(id, usuario, nome_maquina, ip_maquina, inicio, fim, reu, juiz, num_proc, resultado, resultado_enviado)

for row in cursor.fetchall():
    print(row)

conn.commit()

cursor.close()
conn.close()