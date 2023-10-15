import numpy as np
from chroma_craft.color_utils.color_space import (
    hex_to_rgb,
    rgb_to_hex,
    cielab_to_rgb,
)
from chroma_craft.math.utils import generate_evenly_spaced_points_on_sphere
from colorspacious import cspace_convert
import warnings


def generate_palette(n_colors, distance=3, color_format="rgb", seed=None):
    np.random.seed(seed)

    # Generate random base CIELab color
    lightness = np.random.uniform(40, 60)  # must be between 0 and 100
    green_magenta = np.random.uniform(-20, 20)  # must be between -128 and 128
    blue_yellow = np.random.uniform(-20, 20)  # must be between -128 and 128

    base_color = np.array([lightness, green_magenta, blue_yellow])

    final_colors = generate_palette_with_base(
        base_color,
        n_colors,
        distance,
        color_format,
        base_color_format="cielab",
        seed=seed,
    )

    return final_colors


def generate_palette_with_base(
    base_color,
    n_total_colors,
    distance=3,
    color_format="rgb",
    base_color_format="rgb",
    seed=None,
):
    if base_color_format != "cielab":
        if base_color_format == "hex":
            base_color = hex_to_rgb(base_color)
        elif base_color_format == "rgb":
            pass
        else:
            raise ValueError(f"Unknown color format {base_color_format}")

        base_color = cspace_convert(base_color, "sRGB255", "CIELab")
        base_color = np.clip(base_color, [0, -128, -128], [100, 128, 128])

    # Generate remaining CIELab colors
    distant_colors = generate_evenly_spaced_points_on_sphere(
        base_color, n_total_colors - 1, distance, seed=seed
    )

    # If any values are out of range, raise warning
    if (
        np.any(np.abs(distant_colors[:, 1:]) > 128)
        or np.any(distant_colors[:, 0] > 100)
        or np.any(distant_colors[:, 0] < 0)
    ):
        warnings.warn(
            "Some generated colors are out of range for CIELab.  This may cause"
            " unexpected close colors.  Try decreasing the distance parameter."
        )

    # Clip values to ensure they are within CIELab range
    distant_colors = np.clip(distant_colors, [0, -128, -128], [100, 128, 128]).tolist()

    colors = [base_color] + distant_colors

    # Convert to colorspace
    if color_format == "hex":
        final_colors = [rgb_to_hex(cielab_to_rgb(color)) for color in colors]
    elif color_format == "rgb":
        final_colors = [cielab_to_rgb(color) for color in colors]
    else:
        raise ValueError(f"Unknown color format {color_format}")

    return final_colors
