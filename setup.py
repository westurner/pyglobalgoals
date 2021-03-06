#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'beautifulsoup4',
    'docutils',
    'jinja2',
    'requests',
    'requests_cache',
    #'tweepy',
]

test_requirements = [
]

setup(
    name='pyglobalgoals',
    version='0.2.5',
    description=("pyglobalgoals is a Python package, Python module, and a set of Python Jupyter notebooks for working with JSON-LD, RDFa, schema.org and The Global Goals For Sustainable Development"),
    long_description=readme + '\n\n' + history,
    author="Wes Turner",
    author_email='wes@wrd.nu',
    url='https://github.com/westurner/pyglobalgoals',
    packages=[
        'pyglobalgoals',
    ],
    package_dir={'pyglobalgoals':
                 'pyglobalgoals'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pyglobalgoals',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
