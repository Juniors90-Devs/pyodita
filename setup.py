#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __doc__: str
"""
Pyodita (Building)
======================

A sample Python project.

"""

# Python tiene librerias standar

from setuptools import setup, find_packages  # noqa


setup(
    name='Pyodita',
    version='0.0.1a'
    description='A sample Python project',
    long_description=__doc__,
    long_description_content_type='text/x-rst',
    url='https://github.com/juniors90/pytodita',
    author='Ferreira Juan David',
    author_email='juandavid9a0@gmail.com',
    license='MIT',
    classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers :: Researchs',
    'Topic :: Software Development :: Build Tools :: Biotecnology',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    ],
    keywords='sample setuptools development',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },
    packages=find_packages(include=['pyodita', 'pyodita.*']),
    install_requires=[],
    python_requires='>=3.7',
)


