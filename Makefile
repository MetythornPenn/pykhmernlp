install:
	rm -rf *.egg-info/ dist/ pykhmernlp.egg-info
	pip install -e .

remove:
	pip uninstall pykhmernlp -y



