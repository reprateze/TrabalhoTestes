# 📝 Task Manager – Testes Automatizados (2025/2)

Projeto desenvolvido para a disciplina **Gestão da Qualidade**, com foco em **testes automatizados unitários** e aplicação completa do fluxo **GitFlow**.

O objetivo é implementar uma aplicação simples de gerenciamento de tarefas e garantir sua qualidade por meio de testes unitários usando **Pytest**.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Pytest** (framework de testes)
- **Git + GitFlow** (controle de versionamento)
- **Dataclasses** (estrutura da entidade Task)

---

## 📌 Estrutura do Projeto

src/
└── task_manager/
├── models.py # Classe Task (domínio)
└── manager.py # Lógica de negócio (CRUD, validações)

tests/
└── test_manager.py # Testes unitários automatizados


---

## 📦 Domínio da Aplicação

A aplicação é um **gerenciador de tarefas simples**, contendo:

### ✔ Classe `Task`
- `id`
- `title`
- `description`
- `due_date`
- `completed`

### ✔ Classe `TaskManager`
Funcionalidades implementadas:

- Adicionar tarefa (`add_task`)
- Obter tarefa por ID (`get_task`)
- Remover tarefa (`remove_task`)
- Editar tarefa (`edit_task`)
- Marcar como concluída (`complete_task`)
- Listar pendentes (`list_pending`)
- Listar concluídas (`list_completed`)
- Validações:
  - ID e título obrigatórios
  - Não permitir duplicadas
  - Validar tipo da data
  - Exceções personalizadas

---

## 🧪 Testes Implementados (Pytest)

O projeto contém **08 testes unitários**, cobrindo:

| Teste | Descrição |
|-------|-----------|
| `test_add_task_success` | Verifica se adiciona uma tarefa corretamente |
| `test_add_task_missing_fields_raises` | Garante erro quando campos obrigatórios faltam |
| `test_add_duplicate_task_raises` | Evita adicionar tarefas duplicadas |
| `test_remove_task_success` | Remove tarefa com sucesso |
| `test_remove_nonexistent_raises` | Exceção ao remover ID inexistente |
| `test_complete_task_marks_completed` | Marca tarefa como concluída |
| `test_list_pending_and_completed` | Separa tarefas pendentes e concluídas |
| `test_edit_task_success_and_validation` | Edita tarefa e valida campos |
| `test_due_date_type_validation` | Garante tipo correto de data |
| `test_get_nonexistent_raises` | Exceção ao buscar ID inexistente |

---

## ▶️ Como Executar os Testes

1. Instale as dependências:
```bash
pip install pytest

pytest -v

🔀 Fluxo de Versionamento – GitFlow

O projeto segue rigorosamente o modelo GitFlow, utilizando:

main → versão estável

develop → desenvolvimento contínuo

feature/* → desenvolvimento de funcionalidades

feature/models

feature/manager

feature/tests

release/1.0.0 → preparação final da versão

tags → marcação da versão

v1.0.0

Todos os commits possuem mensagens claras e descritivas.

📄 Versão Final

Este projeto corresponde à Release 1.0.0, contendo:

Implementação completa das classes

Testes automatizados verificando todas as regras

Fluxo GitFlow seguido corretamente

Documentação do projeto