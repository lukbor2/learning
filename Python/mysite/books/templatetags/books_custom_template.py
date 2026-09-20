from django import template

register = template.Library()

def cut(value, arg):
    """ Removes all values of arg from the given string. Example of a filter with argument """
    return value.replace(arg, '') 

def lower(value):
    """ Turns into lower case. Example of a filter without argument. """
    return value.lower()


register.filter('cut', cut)
register.filter('lower', lower)