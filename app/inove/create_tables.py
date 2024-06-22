# app/inove/create_tables.py

import sys
import os

# Adicione o caminho da aplicação ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

# Configurar o Django antes de importar qualquer coisa
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inove.settings')
django.setup()

from inove.db import engine, Base
from inove.models_sqlalchemy import User, Post

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
