from django.contrib import admin
from .models import Filmovi, DomaciFilmovi, Serije, DomaceSerije, Epizoda, DomaciEpizoda


class FilmoviAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("naslov", )}
    list_display = ['naslov']


class DomaciFilmoviAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("naslov", )}
    list_display = ['naslov']



class EpizodaInline(admin.StackedInline):
    model = Epizoda
    extra = 0
    fields = ['sezona', 'ep', 'link_gledaj', 'link_preuzmi']
class SerijeAdmin(admin.ModelAdmin):
    list_display = ['naslov']
    # ordering = ('-date',)
    prepopulated_fields = {"slug": ("naslov", )}
    inlines = [EpizodaInline]



class DomaciEpizodaInline(admin.StackedInline):
    model = DomaciEpizoda
    extra = 0
    fields = ['sezona', 'ep', 'link_gledaj', 'link_preuzmi']
class DomaceSerijeAdmin(admin.ModelAdmin):
    list_display = ['naslov']
    # ordering = ('-date',)
    prepopulated_fields = {"slug": ("naslov", )}
    inlines = [DomaciEpizodaInline]


admin.site.register(Filmovi, FilmoviAdmin)
admin.site.register(DomaciFilmovi, DomaciFilmoviAdmin)
admin.site.register(Serije, SerijeAdmin)
admin.site.register(DomaceSerije, DomaceSerijeAdmin)
