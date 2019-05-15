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
    if request.POST is not None:
        data = request.POST.dict()
        
        #Example:
        # {'csrfmiddlewaretoken': 'Z1vlk5jq7CfMiqtonFNwWgD5voJLOosMqaUAhVbvGMyYq84JFzvmNmb21Fnbaq40',
        # 'id': '45717250', 
        # 'html_url': 'https://github.com/tensorflow/tensorflow', 
        # 'name': 'tensorflow', 
        # 'description': 'An Open Source Machine Learning Framework for Everyone', 
        # 'created_at': '2015-11-07T01:19:20Z', 
        # 'login': 'tensorflow', 
        # 'forks_count': '74685', 
        # 'stargazers_count': '127613'}

    repo_search = request.GET.get('search')

    if repo_search is not None:
        r = requests.get('https://api.github.com/search/repositories?q=topic:{}'.format(repo_search), 
                        headers={'Accept': 'application/vnd.github.mercy-preview+json'})

        data = json.loads(r.text)
        
        featured = data['items']

        context = {'repos': featured}
    else:
        context = {}

    return render(request, 'find_repo.html', context)
