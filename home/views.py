from django.shortcuts import render
from .models import Filmovi

# Create your views here.
def index(request):

    filmovi = Filmovi.objects.all()

    context = {
        'filmovi': filmovi,
    }
    return render(request, 'index.html', context)
