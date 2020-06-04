from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='capitalize')
@stringfilter
def capitalize_this(value):
    return value.capitalize()


@register.filter(name='grammtolitr')
# @stringfilter
def grammtolitr(value):
        return value/1000
