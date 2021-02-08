from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('result', views.result, name='result'),
    path('settings', views.settings, name='settings'),
    path('tutorial', views.tutorial, name='tutorial'),
]
