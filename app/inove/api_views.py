from fastapi.responses import ORJSONResponse
from .models_sqlalchemy import User, Post
from .db import SessionLocal
import requests
from requests.exceptions import RequestException
from datetime import datetime

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def sync_users():
    db = next(get_db())
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()
    except RequestException as e:
        return ORJSONResponse(content={'error': f'Failed to access API: {e}'}, status_code=500)

    try:
        users = response.json()
    except ValueError as e:
        return ORJSONResponse(content={'error': f'Failed to parse JSON: {e}'}, status_code=500)

    for user_data in users:
        user = db.query(User).filter(User.id == user_data['id']).first()
        if not user:
            user = User(
                id=user_data['id'],
                name=user_data['name'],
                username=user_data['username'],
                email=user_data['email'],
                street=user_data['address']['street'],
                suite=user_data['address']['suite'],
                city=user_data['address']['city'],
                zipcode=user_data['address']['zipcode'],
                lat=user_data['address']['geo']['lat'],
                lng=user_data['address']['geo']['lng'],
                phone=user_data['phone'],
                website=user_data['website'],
                company_name=user_data['company']['name'],
                company_catch_phrase=user_data['company']['catchPhrase'],
                company_bs=user_data['company']['bs']
            )
            db.add(user)
    db.commit()

def sync_posts():
    db = next(get_db())
    user_sync_response = sync_users()  # Sincronize os usuários antes dos posts
    if isinstance(user_sync_response, ORJSONResponse):
        return user_sync_response  # Se a sincronização de usuários falhar, retorne a resposta de erro

    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
    except RequestException as e:
        return ORJSONResponse(content={'error': f'Failed to access API: {e}'}, status_code=500)

    try:
        posts = response.json()
    except ValueError as e:
        return ORJSONResponse(content={'error': f'Failed to parse JSON: {e}'}, status_code=500)

    for post_data in posts:
        post = db.query(Post).filter(Post.id == post_data['id']).first()
        if post:
            if post.deleted_at is not None or post.created_at is not None or post.updated_at is not None:
                continue
        else:
            # Se o post não existe, adicione um novo
            post = Post(
                title=post_data['title'],
                body=post_data['body'],
                user_id=post_data['userId']
            )
            db.add(post)
    db.commit()

def list_posts_api():
    sync_posts()
    db = next(get_db())
    posts = db.query(Post).filter(Post.deleted_at == None).order_by(Post.id).all()
    return ORJSONResponse(content=[post.to_dict() for post in posts])

def view_post_api(post_id):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == post_id, Post.deleted_at == None).first()
    db.close()
    if post:
        return ORJSONResponse(content=post.to_dict())
    else:
        return ORJSONResponse(content={'error': 'Post not found'}, status_code=404)
def create_post_api(post_data):
    db = next(get_db())
    new_post = Post(
        title=post_data['title'],
        body=post_data['body'],
        user_id=post_data['user_id']
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    db.close()
    return ORJSONResponse(content=new_post.to_dict())
def update_post_api(post_id, post_data):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == post_id, Post.deleted_at == None).first()
    if post:
        for key, value in post_data.items():
            setattr(post, key, value)
        db.commit()
        db.refresh(post)
        db.close()
        return ORJSONResponse(content=post.to_dict())
    db.close()
    return ORJSONResponse(content={'error': 'Post not found'}, status_code=404)

def delete_post_api(post_id):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.deleted_at = datetime.utcnow()
        db.commit()
        db.close()
        return ORJSONResponse(content={'message': 'Post deleted'})
    db.close()
    return ORJSONResponse(content={'error': 'Post not found'}, status_code=404)

def list_users_api():
    sync_users()
    db = next(get_db())
    users = db.query(User).all()
    db.close()
    return ORJSONResponse(content=[user.to_dict() for user in users])

def user_detail_api(user_id):
    db = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user:
        return ORJSONResponse(content=user.to_dict())
    return ORJSONResponse(content={'error': 'User not found'}, status_code=404)
