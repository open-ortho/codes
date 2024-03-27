.PHONY: clean deploy

dist:
	python3 ./setup.py sdist bdist_wheel

build:
	mkdir -p build
	python3 ./python/save_codes.py

deploy: dist
	twine upload dist/*

clean:
	rm -rf build dist