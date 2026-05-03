import re


def detect_color_format(value: str | bytes) -> str | None:
    """
    Detects a color format.

    Returns:
        'hex' -> #RRGGBB or RRGGBB
        'rgb' -> rgb(r, g, b) or rgb(r, g, b, a)
        'rgba'-> rgba(r, g, b, a)
        None -> invalid
    """
    hex_pattern = re.compile(r'^#?[0-9a-fA-F]{6}$|^#?[0-9a-fA-F]{3}$')

    value = str(value).strip()

    # HEX
    if hex_pattern.fullmatch(value):
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


def rgb_to_hex(r: int, g: int, b: int, a: int | None = None) -> str:
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
