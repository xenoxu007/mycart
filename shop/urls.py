
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='shophome'),
    path('about/' , views.about ,name='about'),
    path('contact/', views.contact ,name='contat'),
    path('tracker/',views.tracker, name='tracker')
    ]