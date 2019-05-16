from django.shortcuts import render
from django.http import HttpResponse
from .models import Repository
import requests
import json

# Create your views here.
def index(request, *args, **kwargs):
    '''Função que renderiza a pagina raíz com a chamada da API do Github e salva formulário do PostgreSQL'''

    if request.method == 'POST':
        # Cria uma cópias dos valores passados para adição ao banco
        data = dict(request.POST.dict())
        del data['csrfmiddlewaretoken']

        # Salva no banco de dados
        try:
            rep = Repository(**data)
            rep.save()
        except Exception as e:
            print(e)

    # Caso passados parâmetros de busca na requisição get, consome a API do Github
    repo_search = request.GET.get('search')

    if repo_search is not None:
        r = requests.get('https://api.github.com/search/repositories?q=topic:{}'.format(repo_search), 
                        headers={'Accept': 'application/vnd.github.mercy-preview+json'})

        # Parse da resposta JSON da API do Github                
        data = json.loads(r.text)

        # Passa para renderização os resultados
        featured = data['items']
        context = {'repos': featured}
    else:
        context = {}

    return render(request, 'find_repo.html', context)
