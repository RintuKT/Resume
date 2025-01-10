from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by the specified delimiter"""
    return [x.strip() for x in value.split(arg)]
