from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class reservation(models.Model):
    name = models.CharField(_("نام"), max_length=200)
    email = models.EmailField(_("ایمیل"), max_length=245)
    phone = models.CharField(_("شماره تماس"), max_length=100)
    number = models.IntegerField(_("تعداد"), max_length=50)
    date = models.DateTimeField(_("تاریخ"), max_length=100)
    time = models.TimeField(_("ساعت"), max_length=50)

    def __str__(self):
        return self.email


