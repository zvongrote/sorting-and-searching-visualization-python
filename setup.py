from setuptools import setup

# Package meta-data
NAME = 'sscommon'
VERSION = '0.1'
DESCRIPTION = 'Helper classes and functions for displaying the sorting and searching algorithms.'
REQUIRES_PYTHON = '>=3.5.0' # colorama requires 3.5.0 or higher
REQUIRED = ['colorama']
PACKAGES = ['sscommon']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    install_requires=REQUIRED,
    packages=PACKAGES,
    python_requires=REQUIRES_PYTHON
)