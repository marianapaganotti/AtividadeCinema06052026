from app.services.ingresso_service import IngressoService
from app.services.outros_services import SessaoService, FilmeService, CinemaService

class IngressoController:

    def __init__(self):
        self.service = IngressoService()

    def comprar(self, sessao_id, espectador_nome, tipo):
        try:
            resultado = self.service.comprar_ingresso(sessao_id, espectador_nome, tipo)
            return {'sucesso': True, 'dados': resultado}
        except ValueError as e:
            return {'sucesso': False, 'erro': str(e)}

    def relatorio_sessao(self, sessao_id):
        try:
            return {'sucesso': True, 'dados': self.service.relatorio_sessao(sessao_id)}
        except ValueError as e:
            return {'sucesso': False, 'erro': str(e)}


class SessaoController:

    def __init__(self):
        self.service = SessaoService()

    def cadastrar(self, cinema_id, filme_id, data_hora, sala):
        try:
            return {'sucesso': True, 'dados': self.service.cadastrar_sessao(cinema_id, filme_id, data_hora, sala)}
        except ValueError as e:
            return {'sucesso': False, 'erro': str(e)}

    def listar(self):
        return {'sucesso': True, 'dados': self.service.listar_sessoes()}

    def sessoes_por_filme(self, filme_id):
        return {'sucesso': True, 'dados': self.service.sessoes_por_filme(filme_id)}


class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def cadastrar(self, titulo, diretor, genero, duracao_min, elenco=''):
        try:
            return {'sucesso': True, 'dados': self.service.cadastrar_filme(titulo, diretor, genero, duracao_min, elenco)}
        except ValueError as e:
            return {'sucesso': False, 'erro': str(e)}

    def listar(self):
        return {'sucesso': True, 'dados': self.service.listar_filmes()}


class CinemaController:

    def __init__(self):
        self.service = CinemaService()

    def cadastrar(self, nome, cidade, estado, capacidade):
        try:
            return {'sucesso': True, 'dados': self.service.cadastrar_cinema(nome, cidade, estado, capacidade)}
        except ValueError as e:
            return {'sucesso': False, 'erro': str(e)}

    def listar(self):
        return {'sucesso': True, 'dados': self.service.listar_cinemas()}
