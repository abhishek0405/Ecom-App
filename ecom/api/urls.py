from django.urls import path, include
from rest_framework.authtoken import views
from .views import home#.views means current dir views
urlpatterns = [
    path('', home, name='api.home'),# home is a name of method we will declare in views of respective app
    path('category/',include('api.category.urls')) #route for /api/category defined in the path specified.
]