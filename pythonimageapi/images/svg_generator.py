import re
from html import escape

HEX_PATTERN = re.compile(r'^#?[0-9a-fA-F]{6}$|^#?[0-9a-fA-F]{3}$')
RGB_PATTERN = re.compile(
    r'^rgb\(\s*'
    r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\s*,\s*'
    r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\s*,\s*'
    r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\s*'
    r'\)$'
)


class SvgGenerator:
    def __init__(self):
        pass

    def generate_svg(self, width: int, height: int, color) -> str:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")

        safe_color = escape(color)

        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}">'
            f'<rect width="{width}" height="{height}" fill="{safe_color}" />'
            f'</svg>'
        )

    def isHex(self, color: str | [int]) -> bool:
        return type(color)
