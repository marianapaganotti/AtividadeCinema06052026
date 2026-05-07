from database.db import get_connection

class FilmeRepository:

    def salvar(self, filme: dict) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO filme (titulo, diretor, genero, duracao_min, elenco)
            VALUES (?, ?, ?, ?, ?)
        """, (filme['titulo'], filme['diretor'], filme['genero'],
              filme['duracao_min'], filme.get('elenco', '')))
        conn.commit()
        fid = cursor.lastrowid
        conn.close()
        return fid

    def listar_todos(self) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM filme ORDER BY titulo")
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def buscar_por_id(self, filme_id: int) -> dict:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM filme WHERE id = ?", (filme_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None


class CinemaRepository:

    def salvar(self, cinema: dict) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cinema (nome, cidade, estado, capacidade)
            VALUES (?, ?, ?, ?)
        """, (cinema['nome'], cinema['cidade'], cinema['estado'], cinema['capacidade']))
        conn.commit()
        cid = cursor.lastrowid
        conn.close()
        return cid

    def listar_todos(self) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cinema ORDER BY nome")
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def buscar_por_id(self, cinema_id: int) -> dict:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cinema WHERE id = ?", (cinema_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
