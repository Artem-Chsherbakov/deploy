from django import template

register = template.Library()

@register.filter
def value_from_model(model, field):
    print("TAGACTIVATED!!!!!!!!!!!!!!!!!!!!!")
    return getattr(model, field)