from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request, *args, **kwargs):
    print(request.GET, args, kwargs)
    print(request.POST, args, kwargs)

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

""" Exemplo data['items']:

[{'created_at': '2016-12-07T00:07:02Z',
            'created_by': 'Guido van Rossum',
            'curated': True,
            'description': 'Python is a dynamically typed programming language '
                           'designed by Guido van Rossum. Much like the '
                           'programming language Ruby, Python was designed to '
                           'be easily read by programmers. Because of its '
                           'large following and many libraries, Python can be '
                           'implemented and used to do anything from webpages '
                           'to scientific research.',
            'display_name': 'Python',
            'featured': True,
            'name': 'python',
            'released': 'February 20, 1991',
            'score': 6896.7534,
            'short_description': 'Python is a dynamically typed programming '
                                 'language.',
            'updated_at': '2019-05-15T02:53:55Z'},
            .
            .
            .]
"""