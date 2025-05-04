from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('project/', views.project, name='project'),
    path('team/', views.team, name='team'),
    path('career/', views.career, name='career'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

]