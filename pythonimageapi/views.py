from django.http import JsonResponse
from django.urls import get_resolver, URLPattern, URLResolver


def extract_patterns(patterns, prefix=""):
    routes = []

    for pattern in patterns:
        if isinstance(pattern, URLPattern):
            routes.append(prefix + str(pattern.pattern))
        elif isinstance(pattern, URLResolver):
            routes.extend(
                extract_patterns(
                    pattern.url_patterns,
                    prefix + str(pattern.pattern)
                )
            )

    return routes


def index(request):
    resolver = get_resolver()

    routes = [route for route in extract_patterns(resolver.url_patterns) if 'admin/' not in route]

    return JsonResponse(routes, json_dumps_params={"indent": True}, safe=False)
