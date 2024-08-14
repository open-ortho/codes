NAME = ortho_codes

.PHONY: clean deploy

dist:
	python3 ./setup.py sdist bdist_wheel

build:
	mkdir -p build
	python3 -m $(NAME).main

deploy: dist
	twine upload dist/*

clean:
	rm -rf build dist