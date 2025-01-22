from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):    
    post = Posts.objects.all().order_by("-id") 
    context = {
        "post" : post
    } 
    return render(request, "index.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect("post:detail",post.id)
    else : 
        form = PostForm()

    context = {"form":form}
    return render(request, "create.html", context)

def detail(request, pk):
    try :
        post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return redirect("post:index")

    context = {
        "post" : post,
    }
    return render(request, "detail.html",context)

def del_post(request,pk):
    post = Posts.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post:index")
    return redirect("post:detail",post.pk)

def edit(request,pk):
    post = Posts.objects.get(pk=pk)
    context = {
        "post" : post,
    }
    return render(request,'edit.html', context)

def update(request,pk):
    post = Posts.objects.get(pk=pk)
    post.title = request.POST.get("title")
    post.content = request.POST.get("content")
    post.save()
    return redirect("post:detail", post.pk)