from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def users(request):
    return render(request, 'main/users.html')
