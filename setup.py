import os
from setuptools import setup, find_packages


def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
    
requirements = [
    "regex",
    "tha",
    "khmercut",
    "khmerpronounce",
]

setup(
    name='pykhmernlp',
    version='0.0.13',
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={
        'pykhmernlp': [
            'corpus/icu_words.txt',
            'corpus/english_words.txt',
            'corpus/khmer_dictionary.tsv',
            'corpus/english_dictionary.tsv',
            'address/address_data/phum.tsv',
            'address/address_data/khum.tsv',
            'address/address_data/srok.tsv',
            'address/address_data/province.txt',
        ],
    },
    include_package_data=True,
    zip_safe=False,
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
