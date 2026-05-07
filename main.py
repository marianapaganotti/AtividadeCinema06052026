import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database.db import init_db
from app.views.cli_view import menu_principal
from app.controllers.controllers import FilmeController, CinemaController, SessaoController

def seed():
    """Popula banco com dados iniciais para demonstracao."""
    fc = FilmeController()
    cc = CinemaController()
    sc = SessaoController()

    if not fc.listar()['dados']:
        fc.cadastrar("Oppenheimer", "Christopher Nolan", "Drama", 180, "Cillian Murphy, Emily Blunt")
        fc.cadastrar("Guardioes da Galaxia 3", "James Gunn", "Acao", 150, "Chris Pratt, Zoe Saldana")
        fc.cadastrar("Barbie", "Greta Gerwig", "Comedia", 114, "Margot Robbie, Ryan Gosling")

    if not cc.listar()['dados']:
        cc.cadastrar("Cinemark Paulista", "Sao Paulo", "SP", 200)
        cc.cadastrar("UCI Campinas", "Campinas", "SP", 150)

    if not sc.listar()['dados']:
        sc.cadastrar(1, 1, "2025-06-10 19:00", "1")
        sc.cadastrar(1, 2, "2025-06-10 21:30", "2")
        sc.cadastrar(2, 3, "2025-06-10 20:00", "1")

    print("Dados de exemplo carregados.")

if __name__ == '__main__':
    init_db()
    seed()
    menu_principal()
