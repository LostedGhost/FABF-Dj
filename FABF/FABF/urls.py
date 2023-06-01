from django.contrib import admin
from django.urls import path
from services import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('register', views.register, name="register"),
    path('add_user', views.add_user, name="add_user"),
    path('login', views.login, name="login"),
]
