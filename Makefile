all: css

test: all

css:
	sass style.sass > static/style.css

init_uwsgi_debug:
	uwsgi -M  --plugins http,python --file web.py -s 127.0.0.1:3031

init_uwsgi:
	# demonize to file LOG, disable logging 
	# 4 workers, master process
	# plugins http and python
	# init file X at socket y:z
	uwsgi -d LOG -L -p 4 -M  --plugins http,python --file web.py -s 127.0.0.1:3031
