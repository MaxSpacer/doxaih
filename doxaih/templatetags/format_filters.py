from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='capitalize')
@stringfilter
def capitalize_this(value):
    return value.capitalize()
