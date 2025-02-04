#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import re
try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False

src = io.open('jsonpatch.py', encoding='utf-8').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", src))
docstrings = re.findall('"""([^"]*)"""', src, re.MULTILINE | re.DOTALL)

PACKAGE = 'jsonpatch'

MODULES = (
        'jsonpatch',
)

REQUIREMENTS = list(open('requirements.txt'))

if has_setuptools:
    OPTIONS = {
        'install_requires': REQUIREMENTS
    }
else:
    OPTIONS = {}

AUTHOR_EMAIL = metadata['author']
VERSION = metadata['version']
WEBSITE = metadata['website']
LICENSE = metadata['license']
DESCRIPTION = docstrings[0]

# Extract name and e-mail ("Firstname Lastname <mail@example.org>")
AUTHOR, EMAIL = re.match(r'(.*) <(.*)>', AUTHOR_EMAIL).groups()

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print('warning: pypandoc module not found, could not convert '
          'Markdown to RST')
    read_md = lambda f: open(f, 'r').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
]


setup(name=PACKAGE,
      version=VERSION,
      description=DESCRIPTION,
      long_description=read_md('README.md'),
      author=AUTHOR,
      author_email=EMAIL,
      license=LICENSE,
      url=WEBSITE,
      py_modules=MODULES,
      package_data={'': ['requirements.txt']},
      scripts=['bin/jsondiff', 'bin/jsonpatch'],
      classifiers=CLASSIFIERS,
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
      project_urls={
          'Website': 'https://github.com/stefankoegl/python-json-patch',
          'Repository': 'https://github.com/stefankoegl/python-json-patch.git',
          'Documentation': "https://python-json-patch.readthedocs.org/",
          'PyPI': 'https://pypi.org/pypi/jsonpatch',
          'Tests': 'https://travis-ci.org/stefankoegl/python-json-patch',
          'Test Coverage': 'https://coveralls.io/r/stefankoegl/python-json-patch',
      },
      **OPTIONS
)
