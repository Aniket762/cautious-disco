from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='feed-page'),
    path('about/', views.about, name='about-page')
]
