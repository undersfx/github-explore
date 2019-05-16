from django.shortcuts import render
from django.http import HttpResponse
from .models import Repository
import requests
import json

# Create your views here.
def index(request, *args, **kwargs):
    if request.method == 'POST':
        print('POST: {}, {}, {}'.format(request.POST, args, kwargs))

        data = dict(request.POST.dict())
        del data['csrfmiddlewaretoken']

        rep = Repository(**data)

        try:
            rep.save()
        except Exception as e:
            print(e)
        
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
    print('GET: {}, {}, {}'.format(request.GET, args, kwargs))

    if repo_search is not None:
        r = requests.get('https://api.github.com/search/repositories?q=topic:{}'.format(repo_search), 
                        headers={'Accept': 'application/vnd.github.mercy-preview+json'})

        data = json.loads(r.text)
        
        featured = data['items']

        context = {'repos': featured}
    else:
        context = {}

    return render(request, 'find_repo.html', context)
