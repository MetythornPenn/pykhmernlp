install:
	rm -rf *.egg-info/ dist/ pykhmernlp.egg-info
	pip install -e .

remove:
	pip uninstall pykhmernlp -y

build-docs:
	mkdocs build

deploy-docs:
	mkdocs gh-deploy

serve-docs:
	mkdocs serve