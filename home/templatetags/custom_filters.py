from django import template
from home.models import Serije, DomaceSerije

register = template.Library()

@register.filter(name='is_serija')
def is_serija(obj):
    # Proveri da li je objekat serija (bilo strana ili domaća)
    return isinstance(obj, (Serije, DomaceSerije))
