from django import template

register = template.Library()

@register.filter(name='rat')
def cut(value, arg):
    """
    This cuts out all the values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('rat', cut)
