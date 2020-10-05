from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('services/', views.services, name='services'), 
    path('projects/', views.projects, name='projects'),
    path('message-sending/', views.send_message, name="send_message"),
    path('testimonies/', views.testify, name='testify')
]
