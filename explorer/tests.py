from django.test import TestCase
from .models import Repository
from .views import index
from django.core.handlers.wsgi import WSGIRequest


# Model Tests
class RepositoryTestCase(TestCase):
    def setUp(self):
        self.repo1 = Repository(id=1, name='foo')
        self.repo2 = Repository(id=2, name='bar')

    def test_repository_instance(self):
        self.assertIsInstance(self.repo1, Repository)
        self.assertIsInstance(self.repo2, Repository)

    def test_repository_property(self):
        self.assertEqual(self.repo1.name, 'foo')
        self.assertEqual(self.repo2.name, 'bar')

# View Tests