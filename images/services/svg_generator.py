from html import escape

from images.services.color import detect_color_format, rgb_to_hex


class SvgGenerator:
    def __init__(self):
        pass

    def generate_svg(self, width: int = 300, height: int = 300, color: str = "e3e3e3", text: str | None = None,
                     font_settings: dict[str, str] | None = None) -> str:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")

        color_format = detect_color_format(color)
        if color_format == 'hex':
            color = color.lstrip('#')
        elif color_format == 'rgb' or color_format == 'rgba':
            color = color.strip(')').strip('rgb(').strip(' ').split(',')
            color = rgb_to_hex(*color)

        safe_color = f'#{escape(color)}'

        if text is not None:
            text = escape(str(text))

        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}">',
            f'<rect width="{width}" height="{height}" fill="{safe_color}" />',
        ]

        font_setting_defaults = {
            "font_family": "Arial",
            "font_size": f"{min(width, height) // 2}px",
        }

        if font_settings is None:
            font_settings = font_setting_defaults.copy()

        if text is not None:  # only render text when non-empty / not None
            svg_parts.append(
                f'<text x="50%" y="50%" '
                f'dominant-baseline="middle" ' 
                f'text-anchor="middle" '
                f'fill="white" '
                f'font-size="{font_settings.get('font_size', font_setting_defaults.get('font_size'))}" '
                f'font-family="{font_settings.get('font_family', font_setting_defaults.get('font_family'))}, sans-serif">'
                f'{text}'
                f'</text>'
            )

        svg_parts.append('</svg>')

        return ''.join(svg_parts)