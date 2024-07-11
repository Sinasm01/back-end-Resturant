from django.shortcuts import render
from .models import Foods


# Create your views here.

def Food_list(request):
    food_list = Foods.objects.all()  # از داخل مدلی که ما ساختیم برو تمام غذاهایی که کاربر گذاشته رو بردار بیار داخل این متغیر بریز
    context = {
        "Foods": food_list,

    }
    return render(request, "Foods/list.html", context)


def Food_detail(request , id ):
    food_detail = Foods.objects.get(id=id)
    context = {
        "Food": food_detail
    }
    return render(request, "Foods/details.html", context)
