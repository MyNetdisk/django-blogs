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
    path('excel/', views.export_teachers_excel),
    path('pdf/', views.export_pdf),
    path('teachers_data/', views.get_teachers_data),
    path('echarts/', views.show_echarts),
    path('api/subjects/', views.show_subjects_api),
    path('api/restful/subjects/', views.show_subjects_api_restful),
    path('api/restful/teachers/', views.show_teachers_api_restful),
]
