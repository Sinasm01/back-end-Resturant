from django.contrib import admin
from .models import Blog
from .models import Category
from .models import Tag
from .models import comments

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(comments)
