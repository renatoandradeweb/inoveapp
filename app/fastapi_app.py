import os
import sys
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
import orjson

# Configura logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Adiciona o caminho da aplicação ao sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'inove')))

import django

# Configura o Django antes de importar views
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inove.settings')
django.setup()

from inove.api_views import list_posts_api, view_post_api, create_post_api, update_post_api, delete_post_api, list_users_api, user_detail_api

def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default, option=orjson.OPT_INDENT_2).decode()

app = FastAPI(default_response_class=ORJSONResponse, json_dumps=orjson_dumps)

@app.get("/api/posts")
async def get_posts():
    try:
        return list_posts_api()
    except Exception as e:
        logger.exception("Erro ao obter posts")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/posts/{post_id}")
async def get_post(post_id: int):
    try:
        # Implemente a lógica para obter os detalhes do post com o ID fornecido
        # Você pode usar a função view_post_api ou implementar a lógica diretamente aqui
        return view_post_api(post_id)
    except Exception as e:
        logger.exception("Erro ao obter detalhes do post")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/posts")
async def add_post(post_data: dict):
    try:
        return create_post_api(post_data)
    except Exception as e:
        logger.exception("Erro ao adicionar post")
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/posts/{post_id}")
async def modify_post(post_id: int, post_data: dict):
    try:
        return update_post_api(post_id, post_data)
    except Exception as e:
        logger.exception("Erro ao modificar post")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/posts/{post_id}")
async def remove_post(post_id: int):
    try:
        return delete_post_api(post_id)
    except Exception as e:
        logger.exception("Erro ao remover post")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/users")
async def get_users():
    try:
        return list_users_api()
    except Exception as e:
        logger.exception("Erro ao obter usuários")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    try:
        return user_detail_api(user_id)
    except Exception as e:
        logger.exception("Erro ao obter detalhes do usuário")
        raise HTTPException(status_code=500, detail=str(e))
