# Chroma-Craft

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Development Status](https://img.shields.io/badge/development-active-brightgreen.svg)

## Description

Chroma-Craft creates perceptually-distinct color palettes for data visualization in Python. While many great plotting libaries exist, they often rely on fixed color palettes and generally have few colors.  These colors often conflict with one another.  Chroma-Craft allows users to create a palette of colors that are perceptually distinct from one another.  This allows for more colors to be used in a plot without sacrificing readability.

## Installation

### GitHub

In your environment, run:

```bash
git clone https://github.com/caharper/chroma-craft.git
cd chroma-craft
python setup.py develop
```

### PyPI

⚠️ Coming soon! ⚠️

## Usage

Simple examples are shown below.  For more examples, see the [examples](./examples) directory.

### Creating a Random Palette

```python
import chroma_craft as cc

# Create a palette with 5 colors
palette = cc.generate_palette(3, distance=80, color_format="rgb", seed=11)
```

`Note:` a random seed can be provided to ensure reproducibility.  Distance is the distance between colors in the palette.  A larger distance will result in more distinct colors.  If the distance is too large, a warning message will be displayed.  Too large of distances can result in colors that are too similar to each other due to clipping in the RGB color space.  Distance is defined as the Delta-E color difference between colors in the palette.  

### Creating a Palette from a Base Color

```python
import chroma_craft as cc

# Create a palette with 15 total colors
palette = cc.generate_palette_with_base(
    np.array([66.0, 128.0, 99.0]), 15, distance=50, color_format="rgb", seed=37
)
```

### Visualizing a Palette

```python
import chroma_craft as cc

cc.visualize_palette(palette, show=True)
```

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes thoroughly.
5. Submit a pull request.
6. Add caharper as a reviewer.

Please ensure your code adheres to the project's coding style and conventions.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out:

- Email: [caharper@smu.edu](mailto:caharper@smu.edu)
- GitHub: [caharper](https://github.com/caharper)
