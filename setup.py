#!/usr/bin/env python

from setuptools import setup

setup(
    name='Blog',
    version='1.0',
    description='Lawson blog',
    author='Lawson',
    author_email='pansen428@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django>=1.6.8',
	                  'beautifulsoup4>=4.1',
                      'django-contrib-comments>=1.5',
                      'django-mptt>=0.5.1',
                      'django-tagging>=0.3.2',
                      'django-xmlrpc>=0.1.5',
                      'pyparsing>=2.0.1',
                      'pytz>=2013b',
					  'Markdown >= 2.3.1',],
)
