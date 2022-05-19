from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.views import generic

from .forms import RegistrationForm


class LandingPage(generic.TemplateView):
    template_name = 'people/landing_page.html'


class RegistrationView(generic.CreateView):
    template_name = 'people/registration_form.html'
    form_class = RegistrationForm
    success_url = 'done/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        return super().form_valid(form)


class RegistrationDoneView(generic.TemplateView):
    template_name = 'people/registration_done.html'


class ProfileView(generic.UpdateView):
    template_name = 'people/profile.html'
    fields = ['first_name', 'last_name', 'email', 'faculty']

    def post(self, request, *args, **kwargs):
        raise PermissionDenied

    def get_object(self, queryset=None):
        return self.request.user


class LoginView(auth_views.LoginView):
    template_name = 'people/login.html'
    next_page = 'people:landing-page'


class LogoutView(auth_views.LogoutView):
    template_name = 'people/logout.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'people/change_password_form.html'
    success_url = 'done/'


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'people/change_password_done.html'
