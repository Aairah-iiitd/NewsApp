from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('category/<str:category>', views.categoric, name = "category"),
    path('world', views.worldnews, name = "world"),
    path('search', views.search, name = "search")
]
