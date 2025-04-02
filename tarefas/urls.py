from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaTarefa, name='lista-tarefa'),
    path('tarefa/<int:id>', views.tarefaView, name='tarefa-view'),
    path('novaTarefa/', views.novaTarefa, name='nova-tarefa'),
]
