from django.urls import path, include
from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),  # in html using {% url 'about' %} thats how nae is being used rather then some link
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
]
