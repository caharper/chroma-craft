from setuptools import setup, find_packages
from setuptools.dist import Distribution
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name="chroma_craft",
    version="0.1",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/caharper/chroma-craft.git",
    authors=[
        "Clayton Harper",
    ],
    author_emails=[
        "caharper@smu.edu",
    ],
    license="MIT License",
    install_requires=["numpy>=1.20.1", "colorspacious>=1.1.2", "matplotlib>=3.3.4"],
    extras_require={},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization"
        "Topic :: Software Development",
    ],
    python_requires=">=3.7",
    distclass=Distribution,
    packages=find_packages(exclude=("*_test.py",)),
    include_package_data=True,
)
