all: css

test: all

css:
	sass style.sass > static/style.css

