VERSION=0.0.1
DIST_FILE=fiap-solution-sprint-openlibrary_$(VERSION).zip

clean:
	rm -r build || true
	rm -r dist || true
build: clean
	mkdir build
	cp requirements.txt build/
	cp -R src/* build/
	cd build && pip3 install --no-cache-dir --no-deps -r requirements.txt --force -t . && pip install numpy --upgrade
	mkdir dist
	cd build && zip -ur ../dist/$(DIST_FILE) * -x requirements.txt
