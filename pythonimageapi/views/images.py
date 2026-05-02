from django.http import HttpResponse

from pythonimageapi.images.svg_generator import SvgGenerator


def svg(request, size: int, color: str):
    generator = SvgGenerator()

    return HttpResponse(generator.generate_svg(int(size), int(size), color, request.GET['text']),
                        content_type='image/svg+xml')
