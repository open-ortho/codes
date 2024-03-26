build:
	mkdir -p build
	python3 ./python/save_codes.py

.PHONY: clean
clean:
	rm -rf build