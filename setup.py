# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = "Look in methoology.md"

setup(
    name='edc-registration',
    version='0.0.1',
    description='Energy Data Centre user registration',
    long_description=long_description,

    # The project's main homepage.
    url='http://www.ceda.ac.uk',
    # Author details
    author='Andrew Harwood',
    author_email='a.s.harwood@stfc.ac.uk',
    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='ceda',
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
    include_package_data = True,
    
)
