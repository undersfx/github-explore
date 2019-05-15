from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request, *args, **kwargs):
    print('GET: {}, {}, {}'.format(request.GET, args, kwargs))
    print('POST: {}, {}, {}'.format(request.POST, args, kwargs))

    # TODO:
    # Quando chegar uma solicitação de POST, salvar no banco de dados

    repo_search = request.GET.get('search')

    if repo_search:
        r = requests.get('https://api.github.com/search/repositories?q=topic:{}'.format(repo_search), 
                        headers={'Accept': 'application/vnd.github.mercy-preview+json'})

        data = json.loads(r.text)
        
        featured = data['items']

        context = {'repos': featured}
    else:
        context = {}

    return render(request, 'find_repo.html', context)
