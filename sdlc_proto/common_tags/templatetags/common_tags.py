from sdlc_proto.common_tags.apps import register

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def dictLookup(value, arg):
    return value.get(arg)

@register.filter
def getField(value, arg):
    result = None
    try:
        result = getattr(value, arg)
    except AttributeError:
        pass
    return result