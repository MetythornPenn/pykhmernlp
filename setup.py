import os
from setuptools import setup, find_packages


def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
    
requirements = [
    "tha",
    "regex",
    "pandas",
    "openpyxl",
    "khmercut",
    "khmerpronounce",
    "importlib_resources",
]

setup(
    name='pykhmernlp',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pykhmernlp': [
            'corpus/*',
            'address/phum/*.txt',
            'address/khum/*.txt',
            'address/srok/*.txt',
            'address/province/*.txt'
        ]
    },
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
