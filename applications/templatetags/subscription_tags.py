from django import template
# from ..event.models import Subscriber, TicketCollector
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

# @register.simple_tag()
# def organization_subscribed(pk, profile):
#     try:
#         return Subscriber.objects.get(organization=pk, profile=profile)
#     except ObjectDoesNotExist:
#         return False

# @register.simple_tag()
# def event_subscribed(pk, profile):
#     try:
#         return Subscriber.objects.get(event=pk, profile=profile)
#     except ObjectDoesNotExist:
#         return False

# @register.simple_tag()
# def event_get_ticket(event, profile):
#     return TicketCollector.objects.filter(buyer=profile, ticket__event=event, active=True)


@register.filter
def to_dot(value):
    return str(value).replace(",",".")