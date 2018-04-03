from django.shortcuts import render
from .models import Post

# Create your views here.

#def post_list(request):
#    return render(request,'blog/post_list.html')

def index(request):
    post_list= Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list,})


