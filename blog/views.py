from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Category,Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CategoryModalForm


# Home View Function
def HomeView(request):
    featuredPosts = Post.objects.order_by('-id')[0:3]
    post_lists  = Post.objects.order_by('-id')
    categories = Category.objects.order_by("-id")



    paginator = Paginator(post_lists, 5)
    page = request.GET.get('page')
    post_lists = paginator.get_page(page)


    context = {
        "featuredPosts": featuredPosts,
        "post_lists": post_lists,
        "categories": categories
    }
    return render(request, 'blog/home.html', context)




# Category View Function
@login_required
def CategoryView(request):
    cat = Category.objects.order_by('-id')

    paginator = Paginator(cat, 10)
    page = request.GET.get('page')
    cat = paginator.get_page(page)


    context ={
        "categories": cat
    }
    return render(request, 'blog/categories.html', context)

@login_required

def CategoryUpdateView(request, pk):
    cat_id =get_object_or_404(Category,pk=pk)
    form = CategoryModalForm(request.POST or None, instance=cat_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updatedBy = request.user.id
        obj.save()
        messages.success(request, 'Category Updated Successfully')
        return redirect('/category/')
    
    context={
        'form':form,
        'valueBtn':'Update',
        'title':'Update Category'
    }

    return render(request,'blog/category-form.html',context)


@login_required
def CategoryDeleteView(request,pk):
    query_del = get_object_or_404(Category, pk=pk)
    query_del.delete()
    messages.success(request, "Category Deleted Successfully")
    return redirect('/category/')

@login_required

def CategoryCreateView(request):
    form= CategoryModalForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.createdBy=request.user.id
        obj.save()
        messages.success(request, 'Category Added Successfully')
        return redirect('/category/')
    
    context={
        'form':form,
        'valueBtn':'Add',
        'title':'Create Category'
    }

    return render(request,'blog/category-form.html',context)