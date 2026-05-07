from app.controllers.controllers import (
    IngressoController, SessaoController, FilmeController, CinemaController
)

ingresso_ctrl = IngressoController()
sessao_ctrl = SessaoController()
filme_ctrl = FilmeController()
cinema_ctrl = CinemaController()


def menu_principal():
    while True:
        print("\n=== CINEMA SYSTEM ===")
        print("1. Filmes")
        print("2. Cinemas")
        print("3. Sessoes")
        print("4. Comprar Ingresso")
        print("5. Relatorio de Sessao")
        print("0. Sair")
        op = input("Opcao: ").strip()

        if op == '1':
            menu_filmes()
        elif op == '2':
            menu_cinemas()
        elif op == '3':
            menu_sessoes()
        elif op == '4':
            tela_comprar_ingresso()
        elif op == '5':
            tela_relatorio_sessao()
        elif op == '0':
            print("Encerrando.")
            break
        else:
            print("Opcao invalida.")


def menu_filmes():
    print("\n--- FILMES ---")
    print("1. Cadastrar  2. Listar")
    op = input("Opcao: ").strip()
    if op == '1':
        titulo = input("Titulo: ")
        diretor = input("Diretor: ")
        genero = input("Genero: ")
        duracao = int(input("Duracao (min): "))
        elenco = input("Elenco (opcional): ")
        res = filme_ctrl.cadastrar(titulo, diretor, genero, duracao, elenco)
        print("OK:", res['dados'] if res['sucesso'] else res['erro'])
    elif op == '2':
        filmes = filme_ctrl.listar()['dados']
        for f in filmes:
            print(f"[{f['id']}] {f['titulo']} - {f['genero']} ({f['duracao_min']}min) Dir: {f['diretor']}")


def menu_cinemas():
    print("\n--- CINEMAS ---")
    print("1. Cadastrar  2. Listar")
    op = input("Opcao: ").strip()
    if op == '1':
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        estado = input("Estado (UF): ")
        cap = int(input("Capacidade: "))
        res = cinema_ctrl.cadastrar(nome, cidade, estado, cap)
        print("OK:", res['dados'] if res['sucesso'] else res['erro'])
    elif op == '2':
        cinemas = cinema_ctrl.listar()['dados']
        for c in cinemas:
            print(f"[{c['id']}] {c['nome']} - {c['cidade']}/{c['estado']} Cap:{c['capacidade']}")


def menu_sessoes():
    print("\n--- SESSOES ---")
    print("1. Cadastrar  2. Listar  3. Sessoes por filme")
    op = input("Opcao: ").strip()
    if op == '1':
        cinema_id = int(input("ID Cinema: "))
        filme_id = int(input("ID Filme: "))
        data_hora = input("Data/Hora (YYYY-MM-DD HH:MM): ")
        sala = input("Sala: ")
        res = sessao_ctrl.cadastrar(cinema_id, filme_id, data_hora, sala)
        print("OK:", res['dados'] if res['sucesso'] else res['erro'])
    elif op == '2':
        sessoes = sessao_ctrl.listar()['dados']
        for s in sessoes:
            print(f"[{s['id']}] {s['filme']} | {s['cinema']} | {s['data_hora']} | Sala {s['sala']}")
    elif op == '3':
        filme_id = int(input("ID Filme: "))
        sessoes = sessao_ctrl.sessoes_por_filme(filme_id)['dados']
        for s in sessoes:
            print(f"[{s['id']}] {s['cinema']} - {s['cidade']} | {s['data_hora']} | Sala {s['sala']}")


def tela_comprar_ingresso():
    print("\n--- COMPRAR INGRESSO ---")
    sessoes = sessao_ctrl.listar()['dados']
    for s in sessoes:
        print(f"[{s['id']}] {s['filme']} | {s['cinema']} | {s['data_hora']}")
    sessao_id = int(input("ID da Sessao: "))
    nome = input("Seu nome: ")
    tipo = input("Tipo (inteira/meia): ").strip().lower()
    res = ingresso_ctrl.comprar(sessao_id, nome, tipo)
    if res['sucesso']:
        d = res['dados']
        print(f"\n=== INGRESSO CONFIRMADO ===")
        print(f"Filme   : {d['filme']}")
        print(f"Cinema  : {d['cinema']}")
        print(f"Sessao  : {d['data_hora']} | Sala {d['sala']}")
        print(f"Nome    : {d['espectador']}")
        print(f"Tipo    : {d['tipo']}")
        print(f"Preco   : R$ {d['preco']:.2f}")
        print(f"ID      : #{d['id']}")
    else:
        print("ERRO:", res['erro'])


def tela_relatorio_sessao():
    print("\n--- RELATORIO DE SESSAO ---")
    sessao_id = int(input("ID da Sessao: "))
    res = ingresso_ctrl.relatorio_sessao(sessao_id)
    if res['sucesso']:
        d = res['dados']
        print(f"Filme   : {d['sessao']['filme']}")
        print(f"Cinema  : {d['sessao']['cinema']}")
        print(f"Data    : {d['sessao']['data_hora']}")
        print(f"Total   : {d['total_ingressos']} ingressos")
        print(f"Receita : R$ {d['receita_total']:.2f}")
    else:
        print("ERRO:", res['erro'])
