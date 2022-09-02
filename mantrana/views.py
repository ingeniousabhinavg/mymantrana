from django.shortcuts import render
from .models import Counsellors, Services, FAQ

# Create your views here.

servicesData = Services.objects.all()
counsellorsData = Counsellors.objects.all()
faqData = FAQ.objects.all()

context = {
        'servicesData':servicesData,
        'counsellorsData':counsellorsData,
        'faqData':faqData
}

def index(request):
    return render(request, 'index.html',context)


def services(request):
    return render(request, 'services.html',context)