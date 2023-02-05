from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound , Http404

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения")

def categories(request,catid):
    if(request.POST):
     print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year)>2023:
        return redirect('/', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
def handler403(request,exception):
    return ("<h1>Ошибка авторизации</h1>")
def handler400(request,exception):
    return  ("<h1>Невозможно обработать запрос</h1>")
def handler500(exception):
   return   ("<h1>Ошибка сервера</h1>")

