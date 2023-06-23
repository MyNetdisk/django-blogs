from django.urls import path, include
from blog import views

urlpatterns = [
    path("hello/", views.Hello),
    path("subjects/", views.show_subjects),
    path("teachers/", views.show_teachers),
    path("praise/", views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('login/', views.login),
    path('captcha/', views.get_captcha),
]
