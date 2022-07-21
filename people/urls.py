from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'people'
urlpatterns = [
    path(_('register/'), views.RegistrationView.as_view(), name='register'),
    path(_('register/done/'), views.RegistrationDoneView.as_view(), name='register-done'),
    path(_('profile/'), views.ProfileView.as_view(), name='profile'),
    path(_('login/'), views.LoginView.as_view(), name='login'),
    path(_('logout/'), views.LogoutView.as_view(), name='logout'),
    path(_('password/change/'), views.PasswordChangeView.as_view(), name='change-password'),
    path(_('password/change/done/'), views.PasswordChangeDoneView.as_view(), name='change-password-done'),
    path(_('password/reset/'), views.PasswordResetView.as_view(), name='reset-password'),
    path(_('password/reset/done/'), views.PasswordResetDoneView.as_view(), name='reset-password-done'),
    path(_('reset/<uidb64>/<token>/'), views.PasswordResetConfirmView.as_view(), name='reset-password-confirm'),
    path(_('reset/done/'), views.PasswordResetCompleteView.as_view(), name='reset-password-complete'),
]
