from app.repositories.ingresso_repository import IngressoRepository
from app.repositories.sessao_repository import SessaoRepository

class IngressoService:

    def __init__(self):
        self.ingresso_repo = IngressoRepository()
        self.sessao_repo = SessaoRepository()

    def comprar_ingresso(self, sessao_id: int, espectador_nome: str, tipo: str) -> dict:
        # Regra: sessao deve existir
        sessao = self.sessao_repo.buscar_por_id(sessao_id)
        if not sessao:
            raise ValueError("Sessao nao encontrada.")

        # Regra: tipo valido
        if tipo not in ('inteira', 'meia'):
            raise ValueError("Tipo deve ser 'inteira' ou 'meia'.")

        # Regra: capacidade nao pode ser ultrapassada
        totais = self.ingresso_repo.total_por_sessao(sessao_id)
        if totais['total'] >= sessao['capacidade']:
            raise ValueError("Sessao lotada. Nao ha mais ingressos disponiveis.")

        # Regra de negocio: preco
        preco = 20.00 if tipo == 'inteira' else 10.00

        ingresso = {
            'sessao_id': sessao_id,
            'espectador_nome': espectador_nome,
            'tipo': tipo,
            'preco': preco,
        }

        ingresso_id = self.ingresso_repo.salvar(ingresso)
        return {
            'id': ingresso_id,
            'filme': sessao['filme'],
            'cinema': sessao['cinema'],
            'data_hora': sessao['data_hora'],
            'sala': sessao['sala'],
            'espectador': espectador_nome,
            'tipo': tipo,
            'preco': preco
        }

    def listar_ingressos_sessao(self, sessao_id: int) -> list:
        return self.ingresso_repo.listar_por_sessao(sessao_id)

    def relatorio_sessao(self, sessao_id: int) -> dict:
        sessao = self.sessao_repo.buscar_por_id(sessao_id)
        if not sessao:
            raise ValueError("Sessao nao encontrada.")
        totais = self.ingresso_repo.total_por_sessao(sessao_id)
        return {
            'sessao': sessao,
            'total_ingressos': totais['total'],
            'receita_total': totais['receita'] or 0
        }
