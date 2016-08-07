"""OpenBikes packaging instructions."""

from setuptools import setup, find_packages
from obpy import __version__, __author__, __project__

README = 'README.md'
REQUIREMENTS = [
    'requests'
]


def long_description():
    """Insert README.md into the package."""
    try:
        with open(README) as readme_fd:
            return readme_fd.read()
    except IOError:
        return 'Failed to read README.md'


setup(
    name=__project__,
    version=__version__,
    description='OpenBikes API library',
    author=__author__,
    author_email='contact.openbikes@gmail.com',
    packages=find_packages(),
    long_description=long_description(),
    install_requires=REQUIREMENTS,
)
