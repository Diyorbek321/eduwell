from django.urls import path
from app.views import HomePageTemplateView, AboutPageTemplateView,ContactPageTemplateView,ServiceOageTemplateView

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('about/', AboutPageTemplateView.as_view(), name='about_page'),
    path('contact/', ContactPageTemplateView.as_view(), name='contact_page'),
    path('service/', ServiceOageTemplateView.as_view(), name='service_page')
]
