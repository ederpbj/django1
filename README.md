

### Links úteis

[Curso](https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/)

[HTML for beginners](https://html.com/)

[Web Developer - extension](https://chromewebstore.google.com/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm?hl=pt-BR&pli=1)

[Bootstrap](https://getbootstrap.com/)

[One page html](https://onepagelove.com/templates/free-templates)

### Aulas Resumos

#### Seção 3 Django Framework básico

1. Introdução
2. Criando um ambiente virtual e instalando Django
3. Criando um projeto Django com SQlite3 
4. Criando uma aplicação Django e conhecendo estrutura
5. Django Projeto x Aplicações
6. O padrão MTV do Django
7. Configurações do Django e o arquivo settings.py
8. Views no Django e o arquivo views.py
9. Rotas no Django e o arquivo urls.py
10. Templates no Django
11. Models no Django e o arquivo models.py

### Comandos

```Python
# Ativar ambiente virtual
source myenv/bin/activate

# Sair do ambiente vitual
deactivate

pip install django

# salva em txt todas as bibliotecas utilizadas
pip freeze > requirements.txt

# iniciar o django no diretório
# manage gerencia a aplicação
django-admin startproject django1 . # cria projeto na raiz manager.py
django-admin startproject django1   # cria projeto uma pasta e dentro dela manager.py

django-admin startapp core # cria uma aplicação, informar no django1/INSTALLED_APPS, bem como templates

python manage.py runserver # rodar o servidor na pasta django1

python manage.py makemigrations # fazer as migrações

python manage.py migrate # executar a migrate, depois abrir o db.sqlite3


```
