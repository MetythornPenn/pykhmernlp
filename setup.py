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
    "khmerpronounce",
]

setup(
    name='pykhmernlp',
    version='0.0.5',
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={
        "pythainlp": [
            "corpus/*",
            "adddress/address_data/phum*",
            "adddress/address_data/khum*",
            "adddress/address_data/srok*",
            "adddress/address_data/province*",
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
