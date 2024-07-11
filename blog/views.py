from django.shortcuts import render, get_object_or_404
from .models import Blog, Tag, Category, comments
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.

def BlogList(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    blog_list = paginator.get_page(page_number)

    context = {
        "blogs": blog_list
    }

    return render(request, "blog/blog_list.html", context)


def Blog_Detail(request, id):
    blog_detail = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog_detail)
    category = Category.objects.all()
    comment = comments.objects.all().filter(blog=blog_detail)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]

            new_comment = comments(blog=blog_detail, name=new_name, message=new_message, email=new_email)
            new_comment.save()

    context = {
        "bloglist": blog_detail,
        "tags": tags,
        "category": category,
        "comment": comment
    }
    return render(request, "blog/Blog_detail.html", context)


def blog_tag(request, tag):
    blogs = Blog.objects.filter(tags__slug=tag)

    context = {
        "blogs": blogs
    }
    return render(request, "blog/blog_list.html", context)


def blog_category(request, category):
    blogs = Blog.objects.filter(category__slug=category)

    context = {
        "blogs": blogs
    }
    return render(request, "blog/blog_list.html", context)


def search(request):  # Code For Views %%%%
    if request.method == "GET":
        q = request.GET.get("search")
    blogs = Blog.objects.filter(title__icontains=q)
    return render(request, "blog/blog_list.html", {"blogs": blogs})
