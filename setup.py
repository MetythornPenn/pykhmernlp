import os
from setuptools import setup


def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
    
requirements = [
    "tha",
    "regex",
    "pandas",
    "openpyxl",
    "khmerpronounce",
]

setup(
    name='pykhmernlp',
    version='0.0.1',
    packages=['pykhmernlp'],
    url='https://github.com/MetythornPenn/pykhmernlp.git',
    license='Apache Software License 2.0',
    author = 'Metythorn Penn',
    author_email = 'metythorn@gmail.com',
    keywords='pykhmernlp',
    description='Collection of Khmer language toolkits',
    install_requires=requirements,
    long_description=(read('README.md')),
    long_description_content_type='text/markdown',
	classifiers= [
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
	],
)
