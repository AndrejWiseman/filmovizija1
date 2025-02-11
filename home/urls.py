from django.urls import path
from .views import index, filmovi, domaci_filmovi, serije, domace_serije, tagovi, filmovi_detaljno, rezultati_pretrage

urlpatterns = [
    path('', index, name='index'),
    path('filmovi/', filmovi, name='filmovi'),
    path('domaci-filmovi/', domaci_filmovi, name='domaci-filmovi'),
    path('serije/', serije, name='serije'),
    path('domace-serije/', domace_serije, name='domace-serije'),
    path('zanr/<str:tag_name>', tagovi, name='tagovi'),
    path('<slug:slug>', filmovi_detaljno, name='filmovi-detaljno'),
    path('rezultati-pretrage/', rezultati_pretrage, name='rezultati-pretrage'),

]
