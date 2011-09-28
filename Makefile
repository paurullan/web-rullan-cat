all: css

test: all

css:
	sass style.sass > style.css

