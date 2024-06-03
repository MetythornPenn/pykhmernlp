import setuptools

with open("README.md", "r") as f:
  long_description = f.read()

setuptools.setup(
  name="khmernlp",
  version="0.0.1",
  description="Khmer Language Toolkit.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/MetythornPenn/khmernlp.git",
  author="Metythorn Penn",
  author_email="metythorn@gmail.com",
  license="Apache License 2.0",
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Natural Language :: English",
  ],
  python_requires=">3.5",
  packages=setuptools.find_packages(),
  package_dir={"khmernlp": "khmernlp"},
  install_requires=[
    "tha",
    "regex",
    "pandas",
    "openpyxl",
    "khmercut",
    "khmerpronounce"
  ],
)
