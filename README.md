# Projeto Forum Web

Aplicacao web simples de forum feita com FastAPI, templates HTML e MySQL.

## Tecnologias

- Python
- FastAPI
- Jinja2
- MySQL
- mysql-connector-python

## Estrutura do projeto

- app.py: rotas HTTP e renderizacao das telas
- model.py: operacoes de CRUD na tabela postagens
- dao.py: conexao com o banco MySQL
- templates/: paginas HTML
- static/: CSS, JS e imagens

## Pre-requisitos

- Python 3.10+
- MySQL Server ativo
- Pip

## 1. Criar banco de dados

No MySQL, execute:

```sql
CREATE DATABASE IF NOT EXISTS `forumweb-db`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE `forumweb-db`;

CREATE TABLE IF NOT EXISTS postagens (
  id INT NOT NULL,
  titulo VARCHAR(255) NOT NULL,
  resumo TEXT NOT NULL,
  conteudo LONGTEXT NOT NULL,
  autor VARCHAR(120) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 2. Configurar conexao com banco

A conexao atual esta em dao.py com estes valores:

- host: localhost
- porta: 3306
- user: root
- password: (vazia)
- database: forumweb-db

Se seu MySQL estiver em outra porta (exemplo: 3308), altere a linha port em dao.py.

## 3. Instalar dependencias

No terminal, dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

## 4. Rodar a aplicacao

```bash
fastapi dev app.py
```

## 5. Abrir no navegador

- Home: http://127.0.0.1:8000/
- Criar: http://127.0.0.1:8000/create
- Editar: http://127.0.0.1:8000/edit
- Deletar: http://127.0.0.1:8000/del

## Inserir um registro de teste

```sql
INSERT INTO postagens VALUES (
  1,
  'Primeira postagem',
  'Resumo da primeira postagem',
  'Conteudo completo da primeira postagem',
  'Aluno'
);
```

## Observacoes importantes

- O campo id e informado manualmente pelo formulario. Ele nao e AUTO_INCREMENT.
- Se a conexao falhar, confirme se o MySQL esta rodando e se host/porta/user/senha em dao.py estao corretos.
- Se a porta estiver fechada, teste no PowerShell:

```powershell
Test-NetConnection localhost -Port 3306
```
