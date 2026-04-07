from django.urls import path
from Core import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('success/', views.sucess, name='success'),
    path('fail/', views.fail, name='fail'),
    path('',views.readme,name='readme')
]
