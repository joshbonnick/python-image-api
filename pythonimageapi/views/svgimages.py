from django.http import FileResponse
from django.views import View

from pythonimageapi.images.svg_generator import SvgGenerator


class SvgImages(View):
    def get(self, request, size: str | None = None, color: str | None = None) -> FileResponse:
        generator = SvgGenerator()

        args = {}
        font_settings = {}

        if 'text' in request.GET:
            args['text'] = request.GET['text']

        if 'font_size' in request.GET:
            font_settings["font_size"] = request.GET['font_size']

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

        args['font_settings'] = font_settings

        return FileResponse(generator.generate_svg(**args), content_type='image/svg+xml')
