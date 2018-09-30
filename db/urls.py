from django.urls import path
from . import views

urlpatterns = [
    path('get_word', views.get_word),
    path('set_word', views.set_word),
    path('count', views.count)
]
