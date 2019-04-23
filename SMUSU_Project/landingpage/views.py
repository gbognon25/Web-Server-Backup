from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

def index(request):
    return render(request,"landingpage/Index.html")

class AboutPageView(TemplateView):
    template_name = "landingpage/About.html"
