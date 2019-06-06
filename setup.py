
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

try:
    import unittest.mock
    has_mock = True
except ImportError:
    has_mock = False


__version__ = '1.0.0'

setup(
    name="madis-lib",
    version=__version__,
    author="Panagiotis Kanakakis",
    author_email="pkanakakis@di.uoa.gr",
    long_description_content_type="text/markdown",
    url="https://github.com/PanagiotisKanakakis/madis-lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[]
)

