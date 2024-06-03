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
    "khmercut",
    "khmerpronounce"
]

setup(
    name='khmernlp',
    version='0.1.0',
    packages=['khmernlp'],
    url='https://github.com/MetythornPenn/khmernlp.git',
    license='Apache Software License 2.0',
    author = 'Metythorn Penn',
    author_email = 'metythorn@gmail.com',
    keywords='khmernlp',
    description='Khmer language toolkits',
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
