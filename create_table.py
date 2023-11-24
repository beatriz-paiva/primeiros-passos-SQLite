import sqlite3

from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'controle_execucao.db'
DB_FILE = ROOT_DIR/DB_NAME
TABLE_NAME = 'teste'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'usuario VARCHAR(255) NOT NULL,'
    'nome_maquina VARCHAR(255) NOT NULL,'
    'ip_maquina VARCHAR(255) NOT NULL,'
    'inicio DATETIME,'
    'fim DATETIME,'
    'reu VARCHAR(255),'
    'juiz VARCHAR(255),'
    'num_proc VARCHAR(255),'
    'resultado VARCHAR(255),'
    'resultado_enviado VARCHAR(255)'
    ')'
)

conn.commit()

cursor.close()
conn.close()