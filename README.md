# Sistema de Rede de Cinemas

Projeto de Engenharia de Software – 3º Semestre ADS

## Descrição

Sistema de gerenciamento de rede de cinemas com controle de filmes, sessões e venda de ingressos.

## Arquitetura

```
View → Controller → Service → Repository → SQLite
```

## Como Executar

```bash
# Instalar Python 3.x (já vem no sistema)
python main.py
```

## Estrutura do Projeto

```
cinema/
├── main.py                          # Ponto de entrada
├── database/
│   └── db.py                        # Conexão SQLite
└── app/
    ├── views/
    │   └── cli_view.py              # Interface de terminal
    ├── controllers/
    │   └── controllers.py           # Camada de controle
    ├── services/
    │   ├── ingresso_service.py      # Regras de negócio (ingressos)
    │   └── outros_services.py       # Regras de negócio (filmes, sessões, cinemas)
    └── repositories/
        ├── ingresso_repository.py   # Persistência de ingressos
        ├── sessao_repository.py     # Persistência de sessões
        └── filme_cinema_repository.py # Persistência de filmes e cinemas
```

## Funcionalidades

- Cadastro e listagem de filmes (com diretor, gênero, elenco)
- Cadastro e listagem de cinemas (com cidade, estado, capacidade)
- Cadastro e listagem de sessões
- **Compra de ingresso** (caso de uso principal implementado completo)
- Relatório de público e receita por sessão

## Regras de Negócio

- Ingresso: inteira R$ 20,00 / meia-entrada R$ 10,00
- Sessão não pode exceder a capacidade do cinema
- Sessão e filme devem existir para compra de ingresso

## Tecnologias

- Python 3
- SQLite (sem dependências externas)

## Documentação (pasta `/docs`)

- `requisitos.docx` – Requisitos funcionais
- `casos_de_uso.docx` – Diagrama de casos de uso
- `sequencia.docx` – Diagrama de sequência

---

Desenvolvido para a disciplina de Engenharia de Software
