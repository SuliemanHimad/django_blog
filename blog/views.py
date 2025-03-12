from django.shortcuts import render
from blog.models import Category,Post
from django.core.paginator import Paginator
# Create your views here.

def HomeView(request):
    featuredPosts = Post.objects.order_by('-id')[0:3]
    post_lists  = Post.objects.order_by('-id')

    paginator = Paginator(post_lists, 5)
    page = request.GET.get('page')
    post_lists = paginator.get_page(page)




    context = {
        "featuredPosts": featuredPosts,
        "post_lists": post_lists
    }
    return render(request, 'blog/home.html', context)

def CategoryView(request):
    cat = Category.objects.order_by('-id')
    context ={
        "categories": cat
    }
    return render(request, 'blog/categories.html', context)