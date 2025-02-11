from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Count, Q

from .models import Filmovi

# Create your views here.
def index(request):

    # filmovi = Filmovi.objects.all()

    context = {
        # 'filmovi': filmovi,
    }
    return render(request, 'index.html', context)


# ovo je sa proba grid doslo
