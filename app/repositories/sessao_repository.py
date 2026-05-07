from database.db import get_connection

class SessaoRepository:

    def salvar(self, sessao: dict) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sessao (cinema_id, filme_id, data_hora, sala)
            VALUES (?, ?, ?, ?)
        """, (sessao['cinema_id'], sessao['filme_id'], sessao['data_hora'], sessao['sala']))
        conn.commit()
        sid = cursor.lastrowid
        conn.close()
        return sid

    def listar_todas(self) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, s.data_hora, s.sala,
                   f.titulo as filme, f.duracao_min,
                   c.nome as cinema, c.cidade
            FROM sessao s
            JOIN filme f ON f.id = s.filme_id
            JOIN cinema c ON c.id = s.cinema_id
            ORDER BY s.data_hora
        """)
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def buscar_por_id(self, sessao_id: int) -> dict:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.*, f.titulo as filme, f.duracao_min, c.nome as cinema, c.capacidade
            FROM sessao s
            JOIN filme f ON f.id = s.filme_id
            JOIN cinema c ON c.id = s.cinema_id
            WHERE s.id = ?
        """, (sessao_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def listar_por_filme(self, filme_id: int) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.*, c.nome as cinema, c.cidade
            FROM sessao s
            JOIN cinema c ON c.id = s.cinema_id
            WHERE s.filme_id = ?
        """, (filme_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]
