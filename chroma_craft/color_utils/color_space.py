import numpy as np
from colorspacious import cspace_convert


def is_hex_color(color):
    if not isinstance(color, str):
        return False

    if color[0] != "#":
        return False, f"Hex color must start with '#', got {color}"

    if len(color) != 7:
        return False
    try:
        int(color[1:], 16)
    except ValueError:
        return False, f"Could not convert {color} to hex color"

    return True


def is_rgb_color(color):
    if not isinstance(color, tuple):
        return False, f"RGB color must be a tuple, got {color}"

    if len(color) != 3:
        return False, f"RGB color must have three elements, got {color}"

    for c in color:
        if not isinstance(c, int):
            return False, f"RGB color elements must be integers, got {color}"

        if c < 0 or c > 255:
            return False, f"RGB color elements must be between 0 and 255, got {color}"

    return True


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


def cielab_to_rgb(cielab):
    # Clip to be in range [0, 255]
    rgb = cspace_convert(cielab, "CIELab", "sRGB255")
    rgb = np.clip(rgb, 0, 255)
    return rgb.astype(int)
