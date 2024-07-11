from django.urls import path
from .import views
app_name = "Foods"

urlpatterns = [
    path("",views.Food_list,name="Food_list"),
    path("<int:id>/",views.Food_detail,name="detail")
]