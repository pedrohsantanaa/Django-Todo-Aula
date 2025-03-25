from django.shortcuts import render

# Create your views here.

def listaTarefa(request):
    return render(request, 'tarefas/list.html')