try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pyudorandom

setup(
    name='pyudorandom',
    version=pyudorandom.__version__,
    packages=['pyudorandom'],
    author=pyudorandom.__author__,
    author_email='mats@plysjbyen.net',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ),
    description='Generate pseudorandom numbers by using algebra',
    test_suite='test_pyudorandom'
)
