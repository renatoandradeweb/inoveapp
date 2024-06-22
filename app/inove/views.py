from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
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

def index(request):
    return render(request, 'index.html')

def sync_users(request):
    db = next(get_db())
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()
    except RequestException as e:
        messages.error(request, f'Failed to access API: {e}')
        return False

    try:
        users = response.json()
    except ValueError as e:
        messages.error(request, f'Failed to parse JSON: {e}')
        return False

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
    return True  # Indica sucesso

def sync_posts(request):
    db = next(get_db())
    if not sync_users(request):  # Sincronize os usuários antes dos posts
        return False  # Se a sincronização de usuários falhar, retorne False

    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
    except RequestException as e:
        messages.error(request, f'Failed to access API: {e}')
        return False

    try:
        posts = response.json()
    except ValueError as e:
        messages.error(request, f'Failed to parse JSON: {e}')
        return False

    for post_data in posts:
        post = db.query(Post).filter(Post.id == post_data['id']).first()
        if post:
            if post.deleted_at is not None or post.created_at is not None or post.updated_at is not None:
                continue
        else:
            post = Post(
                title=post_data['title'],
                body=post_data['body'],
                user_id=post_data['userId']
            )
            db.add(post)
    db.commit()
    return True  # Indica sucesso

def list_posts(request):
    if not sync_posts(request):
        messages.error(request, "Failed to sync posts.")

    db = next(get_db())

    query = request.GET.get('q')
    posts = db.query(Post).filter(Post.deleted_at == None).order_by(Post.id).all()

    paginator = Paginator(posts, 10)  # Mostra 10 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list_posts.html', {'page_obj': page_obj, 'query': query})

def view_post(request, post_id):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == post_id, Post.deleted_at == None).first()
    user = db.query(User).filter(User.id == post.user_id).first()
    db.close()
    if post:
        return render(request, 'view_post.html', {'post': post, 'user': user.name })
    else:
        messages.error(request, "Post not found.")
        return redirect('list_posts')

def list_users(request):
    if not sync_posts(request):
        messages.error(request, "Failed to sync users.")

    db = next(get_db())
    users = db.query(User).all()
    return render(request, 'list_users.html', {'users': users})

def view_user(request, user_id):
    db = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    return render(request, 'view_user.html', {'user': user})

def create_post(request):
    db = next(get_db())
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user_id = request.POST.get('user')
        try:
            post_data = {
                'title': title,
                'body': body,
                'userId': user_id
            }
            response = requests.post('https://jsonplaceholder.typicode.com/posts', json=post_data)
            response.raise_for_status()

            # Verificar se o ID já existe e definir um novo ID se necessário
            db_post = Post(title=title, body=body, user_id=user_id)
            db.add(db_post)
            db.commit()
            db.refresh(db_post)
        except requests.RequestException:
            messages.error(request, "Failed to access API. Post not created.")
        except Exception as e:
            db.rollback()  # Rollback in case of error
            messages.error(request, f"Error creating post: {e}")
        else:
            messages.success(request, "Post created successfully.")
        return redirect('list_posts')
    else:
        users = db.query(User).all()
        return render(request, 'create_post.html', {'users': users})

def edit_post(request, post_id):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == post_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user_id = request.POST.get('user')
        try:
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post.id}')
            if response.status_code == 200:
                # Atualiza o post na API
                post_data = {
                    'id': post.id,
                    'title': title,
                    'body': body,
                    'userId': user_id
                }
                response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post.id}', json=post_data)
                response.raise_for_status()
            post.title = title
            post.body = body
            post.user_id = user_id
            db.commit()
            db.refresh(post)
        except requests.RequestException:
            messages.error(request, "Failed to access API. Post not updated.")
        else:
            messages.success(request, "Post updated successfully.")
        return redirect('list_posts')
    else:
        users = db.query(User).all()
        return render(request, 'edit_post.html', {'post': post, 'users': users})

def delete_post(request, post_id):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == post_id).first()
    try:
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post.id}')
        response.raise_for_status()
        post.deleted_at = datetime.utcnow()
        db.commit()
    except requests.RequestException:
        messages.error(request, "Failed to access API. Post not deleted.")
    else:
        messages.success(request, "Post successfully deleted.")
    return redirect('list_posts')
