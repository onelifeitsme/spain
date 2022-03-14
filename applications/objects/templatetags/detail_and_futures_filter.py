import datetime

from django import template
register = template.Library()

@register.filter('get_daf')
def get_daf(value, arg):
    need_obj = None
    for obj in value:
        if obj.type.name == arg:
            need_obj = obj
    return need_obj

@register.filter('get_daf_single')
def get_daf_single(value, arg):
    need_obj = None
    daf = value.detailandfeature_set.filter(rent_object=value)
    if daf.exists:
        for i in daf:
            if i.type.name == arg:
                return i.property


@register.filter('date_format')
def current_time(value):
    if value:
        return value.strftime('%dTH %B %Y')
    else:
        return None


@register.filter('date_expired')
def date_expired(value):
    if datetime.datetime.now().date() > value.checkout:
        return False
    else:
        return True