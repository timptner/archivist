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
