from django.http import FileResponse
from django.views import View

from pythonimageapi.images.svg_generator import SvgGenerator


class SvgImages(View):
    def get(self, request, size: str | None = None, color: str | None = None) -> FileResponse:
        generator = SvgGenerator()

        args = {}

        if 'text' in request.GET:
            args['text'] = request.GET['text']

        if color is not None:
            args['color'] = color

        if size is not None:
            if "x" in size:
                parts = size.split('x')

                args['width'] = int(parts[0])
                args['height'] = int(parts[1])
            else:
                args['width'] = int(size)
                args['height'] = int(size)

        return FileResponse(generator.generate_svg(**args), content_type='image/svg+xml')
