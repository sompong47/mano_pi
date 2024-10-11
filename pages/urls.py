from django.urls import path
from pages.views import contact, about, index

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
]
