CREATE DATABASE `forumweb-db`
USE `forumweb-db`;

CREATE TABLE postagens (
  id INT NOT NULL,
  titulo VARCHAR(255) NOT NULL,
  resumo VARCHAR(255) NOT NULL,
  conteudo VARCHAR(255) NOT NULL,
  autor VARCHAR(120) NOT NULL,
  PRIMARY KEY (id)
)

INSERT INTO postagens VALUES (
    2,
    'Primeira postagem',
    'Resumo da primeira postagem',
    'Conteúdo completo da primeira postagem',
    'Aluno'
);

SELECT * FROM postagens;