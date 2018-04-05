# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from distutils.core import setup


setup(
    name='django-measurement',
    version='0.1',
    url='https://github.com/webit-mdowney/django-measurement',
    packages=[
        'django_measurement',
    ],
    install_requires=[
        'measurement',
    ],
)
