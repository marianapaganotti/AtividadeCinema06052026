import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'cinema.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS cinema (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS filme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            diretor TEXT NOT NULL,
            genero TEXT NOT NULL,
            duracao_min INTEGER NOT NULL,
            elenco TEXT
        );

        CREATE TABLE IF NOT EXISTS sessao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id INTEGER NOT NULL,
            filme_id INTEGER NOT NULL,
            data_hora TEXT NOT NULL,
            sala TEXT NOT NULL,
            FOREIGN KEY (cinema_id) REFERENCES cinema(id),
            FOREIGN KEY (filme_id) REFERENCES filme(id)
        );

        CREATE TABLE IF NOT EXISTS ingresso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sessao_id INTEGER NOT NULL,
            espectador_nome TEXT NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('inteira', 'meia')),
            preco REAL NOT NULL,
            data_compra TEXT NOT NULL,
            FOREIGN KEY (sessao_id) REFERENCES sessao(id)
        );
    """)

    conn.commit()
    conn.close()
    print("Banco de dados inicializado.")
