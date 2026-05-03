from django.http import FileResponse

from pythonimageapi.images.svg_generator import SvgGenerator


def svg(request, size: str, color: str) -> FileResponse:
    generator = SvgGenerator()

    if "x" in size:
        parts = size.split('x')

        width = int(parts[0])
        height = int(parts[1])
    else:
        width = int(size)
        height = int(size)

    text = None
    if 'text' in request.GET:
        text = request.GET['text']

    return FileResponse(generator.generate_svg(width, height, color, text), content_type='image/svg+xml')
