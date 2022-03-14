# -*- coding: utf-8 -*-
import re
from django import template
# from ..organizator.models import PromoCode, PromoCodeType
# from ..event.models import SeatType
# from django.core.urlresolvers import reverse
from django.urls import reverse

register = template.Library()
import datetime

# @register.simple_tag()
# def get_color(id):
#     try:
#         return SeatType.objects.get(id=id)
#     except SeatType.DoesNotExist:
#         return ''

# @register.simple_tag
# def get_free_mailing_records(profile):
#     return PromoCode.get_free(profile, PromoCodeType.FREE_MAILING)

@register.filter
def get_place_email(place, org):
    if place and org:
        return place.get_email(org)

@register.filter
def get_place_phone(place, org):
    if place and org:
        return place.get_phone(org)

@register.filter
def get_place_site(place, org):
    if place and org:
        return place.get_site(org)

@register.filter
def get_place_vk(place, org):
    if place and org:
        return place.get_vk(org)

@register.filter
def get_place_tw(place, org):
    if place and org:
        return place.get_tw(org)

@register.filter
def get_place_fb(place, org):
    if place and org:
        return place.get_fb(org)

@register.filter
def get_place_inst(place, org):
    if place and org:
        return place.get_inst(org)

@register.filter
def get_place_phone(place, org):
    if place and org:
        return place.get_phone(org)

@register.filter
def plus_days(value, days):
    return value + datetime.timedelta(days=days)


@register.filter
def create_links(value):
    return re.sub(r'(https?://(?:[-\w./]|(?:%[\da-fA-Fа-яА-ЯёЁ]{2}))+)',
           r'<a href="' + reverse('leave_page') + r'?url=\1">\1</a>', value)


@register.simple_tag
def get_reservation_count(ticket, timeline):
    return ticket.get_reservation_count(timeline)


def get_parameters(parser, token):

    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError(
            "get_parameters tag takes at least 1 argument")
    return GetParametersNode(args[1].strip())


class GetParametersNode(template.Node):

    def __init__(self, field):
        self.field = field

    def render(self, context):
        request = context['request']
        getvars = request.GET.copy()

        if self.field in getvars:
            del getvars[self.field]

        if len(getvars.keys()) > 0:
            get_params = "%s&" % getvars.urlencode()
        else:
            get_params = ''

        return get_params


get_parameters = register.tag(get_parameters)