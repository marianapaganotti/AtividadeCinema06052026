from app.repositories.sessao_repository import SessaoRepository
from app.repositories.filme_cinema_repository import FilmeRepository, CinemaRepository

class SessaoService:

    def __init__(self):
        self.sessao_repo = SessaoRepository()
        self.filme_repo = FilmeRepository()
        self.cinema_repo = CinemaRepository()

    def cadastrar_sessao(self, cinema_id: int, filme_id: int, data_hora: str, sala: str) -> dict:
        if not self.filme_repo.buscar_por_id(filme_id):
            raise ValueError("Filme nao encontrado.")
        if not self.cinema_repo.buscar_por_id(cinema_id):
            raise ValueError("Cinema nao encontrado.")

        sessao = {'cinema_id': cinema_id, 'filme_id': filme_id,
                  'data_hora': data_hora, 'sala': sala}
        sid = self.sessao_repo.salvar(sessao)
        return {'id': sid, **sessao}

    def listar_sessoes(self) -> list:
        return self.sessao_repo.listar_todas()

    def sessoes_por_filme(self, filme_id: int) -> list:
        return self.sessao_repo.listar_por_filme(filme_id)


class FilmeService:

    def __init__(self):
        self.filme_repo = FilmeRepository()

    def cadastrar_filme(self, titulo, diretor, genero, duracao_min, elenco='') -> dict:
        if duracao_min <= 0:
            raise ValueError("Duracao deve ser positiva.")
        filme = {'titulo': titulo, 'diretor': diretor, 'genero': genero,
                 'duracao_min': duracao_min, 'elenco': elenco}
        fid = self.filme_repo.salvar(filme)
        return {'id': fid, **filme}

    def listar_filmes(self) -> list:
        return self.filme_repo.listar_todos()


class CinemaService:

    def __init__(self):
        self.cinema_repo = CinemaRepository()

    def cadastrar_cinema(self, nome, cidade, estado, capacidade) -> dict:
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser positiva.")
        cinema = {'nome': nome, 'cidade': cidade, 'estado': estado, 'capacidade': capacidade}
        cid = self.cinema_repo.salvar(cinema)
        return {'id': cid, **cinema}

    def listar_cinemas(self) -> list:
        return self.cinema_repo.listar_todos()
