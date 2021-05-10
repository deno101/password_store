from django.http import HttpResponseBadRequest


def validate_method(method):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if not request.method == method:
                return HttpResponseBadRequest()
            else:
                return function(request, args, kwargs)

        return wrapper

    return decorator
