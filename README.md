# Prova Técnica – Analista de Dados Python

## 🎯 Objetivo

Avaliar sua capacidade de:

1. Ler e processar um arquivo **CSV** com Python
2. Validar dados básicos (tipos, campos obrigatórios)
3. Salvar os dados em um **banco de dados relacional**
4. (Opcional) Criar uma **API simples** para upload/consulta
5. (Opcional) Criar **Docker** e **testes automatizados**

Não existe uma única solução certa. O que mais importa é a **organização**, **clareza** e **boas práticas**.

---

## 🧩 Parte 1 — Leitura e validação do CSV ✅ (OBRIGATÓRIO)

Crie um código em Python que:

- leia o arquivo `sample_data.csv`
- valide cada linha
- separe:
  - **registros válidos**
  - **registros inválidos** (com motivo do erro)

Validações mínimas sugeridas:

- arquivo possui o cabeçalho correto:
  id,name,email,age,salary
- `id` deve ser número inteiro
- `age` deve ser número inteiro
- `salary` deve ser número (pode ter ponto decimal)
- `name` e `email` não devem estar vazios

Requisitos:

- usar `pandas`

---

## 🧩 Parte 2 — Salvar em banco de dados ✅ (OBRIGATÓRIO)

Crie um código que grave os dados válidos em um **banco de dados relacional**.

Requisitos mínimos:

- pode usar **SQLite** (sugestão, mais simples)
- criar pelo menos:
  - uma tabela com os **registros válidos**
  - opcional: uma tabela para **registros inválidos** com o motivo do erro

Você pode usar:

- biblioteca padrão com `sqlite3`, **ou**
- ORM como `SQLAlchemy` (diferencial, não obrigatório)

---

## 🧩 Parte 3 — Estrutura do projeto ✅ (OBRIGATÓRIO)

Organize seu código em uma estrutura minimamente clara.
Sugestão (apenas exemplo):

```
project/
  ├── main.py          # ponto de entrada
  ├── csv_utils.py     # funções para ler/validar CSV
  ├── db_utils.py      # funções para salvar no banco
  └── README.md        # seu README com instruções
```

Você pode usar outra estrutura, desde que seja **organizada e fácil de entender**.

---

## 🌐 Parte 4 — API simples (OPCIONAL, DIFERENCIAL)

Se quiser, crie uma API REST simples:

- POST /upload  → recebe um arquivo CSV e processa
- GET /records  → lista registros válidos
- GET /errors   → lista registros inválidos
- GET /health   → health check

Sugestão de frameworks:

- FastAPI
- Flask

---

## 🧪 Parte 5 — Testes automatizados (OPCIONAL, DIFERENCIAL)

Se quiser mostrar mais conhecimento, inclua testes com:

- pytest ou unittest

Exemplos do que testar:

- leitura de CSV válido
- tratamento de linha inválida
- inserção no banco

---

## 🐳 Parte 6 — Docker (OPCIONAL, DIFERENCIAL)

Diferencial para o perfil júnior:

- criar Dockerfile
- opcionalmente docker-compose

---

## 📂 Arquivo de entrada

Use o arquivo fornecido neste repositório:

- sample_data.csv

Esse arquivo contém:

- linhas válidas
- linhas com erros propositalmente:
  - id duplicado
  - idade inválida (abc)
  - salário inválido (xyz)

Sua solução deve:

- processar todo o arquivo
- salvar o que for válido
- identificar e registrar o que for inválido

---

## 📦 Entrega

Você deve entregar:

- link do repositório (GitHub, GitLab, etc.)

Seu repositório deve conter:

- código-fonte
- este README.md (pode adaptar)
- o arquivo sample_data.csv

Inclua no README do seu projeto:

- como rodar o projeto
- bibliotecas necessárias
- como executar (ex.: python main.py)

Boa prova 🙂
