from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'people'
urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing-page'),
    path(_('register/'), views.RegistrationView.as_view(), name='register'),
    path(_('register/done/'), views.RegistrationDoneView.as_view(), name='register-done'),
    path(_('login/'), views.LoginView.as_view(), name='login'),
    path(_('logout/'), views.LogoutView.as_view(), name='logout'),
    path(_('change-password/'), views.PasswordChangeView.as_view(), name='change-password'),
    path(_('change-password/done/'), views.PasswordChangeDoneView.as_view(), name='change-password-done'),
]
