install:
	rm -rf *.egg-info/ dist/ khmernlp.egg-info
	pip install -e .

remove:
	pip uninstall khmernlp -y

