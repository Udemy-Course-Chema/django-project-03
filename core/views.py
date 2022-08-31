from webbrowser import get
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/home.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = 'Web Playground'
    #     return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'webPlayground'})
    


class SamplePageView(TemplateView):
    template_name: str = "core/sample.html"