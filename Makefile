run: venv/bin/lektor
	venv/bin/lektor server -h 0.0.0.0 -p 8080

lektor: assets/main.css

venv/bin/lektor: venv
	venv/bin/pip install -r requirements.txt

venv:
	virtualenv -p python3 $@

distclean:
	-venv/bin/lektor clean
	-rm -Rf venv

tmp/normalize.css:
	mkdir -p tmp
	wget https://raw.githubusercontent.com/necolas/normalize.css/7.0.0/normalize.css -O $@

assets/main.css: tmp/normalize.css src/main.css
	cat $+ > $@
