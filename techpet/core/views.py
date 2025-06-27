from django.shortcuts import render

# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views import View

from .models import PetData

# Create your views here.

def Home(request):
    return render(request, 'core/index.html')

class PetsDetail(DetailView):
    model = PetData
    template_name = 'core/petsUI/petsview.html'
    context_object_name = 'pet'