test:
	pytest -s -v --html=./test_report/report.html  --self-contained-html

release:
	rm -Rf ./dist ./build
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload  ./dist/*

setup:
	virtualenv venv
	pip install -r ./requirements-dev.txt
	pip install -r ./requirements.txt