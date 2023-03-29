from django import template

register = template.Library()

@register.filter()
def new_frames(value):
    return value-2