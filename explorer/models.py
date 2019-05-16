from django.db import models

# Create your models here.
class Topic(models.Model):
    '''Modelo para o consumo da API de Tópicos'''

    created_by          = models.CharField(max_length=128)
    description         = models.CharField(max_length=128)
    display_name        = models.CharField(max_length=128)
    name                = models.CharField(max_length=128)
    short_description   = models.CharField(max_length=512)
    released            = models.CharField(max_length=128)
    curated             = models.BooleanField()
    featured            = models.BooleanField()
    score               = models.DecimalField(decimal_places=0, max_digits=16)
    created_at          = models.DateTimeField()
    updated_at          = models.DateTimeField()

class Repository(models.Model):
    '''Modelo para o consumo da API de Reposítórios'''
    
    id                  = models.DecimalField(decimal_places=0, max_digits=32, primary_key=True)
    html_url            = models.CharField(max_length=128)
    name                = models.CharField(max_length=128)
    description         = models.CharField(max_length=256)
    created_at          = models.CharField(max_length=24)
    login               = models.CharField(max_length=128)
    forks_count         = models.DecimalField(decimal_places=0, max_digits=16) 
    stargazers_count    = models.DecimalField(decimal_places=0, max_digits=16)

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