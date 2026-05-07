from database.db import get_connection
from datetime import datetime

class IngressoRepository:

    def salvar(self, ingresso: dict) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ingresso (sessao_id, espectador_nome, tipo, preco, data_compra)
            VALUES (?, ?, ?, ?, ?)
        """, (
            ingresso['sessao_id'],
            ingresso['espectador_nome'],
            ingresso['tipo'],
            ingresso['preco'],
            ingresso.get('data_compra', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        ))
        conn.commit()
        ingresso_id = cursor.lastrowid
        conn.close()
        return ingresso_id

    def listar_por_sessao(self, sessao_id: int) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT i.*, s.data_hora, f.titulo, c.nome as cinema_nome
            FROM ingresso i
            JOIN sessao s ON s.id = i.sessao_id
            JOIN filme f ON f.id = s.filme_id
            JOIN cinema c ON c.id = s.cinema_id
            WHERE i.sessao_id = ?
        """, (sessao_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def total_por_sessao(self, sessao_id: int) -> dict:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) as total, SUM(preco) as receita
            FROM ingresso WHERE sessao_id = ?
        """, (sessao_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else {'total': 0, 'receita': 0}
