from django.shortcuts import render, redirect
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

def addcomment(request):
    #print(request.GET['comment_tx'])
    #print(request.GET['id'])
    video = Video.objects.get(id=request.GET['id'])
    newcomment = Comment(text=request.GET['comment_tx'], video_id=video)
    newcomment.save()
    return redirect('/')
# Create your views here.
