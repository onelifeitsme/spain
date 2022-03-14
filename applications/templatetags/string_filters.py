#!coding:utf-8
from django import template
from num2words import num2words
from unidecode import unidecode
from django.template.defaultfilters import slugify

register = template.Library()

@register.filter
def slug(value):
    return slugify(unidecode(value))


@register.filter
def selected_choice(form, field_name):
    if field_name in form.data and form.data[field_name]:
        return dict(form.fields[field_name].choices).get(int(form.data[field_name]))

    if 'filter' in form.request.session and field_name in form.request.session['filter'] and form.request.session['filter'][field_name]:
        return dict(form.fields[field_name].choices).get(int(form.request.session['filter'][field_name]))

@register.filter
def convert_num_to_words(value):
    return num2words(value, lang='ru')


@register.filter
def subtract(value, arg):
    return float("%.2f" % value) - float("%.2f" % arg)

@register.filter
def multiply(value, arg):
    return float("%.2f" % value) * float("%.2f" % arg)

@register.filter
def divide(value, arg):
    return float("%.2f" % value) / float("%.2f" % arg)

@register.filter
def subtract_int(value, arg):
    return int(value) - int(arg)

@register.filter
def multiply_int(value, arg):
    return int(value) * int(arg)

@register.filter
def divide_int(value, arg):
    return int(value) / int(arg)


@register.filter
def split(value, separator=' '):
    return value.split(separator)


@register.filter
def in_list(value, the_list):
    value = str(value)
    return value in the_list.split(',')


@register.filter
def to_bool(value):
    return bool(value)

@register.filter
def to_str(value):
    return str(value)

@register.filter
def next(iterator):

    try:
        return iterator.next()
    except:
        return ''


@register.filter
def get_end(value, type):

    ends = [
        {
            0: u'ий',
            1: u'ие',
            2: u'ия',
            3: u'ия',
            4: u'ия',
            5: u'ий',
            6: u'ий',
            7: u'ий',
            8: u'ий',
            9: u'ий',
        },
        {
            0: u'ов',
            1: u'',
            2: u'а',
            3: u'а',
            4: u'а',
            5: u'ов',
            6: u'ов',
            7: u'ов',
            8: u'ов',
            9: u'ов',
        },
        {
            0: u'ей',
            1: u'ь',
            2: u'ля',
            3: u'ля',
            4: u'ля',
            5: u'ей',
            6: u'ей',
            7: u'ей',
            8: u'ей',
            9: u'ей',
        },
    ]

    val = repr(int(value))

    if int(value) > 10:

        tens = int(val[-2:])

        if tens < 20:
            return ends[type][0]

    return ends[type][int(val[-1])]
