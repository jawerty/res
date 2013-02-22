#!/usr/bin/env python

from setuptools import setup

setup(name='res',
      version='0.1.0',
      description='res is a tiny command line REST client',
      author='Jared Wright',
      license='MIT',
      keywords = "res rest client command line tool cli minimalistic API http calls",
      author_email='jawerty210@gmail.com',
      url='http://github.com/jawerty/res',
      scripts=['res.py', 'colors.py'],
      install_requires=['docopt', 'requests'],
      entry_points = {
        'console_scripts': [
            'res = res:main'
        ],
	  }
)
