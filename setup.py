#!/usr/bin/env python

from __future__ import absolute_import

"""
sentry-auth-github
==================

:copyright: (c) 2016 Functional Software, Inc
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=9.0.0',
]

test_requires = [
    "pytest==4.6.5",
    "pytest-cov==2.5.1",
]

setup(
    name='sentry-auth-github',
    version='0.1.0',
    author='Sentry',
    author_email='support@getsentry.com',
    url='https://www.getsentry.com',
    description='GitHub authentication provider for Sentry',
    long_description=__doc__,
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'tests': test_requires,
    },
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'auth_github = sentry_auth_github',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
