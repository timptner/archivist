from django.views import generic



class LandingPage(generic.TemplateView):
    template_name = 'people/landing_page.html'
