#!/usr/bin/env python
"""
sentry-auth-github
==================

:copyright: (c) 2015 Functional Software, Inc
"""
from setuptools import setup, find_packages


tests_require = [
    'pytest',
    'mock',
]

install_requires = [
    'sentry',
]

setup(
    name='sentry-auth-github',
    version='0.1.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='https://www.getsentry.com',
    description='GitHub authentication provider for Sentry',
    long_description=__doc__,
    license='',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
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
