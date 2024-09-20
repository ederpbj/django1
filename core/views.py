
from django.utils import timezone  # Importar timezone do Django
from django.shortcuts import render

# Create your views here.

def index(request):
    #print(dir(request.user))
    #print(f'User: {request.user}')
    #print(request)
    #print(dir(request))
    #print(dir(request.session))
    #print(f'Headers: {request.headers}')
    #print(f"User-agente: {request.headers['User-Agent']}")
    #print(f"User: {request.user}") # retorna o usuario atual logado
    # Captura a data e hora atual
    #current_time = datetime.now()

    # Exibe informações da requisição e a data atual
    #print("Request Info:", request)
    #print(dir(request.user))
    #print(f"Last login: {request.user.last_login}") # retorna o usuario ultimo login
    #print(f"Last name: {request.user.last_name}") # retorna o usuario ultimo nome
    #print("Request Date:", current_time)
    #print(f"User: {request.user}") # retorna o usuario atual logado

    user = request.user  # Obtém o usuário autenticado
    #print(user.last_login)  # Exibe a data e hora do último login

    # Verifica se o usuário está autenticado
    if not user.is_authenticated:
        teste = 'Usuário não logado'
    else:
        # Converte o horário do último login para o fuso horário local
        last_login_local = timezone.localtime(user.last_login)
        # Formata a data e hora no formato desejado
        formatted_login = last_login_local.strftime('%d/%m/%Y - %H:%M:%S')
        teste = f'Usuário logado, último login: {formatted_login}'

    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é massa',
        'logado': teste,
        'usuario': user,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')