from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('assets/', views.assets, name='assets'),
    path('deposit/', views.deposit, name='deposit'),
    path('portfolio/', views.portfolio, name='portfolio')
]