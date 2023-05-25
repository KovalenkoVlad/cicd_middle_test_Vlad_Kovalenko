from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe = Recipe.objects.create(title='Test Recipe', description='Test Description', created_at=2023)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')