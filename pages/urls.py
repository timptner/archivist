from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
]
