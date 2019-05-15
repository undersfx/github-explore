from django.db import models

# Create your models here.
class Repo(models.Model):
    created_by          = models.CharField(max_length=100) # 'Guido van Rossum',
    description         = models.CharField(max_length=100) # 'Python is a dynamically typed programming language designed '
    display_name        = models.CharField(max_length=100) # 'Python',
    name                = models.CharField(max_length=100) # 'python',
    short_description   = models.CharField(max_length=500) # 'Python is a dynamically typed programming language.',
    released            = models.CharField(max_length=100) # 'February 20, 1991',
    curated             = models.BooleanField() # True,
    featured            = models.BooleanField() # True,
    score               = models.DecimalField(decimal_places=0, max_digits=16) # 6896.7534,
    created_at          = models.DateTimeField() # '2016-12-07T00=07=02Z',
    updated_at          = models.DateTimeField() # '2019-05-15T02=53=55Z'}

# >>> from django.utils.dateparse import parse_datetime
# >>> parse_datetime('2016-12-07T00=07=02'.replace('=', ':'))
# datetime.datetime(2016, 12, 7, 0, 7, 2)

""" Exemplo data['items']:
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