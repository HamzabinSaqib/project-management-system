from django import template

register = template.Library()

@register.simple_tag
def first_true(request):
    if not hasattr(request, "_first_true_has_been_called"):
        setattr(request, "_first_true_has_been_called", True)
        return True
    return False