#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="Diophantine",
    version="0.1.1",
    py_modules=['diophantine'],
    author="Thomas G. Close",
    author_email="tom.g.close@gmail.com",
    description=(
        "A python package for finding small solutions of systems of "
        "diophantine (integer algebra) equations"),
    long_description=open("README.rst").read(),
    license="MIT",
    keywords=["mathematics", "diophantine", "algebra", "integer",
              "systems"],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Topic :: Scientific/Engineering'],
    python_requires='>=3.6, <4',
    install_requires=['sympy']
)
