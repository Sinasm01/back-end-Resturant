from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.TextField(_("توضیحات"), max_length=100)
    create_time = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    auther = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blog/", null=True, blank=True)
    category = models.ForeignKey("Category", related_name="blog", verbose_name=_("دسته بندی"), on_delete=models.CASCADE,
                                 null=True, blank=True)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"), related_name="blogs", null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))  # در داخل سرچ بار بالای سفحه مرورگر سرچ ما شکل بهتری میگیرد
    publish_data = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    publish_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("تاریخ بروزرسانی"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class comments(models.Model):
    blog = models.ForeignKey("Blog", verbose_name=_("مقاله"), related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(_("نام"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=50)
    message = models.TextField(_("پیام"), max_length=50)
    data = models.DateTimeField(_("تاریخ"), max_length=50, auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
