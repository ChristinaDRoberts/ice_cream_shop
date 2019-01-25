from django.shortcuts import render
from django.views.generic import TemplateView

from .models import IceCream

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        daily_creams = IceCream.objects.filter(available='Daily')
        weekly_creams = IceCream.objects.filter(available='Weekly')
        seasonal_creams = IceCream.objects.filter(available='Seasonal')
        featured_creams = IceCream.objects.filter(featured=True)

        context = {
            'daily': daily_creams,
            'weekly': weekly_creams,
            'seasonal': seasonal_creams,
            'featured': featured_creams,
        }



        return context

    # daily = ['pumpkin', 'butter pecan']
    # weekly = ['blueberry cheesecake', 'almond chocolate coconut']
    # seasonal = ['toffee bar', 'banana nut bread']
