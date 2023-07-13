from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
    path('page1', TemplateView.as_view(template_name='home/login.html'), name='page1'),
    path('page2', TemplateView.as_view(template_name='home/login.html'), name='page2'),
    path('page3', TemplateView.as_view(template_name='home/login.html'), name='page3'),
]
