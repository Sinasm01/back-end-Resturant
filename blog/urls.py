from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogList, name="blog_list"),
    path("<int:id>/", views.Blog_Detail, name="blog"),
    path("tag/<slug:tag>", views.blog_tag, name="tag"),
    path("category/<slug:category>", views.blog_category, name="category"),
    path("search/", views.search, name="search"),

]
