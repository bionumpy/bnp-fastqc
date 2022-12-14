#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Ivar Grytten",
    author_email='ivargry@ifi.uio.no',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Example implementation of fastqc using BioNumPy",
    entry_points={
        'console_scripts': [
            'bnp_fastqc=bnp_fastqc.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bnp_fastqc',
    name='bnp_fastqc',
    packages=find_packages(include=['bnp_fastqc', 'bnp_fastqc.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ivargr/bnp_fastqc',
    version='0.1.0',
    zip_safe=False,
)
