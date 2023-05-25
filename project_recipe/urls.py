from django.contrib import admin
from django.urls import path
#from recipe import views
from recipe.views import main,recipe_detail
urlpatterns = [
    path('main/', main, name='main'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('admin/', admin.site.urls),
]