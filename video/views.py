from django.shortcuts import render
from django.http import HttpResponse
from .models import Video, Comment



def hello(request):
    users = ['Egor', 'Pavel', 'Domkrat', 'Idrak', 'Magnat', 'Drax']
    ll = list(range(10))
    return render(request, 'index.html', {'pips':users, 'll':ll})
    # return HttpResponse('hello world')

def show_all(request):
    videos = Video.objects.all()
    comments = Comment.objects.all()
    return render(request, 'show_all.html', {'videos':videos,
                  'comments':comments})
# Create your views here.
