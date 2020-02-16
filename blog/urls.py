from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('apt1/', views.apt1, name='blog-apt1'),
    path('apt2/', views.apt2, name='blog-apt2'),
    path('apt3/', views.apt3, name='blog-apt3'),
    path('apt4/', views.apt4, name='blog-apt4'),
    path('landlord/', views.landlord, name='blog-landlord')
]
