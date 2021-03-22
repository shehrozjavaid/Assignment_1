from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.forms import ModelForm

from BLOG_POSTS.models import blogpost
# Create your views here.

class PostForm(ModelForm):
    class Meta:
        model = blogpost
        fields = ['blog_title','blog_body','blog_author']

def post_list(request):
    posts = blogpost.objects.order_by('blog_title')
    context = {
        "posts" : posts
    }
    return render(request,"POST_LIST.html",context=context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse("BLOG_POSTS:list"))
    return render(request,"POST_FORM.html", {"form":form})

def post_update(request,post_id):
    post = get_object_or_404(blogpost,pk=post_id)
    form = PostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect(reverse("BLOG_POSTS:list"))
    return render(request,"POST_FORM.html", {"form":form})

def post_del(request,post_id):
    post=get_object_or_404(blogpost,pk=post_id)
    if request.method == "POST":
        post.delete()
        return redirect(reverse("BLOG_POSTS:list"))
    return render(request,"POST_DELETE.html")