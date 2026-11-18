# 📘 Atividade: REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, definindo rotas para consultar, criar e atualizar recursos e validando os dados enviados pelos clientes.

## 📝 Tarefas

### 🛠️	Criar a Primeira Rota

#### Descrição
Crie uma aplicação FastAPI com uma rota `GET /` que retorna uma mensagem de boas-vindas em JSON. Em seguida, crie uma rota `GET /tarefas` que retorna a lista de tarefas armazenada em memória.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI`
- Implementar a rota `GET /` retornando um dicionário com a chave `message`
- Implementar a rota `GET /tarefas` retornando a lista de tarefas


### 🛠️	Receber Dados com Rotas POST e Path Parameters

#### Descrição
Crie uma rota `POST /tarefas` que recebe uma nova tarefa no corpo da requisição e a adiciona à lista. Crie também uma rota `GET /tarefas/{id}` que retorna uma tarefa específica pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Definir um modelo `Tarefa` com Pydantic contendo `titulo` e `concluida`
- Implementar `POST /tarefas` adicionando a tarefa com um `id` único e retornando-a
- Implementar `GET /tarefas/{id}` retornando a tarefa correspondente
- Retornar erro 404 quando a tarefa não existir


### 🛠️	Atualizar e Remover Recursos

#### Descrição
Crie as rotas `PUT /tarefas/{id}` para atualizar uma tarefa existente e `DELETE /tarefas/{id}` para removê-la. Teste todas as rotas pela documentação interativa gerada automaticamente em `/docs`.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tarefas/{id}` substituindo os dados da tarefa existente
- Implementar `DELETE /tarefas/{id}` removendo a tarefa da lista
- Retornar erro 404 nas rotas `PUT` e `DELETE` quando a tarefa não existir
- Demonstrar o funcionamento de todas as rotas pela interface em `/docs`
