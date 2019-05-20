from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Post
#from .forms import PostForm, UserLoginForm, ImageForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
# Create your views here.

#def post_list(request):
#    return render(request,'blog/post_list.html')

def post_list(request):
    post_list= Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list,})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def edit_post(request, post_id=None):
    item = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'blog/post_form.html', {'form': form})

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
            # return redirect('post_detail', pk=post.pk)
    #         return redirect('post_list',)
    # else:
    #     form = PostForm()
    # return render(request, 'blog/post_edit.html', {'form': form})