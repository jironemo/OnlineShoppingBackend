from django import template

register = template.Library()

@register.filter
def get_first_value(d):
    return d.split("-")[0]