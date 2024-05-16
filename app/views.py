from django.shortcuts import render
from django.views.generic import TemplateView

from app.forms import ContactForm


# Create your views here.
class HomePageTemplateView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return self.render_to_response({'form': form})


class AboutPageTemplateView(TemplateView):
    template_name = 'about-us.html'


class ContactPageTemplateView(TemplateView):
    template_name = 'contact-us.html'


class ServiceOageTemplateView(TemplateView):
    template_name = 'our-services.html'

