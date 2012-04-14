all: css

test: all

css:
	sass style.sass > static/style.css
	sass mobile.sass > static/mobile.css

init_uwsgi_debug:
	uwsgi -M  --plugins http,python --file web.py -s 127.0.0.1:3031

uwsgi: init_uwsgi
init_uwsgi:
	# just show errors
	# 4 workers, master process
	# plugins http and python
	# init file X at socket y:z
	uwsgi -L -p 5 -M  --plugins http,python --file web.py -s 127.0.0.1:3031

init_uwsgi_demonize:
	# demonize and put in file LOG
	uwsgi -d LOG -L -p 4 -M  --plugins http,python --file web.py -s 127.0.0.1:3031

uwsgi_alone:
	uwsgi -p 5 -M -L --plugins http,python --http :8080  --file web.py 

