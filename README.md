# InoveApp

### **Documentation in English**

InoveApp is a Django application with SQLAlchemy, including a FastAPI backend and integration with the JSONPlaceholder API for CRUD operations on posts and users.

## Project Structure

- **/**: Root directory of the project.
  - **.gitignore**: Git configuration file.
  - **docker-compose.yml**: Docker Compose configuration file.
  - **Dockerfile**: Docker configuration file.
  - **README.md**: Project documentation.
  - **wait-for-it.sh**: Script to wait for database initialization.
    - **app/**: Main application directory.
      - **requirements.txt**: File with project dependencies.
      - **manage.py**: Django management script.
      - **fastapi_app.py**: FastAPI Application Routes.
      - **inove/**: Django app directory.
        - **templates/**: HTML templates directory.
        - **api_views.py**: REST API views.
        - **create_tables.py**: Script to create tables in the database.
        - **db.py**: Database configuration using SQLAlchemy.
        - **forms.py**: Django forms.
        - **models_sqlalchemy.py**: Data models definition with SQLAlchemy.
        - **settings.py**: Django settings.
        - **urls.py**: Django URLs.
        - **views.py**: Django views.
        - **wsgi.py**: WSGI (Web Server Gateway Interface) configuration.

## Environment Setup

### Prerequisites

- Docker
- Docker Compose

### Instructions below for running the project

1. Clone this repository:

    ```bash
    git clone https://github.com/renatoandradeweb/inoveapp.git
    cd inoveapp
    ```

2. Build and start the containers:

    ```bash
    docker-compose up --build
    ```

### Docker

4. Dockerfile:

The `Dockerfile` downloads the Python 3.9 image, installs project dependencies, and copies project files into the container.

The `docker-compose.yml` file defines three services:

- **db**: PostgreSQL database service.
- **web**: Django service for the application backend.
- **fastapi**: FastAPI service for the REST API.

5. Access the application:

    - Django App: `http://localhost:8000`
    - FastAPI App: `http://localhost:8001`
    - API Documentation: `http://localhost:8001/docs`


6. REST API Routes:
    - The REST API only manipulates the database:
    - Use Postman or Insomnia to test the routes. Set the base URL to `http://localhost:8001/`.
    - You can also test the APIs using Swagger at `http://localhost:8001/docs`.
    - **GET** `/api/posts/`: List all posts.
    - **GET** `/api/posts/{id}/`: Details of a post.
    - **POST** `/api/posts/`: Create a new post.
    - **PUT** `/api/posts/{id}/`: Update a post.
    - **DELETE** `/api/posts/{id}/`: Delete a post.
    - **GET** `/api/users/`: List all users.
    - **GET** `/api/users/{id}/`: View details of a user.


7. Django Routes:
    - The Django application manipulates both the database and the JSONPlaceholder API:
    - Use the browser to access the routes. Address for access `http://localhost:8000/`.
    - **`/`**: Home page.
    - **`/posts/`**: List all posts.
    - **`/posts/{id}/`**: View details of a post.
    - **`/posts/create_post/`**: Create a new post.
    - **`/posts/edit_post/{id}`**: Edit a post.
    - **`/posts/delete_post/{id}`**: Delete a post.
    - **`/users/`**: List all users.
    - **`/users/{id}/`**: View details of a user.

## Contact
For more information about the project, please contact me:
- LinkedIn: https://www.linkedin.com/in/renatoandradeweb/
- GitHub: https://github.com/renatoandradeweb
- WhatsApp: http://wa.me/5563999821991
- Name: Renato Andrade da Fonseca

<br>

---

### **Documentação em Português**

InoveApp é uma aplicação Django com SQLAlchemy, que inclui um backend FastAPI e integração com a API JSONPlaceholder para operações CRUD em posts e usuários.

## Estrutura do Projeto

- **/**: Diretório raiz do projeto.
  - **.gitignore**: Arquivo de configuração do Git.
  - **docker-compose.yml**: Arquivo de configuração do Docker Compose.
  - **Dockerfile**: Arquivo de configuração do Docker.
  - **README.md**: Documentação do projeto.
  - **wait-for-it.sh**: Script para aguardar a inicialização do banco de dados.
    - **app/**: Diretório principal do aplicativo.
      - **requirements.txt**: Arquivo com as dependências do projeto.
      - **manage.py**: Script de gerenciamento do Django.
      - **fastapi_app.py**: Rotas Aplicação FastAPI.
      - **inove/**: Diretório do Django app.
        - **templates/**: Diretório de templates HTML.
        - **api_views.py**: Views da API REST.
        - **create_tables.py**: Script para criar tabelas no banco de dados.
        - **db.py**: Configuração do banco de dados usando SQLAlchemy.
        - **forms.py**: Formulários do Django.
        - **models_sqlalchemy.py**: Definição dos modelos de dados com SQLAlchemy.
        - **settings.py**: Configurações do Django.
        - **urls.py**: URLs do Django.
        - **views.py**: Views do Django.
        - **wsgi.py**: Configuração do WSGI (Web Server Gateway Interface).

## Configuração do Ambiente

### Pré-requisitos

- Docker
- Docker Compose

### Instruções abaixo para execução do projeto

1. Clone este repositório:

    ```bash
    git clone https://github.com/renatoandradeweb/inoveapp.git
    cd inoveapp
    ```

2. Construa e inicie os contêineres:

    ```bash
    docker-compose up --build
    ```

### Docker

4. Dockerfile:

O arquivo `Dockerfile` baixa a imagem do Python 3.9, instala as dependências do projeto e copia os arquivos do projeto para o contêiner.

O arquivo `docker-compose.yml` define três serviços:

- **db**: Serviço de banco de dados PostgreSQL.
- **web**: Serviço Django para o backend da aplicação.
- **fastapi**: Serviço FastAPI para a API REST.

5. Acesse a aplicação:

    - Django App: `http://localhost:8000`
    - FastAPI App: `http://localhost:8001`
    - API Documentação: `http://localhost:8001/docs`


6. Rotas da API REST:
    - A API REST manipula somente o banco de dados:
    - Use o Postman ou Insomnia para testar as rotas. Defima a url base como `http://localhost:8001/`.
    - Você também pode testar as apis usando o Swagger em `http://localhost:8001/docs`.
    - **GET** `/api/posts/`: Lista todos os posts.
    - **GET** `/api/posts/{id}/`: Detalhes de um post.
    - **POST** `/api/posts/`: Cria um novo post.
    - **PUT** `/api/posts/{id}/`: Atualiza um post.
    - **DELETE** `/api/posts/{id}/`: Deleta um post.
    - **GET** `/api/users/`: Lista todos os usuários.
    - **GET** `/api/users/{id}/`: Ver Detalhes de um usuário.


7. Rotas do Django:
    - A aplicação do Django manipula o banco de dados e a api JSONPlaceholder:
    - Use o navegador para acessar as rotas. Endereço para acesso `http://localhost:8000/`.
    - **`/`**: Página inicial.
    - **`/posts/`**: Lista todos os posts.
    - **`/posts/{id}/`**: Ver Detalhes de um post.
    - **`/posts/create_post/`**: Cria um novo post.
    - **`/posts/edit_post/{id}`**: Edita um post.
    - **`/posts/delete_post/{id}`**: Deleta um post.
    - **`/users/`**: Lista todos os usuários.
    - **`/users/{id}/`**: Ver Detalhes de um usuário.

## Contato
Para mais informações sobre o projeto, entre em contato comigo:
- LinkedIn: https://www.linkedin.com/in/renatoandradeweb/
- github: https://github.com/renatoandradeweb
- whatsapp: http://wa.me/5563999821991
- nome: Renato Andrade da Fonseca
