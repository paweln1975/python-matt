from django import template

register = template.Library()

@register.filter
def getattr(form, name):
    return form[name]

