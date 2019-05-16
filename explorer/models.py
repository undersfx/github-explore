from django.db import models

# Create your models here.
class Topic(models.Model):
    '''Modelo para o consumo da API de Tópicos'''

    created_by          = models.CharField(max_length=128) # 'Guido van Rossum',
    description         = models.CharField(max_length=128) # 'Python is a dynamically typed programming language designed '
    display_name        = models.CharField(max_length=128) # 'Python',
    name                = models.CharField(max_length=128) # 'python',
    short_description   = models.CharField(max_length=512) # 'Python is a dynamically typed programming language.',
    released            = models.CharField(max_length=128) # 'February 20, 1991',
    curated             = models.BooleanField() # True,
    featured            = models.BooleanField() # True,
    score               = models.DecimalField(decimal_places=0, max_digits=16) # 6896.7534,
    created_at          = models.DateTimeField() # '2016-12-07T00=07=02Z',
    updated_at          = models.DateTimeField() # '2019-05-15T02=53=55Z'}

class Repository(models.Model):
    '''Modelo para o consumo da API de Reposítórios'''
    
    id                  = models.DecimalField(decimal_places=0, max_digits=32, primary_key=True) # '45717250', 
    html_url            = models.CharField(max_length=128) # 'https://github.com/tensorflow/tensorflow', 
    name                = models.CharField(max_length=128) # 'tensorflow', 
    description         = models.CharField(max_length=256) # 'An Open Source Machine Learning Framework for Everyone', 
    created_at          = models.CharField(max_length=24) # '2015-11-07T01:19:20Z', 
    login               = models.CharField(max_length=128) # 'tensorflow', 
    forks_count         = models.DecimalField(decimal_places=0, max_digits=16) # '74685', 
    stargazers_count    = models.DecimalField(decimal_places=0, max_digits=16) # '127613'

""" Example Repository:
        {'csrfmiddlewaretoken': 'Z1vlk5jq7CfMiqtonFNwWgD5voJLOosMqaUAhVbvGMyYq84JFzvmNmb21Fnbaq40',
        'id': '45717250', 
        'html_url': 'https://github.com/tensorflow/tensorflow', 
        'name': 'tensorflow', 
        'description': 'An Open Source Machine Learning Framework for Everyone', 
        'created_at': '2015-11-07T01:19:20Z', 
        'login': 'tensorflow', 
        'forks_count': '74685', 
        'stargazers_count': '127613'}
"""

""" Exemple Topic:
{'created_at': '2016-12-07T00:07:02Z',
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
            'updated_at': '2019-05-15T02:53:55Z'}
"""