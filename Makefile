build:
	python setup.py build

install:
	python setup.py install

install-local:
	python setup.py install --user

test:
	python setup.py test

.PHONY: build install install-local test