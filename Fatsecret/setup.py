
from setuptools import setup, find_packages

setup(
    name='Fatsecret',
    version='0.1.0',
    packages=Fatsecret_packages(),
    install_requires=[
        'numpy',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'Fatsecret = Fatsecret:Python Wrapper',
        ],
    },
)
