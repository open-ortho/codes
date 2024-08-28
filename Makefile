NAME = open_ortho_terminology

.PHONY: clean deploy

build:
	mkdir -p build
	python3 -m $(NAME).main

dist:
	python3 ./setup.py sdist bdist_wheel

deploy: dist
	twine upload dist/*

clean:
	rm -rf build dist