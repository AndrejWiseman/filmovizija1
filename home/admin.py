from django.contrib import admin
from .models import Filmovi, Zanrovi


class FilmoviAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("naslov", )}
    list_display = ['naslov']



# class EpizodaInline(admin.StackedInline):
#     model = Epizoda
#     extra = 0
#     # fields = ['sezona', 'ep', 'epizode_preuzmi', 'epizode_link']
#     fields = ['sezona', 'ep']
#
#
# class SerijeAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     # ordering = ('-date',)
#     prepopulated_fields = {"slug": ("title", )}
#     inlines = [EpizodaInline]


admin.site.register(Filmovi, FilmoviAdmin)
admin.site.register(Zanrovi)
