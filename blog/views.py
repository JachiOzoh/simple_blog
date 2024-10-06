from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author':'jachi',
        'title':'Do you want to develop an app?',
        'content':'The post content...',
        'date_posted':'August 28 2024',
    }
,

    {
        'author':'quincy',
        'title':'Dont develop the app!',
        'content':'The post content...',
        'date_posted':'August 29 2024',
    }
]

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})