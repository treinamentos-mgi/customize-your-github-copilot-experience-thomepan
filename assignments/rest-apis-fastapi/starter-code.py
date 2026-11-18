# Código Inicial para a Atividade de REST APIs com FastAPI

# Execute com: uvicorn starter_code:app --reload
# Documentação interativa: http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Tarefa 1: Criar a Primeira Rota
# Implemente GET / e GET /tarefas

tarefas = []


# Tarefa 2: Receber Dados com Rotas POST e Path Parameters
# Defina o modelo Tarefa e implemente POST /tarefas e GET /tarefas/{id}

# class Tarefa(BaseModel):
#     titulo: str
#     concluida: bool = False


# Tarefa 3: Atualizar e Remover Recursos
# Implemente PUT /tarefas/{id} e DELETE /tarefas/{id}
