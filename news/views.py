from django.shortcuts import render
from django.http import HttpResponse
from news.models import newsStory

# Create your views here.

def index(request):
    latest_story = newsStory.objects.order_by('-pub_date')[:5]
    context = {'latest_story': latest_story}
    return render(request, 'praktikal/index.html', context)
#def index(request):
    #return newsStory.heading


def mainstory(request):
    return HttpResponse("Jade is Angry")

