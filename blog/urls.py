from django.urls import path, include
from blog import views

urlpatterns = [
    path("hello/", views.Hello),
    path("subjects/", views.show_subjects),
    path("teachers/", views.show_teachers)
]
