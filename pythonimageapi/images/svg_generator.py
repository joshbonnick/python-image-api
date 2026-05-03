import re
from html import escape

HEX_PATTERN = re.compile(r'^#?[0-9a-fA-F]{6}$|^#?[0-9a-fA-F]{3}$')

class SvgGenerator:
    def __init__(self):
        pass

    def generate_svg(self, width: int = 300, height: int = 300, color: str = "e3e3e3", text: str | None = None,
                     font_settings: dict[str, str] | None = None) -> str:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")

        color_format = self.detect_color_format(color)
        if color_format is 'hex':
            color = color.lstrip('#')
        elif color_format is 'rgb' or color_format is 'rgba':
            color = color.strip(')').strip('rgb(').strip(' ').split(',')
            color = self.rgb_to_hex(*color)

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

    def detect_color_format(self, value: str | bytes) -> str | None:
        """
        Detects a color format.

        Returns:
            'hex' -> #RRGGBB or RRGGBB
            'rgb' -> rgb(r, g, b) or rgb(r, g, b, a)
            'rgba'-> rgba(r, g, b, a)
            None -> invalid
        """
        value = str(value).strip()

        # HEX
        if HEX_PATTERN.fullmatch(value):
            return "hex"

        # rgb / rgba parsing
        if value.startswith("rgb"):
            inside = value[value.find("(") + 1:value.rfind(")")]
            parts = [p.strip() for p in inside.split(",")]

            if len(parts) == 3:
                return "rgb"

            if len(parts) == 4:
                return "rgba"

        return None

    def rgb_to_hex(self, r: int, g: int, b: int, a: int | None = None) -> str:
        """
        Converts RGB or RGBA (0–255 alpha) to hex.

        - RGB -> #RRGGBB
        - RGBA -> #RRGGBBAA
        """
        if not all(0 <= v <= 255 for v in (r, g, b)):
            raise ValueError("RGB values must be in range 0–255")

        if a is None:
            return f"#{r:02x}{g:02x}{b:02x}"

        if not (0 <= a <= 255):
            raise ValueError("Alpha must be in range 0–255")

        return f"#{r:02x}{g:02x}{b:02x}{a:02x}"
