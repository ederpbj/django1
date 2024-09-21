from django.utils.translation.trans_null import deactivate

### Links úteis

[Curso](https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/)

[HTML for beginners](https://html.com/)

[Web Developer - extension](https://chromewebstore.google.com/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm?hl=pt-BR&pli=1)

[Bootstrap](https://getbootstrap.com/)

[One page html](https://onepagelove.com/templates/free-templates)

[images google](https://images.google.com/)

[Django Document](https://docs.djangoproject.com/en/5.1/)

[Html Document](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)


### Aulas Resumos

#### Seção 3 Django Framework básico

17. Introdução
18. Criando um ambiente virtual e instalando Django
19. Criando um projeto Django com SQlite3 
20. Criando uma aplicação Django e conhecendo estrutura
21. Django Projeto x Aplicações
22. O padrão MTV do Django
23. Configurações do Django e o arquivo settings.py
24. Views no Django e o arquivo views.py
25. Rotas no Django e o arquivo urls.py
26. Templates no Django
27. Models no Django e o arquivo models.py
28. Área administrativa e o arquivo admin.py
29. Django shell
30. Dados do banco no template 
31. Arquivos estáticos no Django: CSS, JavaScript e Imagens
32. Coloque nos seus favoritos: Django Docs
33. 
Miniatura da aula
6:58 / 43:07
33. Publicando na internet seu primeiro projeto Django

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

python manage.py createsuperuser # cria super usuario para rota admin

python manage.py # lista os comandos do manage

python manage.py shell # carrega um console python

    from core.models import Produto
    dir(Produto) # mostra os atributos no shell
    
    from core.views import index
    dir(index) # mostra os atributos no shell
    
    # Salvando via shell
    from.core.models import Produto
    produto = Produto(nome="Maquina de barbear", preco=59.99, estoque=1)
    produto.save()
    dir(Produto)
    produto.id
    
    # Cliente via shell
    from.core.models import Cliente
    cliente = Cliente(nome='Erika', sobrenome='CICC PM', email="eroka@gmail.com")
    cliente.save()
    dir(Cliente) # mostra atributos
    cliente.nome
    
    # Alterar ultimo registro
    cliente.nome = 'Eliane'
    cliente.email = 'eliane@gmail.com'
    cliente.save()
    cliente.delete() # deleta ultimo registro
    
    # Dados do banco no template
    python manage.py shell
    from.core.models import Produto
    dir(Produto.objects) # mostra as funções disponíveis
    Produto.objects.all() # exibe todos os produtos
    produtos = Produto.objects.all()
    
    # 31. Arquivos estáticos no Django: CSS, JavaScript e Imagens
    python manage.py shell
    pwd # mostra caminho do diretório atual
    
    from django1.settings import BASE_DIR
    STATIC_ROOT = BASE_DIR/'staticfiles'
    
    python manage.py # exibe funções

    python manage.py collectstatic # coleta os arquivos estaticos e cria uma pasta
    
# atualizando django
python -m django --version
brew install python3.10
python3.10 -m pip install Django==5.1.1

deactivate # sair da base virtual

# 33. Publicando na internet seu primeiro projeto Django
pip install whitenoise gunicorn # serve para arquivos estaticos e manage


# ajustando gitignore
git rm -r --cached . # elimina de acordo com gitignore

git status 

git add . # adicionando arquivos

git commit -m "Projeto finalizado"

```
