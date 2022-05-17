from django.urls import path

from . import views

app_name = 'people'
urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing-page'),
]
