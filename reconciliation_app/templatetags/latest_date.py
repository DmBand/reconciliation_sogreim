from django import template
from ..models import ReconciliationDate

register = template.Library()


@register.simple_tag()
def get_latest(product_id: int):
    r = ReconciliationDate.objects.filter(product=product_id)
    if r:
        return r.latest('date')
