from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pytroid',
    version='0.0.1',
    description='Emulator for NES games written in Python',
    long_description='',
    url='https://github.com/hahcho/pytroid',
    author='Mario Daskalov',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nes emulator nintendo',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pytroid=pytroid:main',
        ],
    },
)
