from django.shortcuts import render, get_object_or_404
from itertools import chain
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from taggit.models import Tag
from django.db.models import Count, Q

from .models import Filmovi, DomaciFilmovi, Serije, DomaceSerije


def index(request):

    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')

    queryset = sorted(list(filmovi_list) + list(domaci_filmovi) + list(serije) + list(domace_serije), key=lambda x: x.dodano, reverse=True)

    novo = queryset[:3]

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))

    total_filmova = len(queryset)

    paginator = Paginator(queryset, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'queryset': queryset,
        'filmovi_list': filmovi_list,
        'novo': novo,
        'all_tags': all_tags,
        'total_filmova': total_filmova,
        'show_header': True,
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)



def filmovi(request):

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))
    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')
    queryset = sorted(list(filmovi_list) + list(domaci_filmovi) + list(serije) + list(domace_serije), key=lambda x: x.dodano, reverse=True)

    total_filmova = len(filmovi_list)

    paginator = Paginator(filmovi_list, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'all_tags': all_tags,
        'queryset': queryset,
        'filmovi_list': filmovi_list,
        'total_filmova': total_filmova,
        'show_header': False,
        'page_obj': page_obj,
    }
    return render(request, 'filmovi.html', context)



def domaci_filmovi(request):

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))

    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')
    queryset = sorted(list(filmovi_list) + list(domaci_filmovi) + list(serije) + list(domace_serije), key=lambda x: x.dodano, reverse=True)

    total_filmova = len(domaci_filmovi)

    paginator = Paginator(filmovi_list, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'all_tags': all_tags,
        'queryset': queryset,
        'total_filmova': total_filmova,
        'domaci_filmovi': domaci_filmovi,
        'show_header': False,
    }
    return render(request, 'domaci-filmovi.html', context)



def filmovi_detaljno(request, slug):

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))
    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')

    queryset = list(chain(filmovi_list, domaci_filmovi, serije, domace_serije))

    film = None
    for model in [Filmovi, DomaciFilmovi, Serije, DomaceSerije]:
        try:
            film = get_object_or_404(model, slug=slug)
            break
        except:
            continue

    if not film:
        raise Http404("Film nije nadjen")


    zanrovi = film.tags.all()

    # Filtriranje sličnih filmova po tagovima
    slicni_filmovi = []
    for item in queryset:
        if item.slug != film.slug and any(tag in item.tags.all() for tag in zanrovi):
            slicni_filmovi.append(item)

    slicni_filmovi = slicni_filmovi[:3]

    context = {
        'all_tags': all_tags,
        'queryset': queryset,
        'filmovi_list': filmovi_list,
        # 'total_filmova': total_filmova,
        'film': film,
        'zanrovi': zanrovi,
        'show_header': False,
        'slicni_filmovi': slicni_filmovi,
    }
    return render(request, 'filmovi-detaljno.html', context)



def serije(request):

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))
    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')
    queryset = sorted(list(filmovi_list) + list(domaci_filmovi) + list(serije) + list(domace_serije), key=lambda x: x.dodano, reverse=True)

    total_filmova = len(serije)

    context = {
        'all_tags': all_tags,
        'queryset': queryset,
        'total_filmova': total_filmova,
        'serije': serije,
        'show_header': False,
    }
    return render(request, 'serije.html', context)



def domace_serije(request):

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))
    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')
    queryset = sorted(list(filmovi_list) + list(domaci_filmovi) + list(serije) + list(domace_serije), key=lambda x: x.dodano, reverse=True)

    total_filmova = len(serije)

    context = {
        'all_tags': all_tags,
        'queryset': queryset,
        'total_filmova': total_filmova,
        'domace_serije': domace_serije,
        'show_header': False,
    }
    return render(request, 'domace-serije.html', context)



def rezultati_pretrage(request):

    query = request.GET.get('search')

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))
    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')
    queryset = sorted(list(filmovi_list) + list(domaci_filmovi) + list(serije) + list(domace_serije),
                      key=lambda x: x.dodano, reverse=True)


    if query:
        # queryset = [item for item in queryset if query.lower() in item.naslov.lower() or query.lower() in item.originalni_naslov.lower()]
        queryset = [item for item in queryset if query.lower() in item.naslov.lower() or (
                    hasattr(item, 'originalni_naslov') and query.lower() in item.originalni_naslov.lower())]

    context = {
        'all_tags': all_tags,
        'queryset': queryset,
        # 'total_filmova': total_filmova,
        'domace_serije': domace_serije,
        'show_header': False,
    }
    return render(request, 'rezultati-pretrage.html', context)



def tagovi(request, tag_name):

    filmovi_list = Filmovi.objects.all().order_by('-dodano')
    domaci_filmovi = DomaciFilmovi.objects.all().order_by('-dodano')
    serije = Serije.objects.all().order_by('-dodano')
    domace_serije = DomaceSerije.objects.all().order_by('-dodano')
    queryset = sorted(list(filmovi_list) + list(domaci_filmovi) + list(serije) + list(domace_serije), key=lambda x: x.dodano, reverse=True)

    filtrirani_tagovi = [item for item in queryset if tag_name in item.tags.names()]

    total_filmova = len(filtrirani_tagovi)

    all_tags = Tag.objects.annotate(ukupno_tagova=Count('taggit_taggeditem_items'))

    context = {
        'filtrirani_tagovi': filtrirani_tagovi,
        'all_tags': all_tags,
        'total_filmova': total_filmova,
        'tag_name': tag_name,
        'queryset': queryset,
        'show_header': False,
    }
    return render(request, 'tagovi.html', context)
