#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


with open("README.md", "r") as readme:
    long_description = readme.read()


setup(
    name='gep-python-coding-challenge',
    version='0.0.1',
    license='MIT',
    description='This package contains the beginner level assignments of the GEP Python Coding Challenge.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='JcS',
    author_email='joyce@hey.com',
    url='https://github.com/Joyce-NL/gep-python-coding-challenge',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Other/Nonlisted Topic',
        'Private :: Do Not Upload',
    ],
    project_urls={
        'Changelog': 'https://github.com/Joyce-NL/gep-python-coding-challenge/blob/master/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/Joyce-NL/gep-python-coding-challenge/issues',
    },
    keywords=[
        'Euler', 'Project Euler'
    ],
    python_requires='>=3.8',
    install_requires=[],
    extras_require={},
)
