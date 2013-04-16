#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

import django_sendmail_backend


PROJECT_DIR = os.path.dirname(__file__)

setup(
    name='django_sendmail_backend',
    version=django_sendmail_backend.__version__,
    url='https://github.com/perenecabuto/django-sendmail-backend.git',
    author="Felipe Ramos",
    author_email="perenecabuto@gmail.com",
    description="Its a simple command line sendmail backend for Django",
    long_description=open(os.path.join(PROJECT_DIR, 'README.md')).read(),
    keywords="Django, Python, sendmail, EMAIL_BACKEND, command line, mta",
    license='BSD',
    packages=find_packages(exclude=["tests/"]),
    include_package_data=True,
    install_requires=['Django>=1.4'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)

