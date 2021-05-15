import re

from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    """Check if a pattern mathes the request path."""
    
    if re.search(pattern, request.path):
        return "active"
    return None