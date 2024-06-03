install:
	rm -rf *.egg-info/ dist/ km_nlp.egg-info
	pip install -e .

remove:
	pip uninstall pykhmernlp -y

