from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('doctors', views.doctors, name="doctors"),
    path('gallery', views.gallery, name="gallery"),
    path('services', views.services, name="services"),
    path('faq', views.faq, name="faq"),
    path('appointment', views.appointment, name="appointment"),
    path('contact', views.contact, name="contact"),
]