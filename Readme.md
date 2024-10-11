# Lista de Tarefas (TO-DO List)

Este é um aplicativo de Lista de Tarefas (TO-DO List) desenvolvido em Python com interface gráfica utilizando CustomTkinter e banco de dados MySQL. O objetivo do aplicativo é permitir que os usuários gerenciem suas tarefas de forma eficiente, com a possibilidade de adicionar, editar, excluir e marcar tarefas como concluídas. Todas as tarefas são armazenadas de forma persistente em um banco de dados.
Funcionalidades

    Adicionar Tarefas: O usuário pode criar novas tarefas, definindo um título e uma descrição.
    Editar Tarefas: É possível editar o título e a descrição de uma tarefa existente.
    Excluir Tarefas: O usuário pode excluir uma tarefa da lista.
    Marcar como Concluída: O usuário pode marcar uma tarefa como concluída, e o status será atualizado no banco de dados.
    Persistência de Dados: Todas as tarefas são armazenadas em um banco de dados MySQL, garantindo que os dados sejam preservados mesmo após o encerramento do aplicativo.

## Pré-requisitos

Antes de executar o projeto, você precisará ter instalado:

    Python 3.x
    CustomTkinter
    MySQL Server
    MySQL Connector para Python

## Instalação

Clone o repositório

Instale as dependências:

bash

pip install customtkinter mysql-connector-python

Configuração do Banco de Dados:

Crie o banco de dados e a tabela utilizando o script SQL fornecido:

sql

CREATE DATABASE IF NOT EXISTS todo_list;

USE todo_list;

CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    status ENUM('pendente', 'concluida') DEFAULT 'pendente',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Além disso, configure suas credenciais de banco de dados no código, na função conectar_banco:

python

    conexao = mysql.connector.connect(
        host="localhost",
        user="Usuario",  # Substitua pelo seu usuário
        password="Senha",  # Substitua pela sua senha
        database="todo_list"
    )

## Executando o Projeto

Para rodar o aplicativo, execute o arquivo principal do projeto com o comando abaixo:

bash

python todo_list.py

Isso abrirá a interface gráfica onde você poderá gerenciar suas tarefas.


## Imagens

![Screenshot (641)](https://github.com/user-attachments/assets/d7e3c24b-18f4-4641-9b03-dbafbc66ccb6)
![Screenshot (642)](https://github.com/user-attachments/assets/44f57121-00ca-4901-9a82-fd13cdebd44a)


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
Licença

Este projeto é licenciado sob a MIT License.
