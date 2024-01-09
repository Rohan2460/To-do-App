from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add", views.add_note, name="add"),
    path("delete/<int:id>", views.del_note, name="delete"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("signup", views.signup, name="signup"),
]
