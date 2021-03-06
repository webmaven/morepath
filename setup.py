import os
from setuptools import setup, find_packages

setup(name='morepath',
      version = '0.1dev',
      description="A micro web-framework with superpowers",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'venusian >= 1.0a8',
        'reg >= 0.3',
        'werkzeug >= 0.9.4',
        ],
      extras_require = dict(
        test=['pytest >= 2.0',
              'pytest-cov'],
        ),
      )
