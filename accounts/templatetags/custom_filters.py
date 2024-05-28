from django import template

register = template.Library()

@register.filter
def get_color(colors, index):
    return colors[index % len(colors)]