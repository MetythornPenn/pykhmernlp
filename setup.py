from setuptools import find_packages, setup

readme = """

KhmerNLP is a Python library for Khmer natural language processing.
The library provides functions like word tokenization, khmer corpus,
transliteration, soundex generation, spell checking, and
date and time parsing/formatting.


# Install

For stable version:

```sh
pip install khmernlp
```

"""

requirements = [
    "requests>=2.22.0",
    "backports.zoneinfo; python_version<'3.9'",
    "tzdata; sys_platform == 'win32'"
]

extras = {
    "attacut": ["attacut>=1.0.6"],
    "benchmarks": ["PyYAML>=5.3.1", "numpy>=1.22", "pandas>=0.24"],
    "icu": ["pyicu>=2.3"],
    "ipa": ["epitran>=1.1"],
    "ml": ["numpy>=1.22", "torch>=1.0.0"],
    "ssg": ["ssg>=0.0.8"],
    "thai2fit": ["emoji>=0.5.1", "gensim>=4.0.0", "numpy>=1.22"],
    "thai2rom": ["numpy>=1.22", "torch>=1.0.0"],
    "translate": [
        "fairseq>=0.10.0",
        "sacremoses>=0.0.41",
        "sentencepiece>=0.1.91",
        "torch>=1.0.0",
        "transformers>=4.6.0",
    ],
    "wunsen": ["wunsen>=0.0.1"],
    "textaugment": [
        "bpemb",
        "gensim>=4.0.0"
    ],
    "wangchanberta": [
        "transformers>=4.6.0",
        "sentencepiece>=0.1.91"
    ],
    "mt5": ["transformers>=4.6.0", "sentencepiece>=0.1.91"],
    "wtp": ["transformers>=4.6.0", "wtpsplit>=1.0.1"],
    "wordnet": ["nltk>=3.3"],
    "generate": ["fastai<2.0"],
    "sefr_cut": ["sefr_cut>=1.1"],
    "spell": [
        "phunspell>=0.1.6",
        "spylls>=0.1.5",
        "symspellpy>=6.7.6"
    ],
    "oskut": ["oskut>=1.3"],
    "nlpo3": ["nlpo3>=1.2.2"],
    "onnx": [
        "sentencepiece>=0.1.91",
        "numpy>=1.22",
        "onnxruntime>=1.10.0"
    ],
    "thai_nner": ["thai_nner"],
    "esupar": [
        "esupar>=1.3.8",
        "numpy",
        "transformers>=4.22.1",
    ],
    "spacy_thai": ["spacy_thai>=0.7.1"],
    "transformers_ud": [
        "ufal.chu-liu-edmonds>=1.0.2",
        "transformers>=4.22.1",
    ],
    "dependency_parsing": [
        "spacy_thai>=0.7.1",
        "ufal.chu-liu-edmonds>=1.0.2",
        "transformers>=4.22.1",
    ],
    "coreference_resolution":{
        "spacy>=3.0",
        "fastcoref>=2.1.5",
    },
    "word_approximation":{
        "panphon>=0.20.0"
    },
    "wangchanglm": [
        "transformers>=4.6.0",
        "sentencepiece>=0.1.91",
        "pandas>=0.24"
    ],
    "wsd":{
        "sentence-transformers>=2.2.2"
    },
    "el":{
        "multiel>=0.5"
    },
    "abbreviation":{
        "khamyo>=0.2.0"
    },
    "full": [
        "PyYAML>=5.3.1",
        "attacut>=1.0.4",
        "emoji>=0.5.1",
        "epitran>=1.1",
        "fairseq>=0.10.0",
        "gensim>=4.0.0",
        "nltk>=3.3",
        "numpy>=1.22",
        "pandas>=0.24",
        "pyicu>=2.3",
        "sacremoses>=0.0.41",
        "sentencepiece>=0.1.91",
        "ssg>=0.0.8",
        "torch>=1.0.0",
        "fastai<2.0",
        "bpemb>=0.3.2",
        "transformers>=4.22.1",
        "sefr_cut>=1.1",
        "phunspell>=0.1.6",
        "spylls>=0.1.5",
        "symspellpy>=6.7.6",
        "oskut>=1.3",
        "nlpo3>=1.2.2",
        "onnxruntime>=1.10.0",
        "thai_nner",
        "wunsen>=0.0.3",
        "wtpsplit>=1.0.1",
        "spacy_thai>=0.7.1",
        "spacy>=3.0",
        "fastcoref>=2.1.5",
        "ufal.chu-liu-edmonds>=1.0.2",
        "panphon>=0.20.0",
        "sentence-transformers>=2.2.2",
        "khamyo>=0.2.0",
    ],
}

setup(
    name="khmernlp",
    version="0.0.1",
    description="Khmer Natural Language Processing library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="MetythornPenn",
    author_email="metythorn@gmail.com",
    url="https://github.com/metythornpenn/khmernlp",
    packages=find_packages(exclude=["tests", "tests.*"]),
    test_suite="tests",
    python_requires=">=3.7",
    package_data={
        "khmernlp": [
            "corpus/*",
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "khmernlp",
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "KhmerNLP",
        "Khmer NLP",
        "Khmer language",
    ],
    entry_points={
        "console_scripts": [
            "khmernlp = khmernlp.__main__:main",
        ],
    },
    project_urls={
        "Source Code": "https://github.com/metythornpenn/khmernlp",
    
    },
)

