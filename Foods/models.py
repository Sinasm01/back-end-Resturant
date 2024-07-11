from django.db import models
from django.utils.translation import gettext as _  # برای اینکه بتونیم در مدل خود کلمات فارسی را به کار ببریم


# Create your models here.
class Foods(models.Model):
    FOOD_TYPE = [
        ("Drink", "نوشیدنی"),
        ("BreakFast", "صبحانه"),
        ("Dinner", "شام"),
        ("Lunch", "ناهار")
    ]

    name = models.CharField(_("نام"), max_length=100)
    description = models.CharField(_("توضیحات"), max_length=200)
    rate = models.IntegerField(_("امتیاز"), default=0)
    price = models.IntegerField(_("قیمت"), default=0)
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='Foods/', null=True)
    food_type = models.CharField(_("نوع غذا"), max_length=10, choices=FOOD_TYPE, default="Drink", null=True)

    def __str__(self):
        return self.name  # این میاد نامی را که برای عکس انتخاب کردیم رو توی جدول پنل کاربری نشون میده
