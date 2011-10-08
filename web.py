#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

from bottle import route, post, error
import bottle

@route("/")
def index():
    return bottle.template("templates/main.tlp")

@route("/static/:filename")
def server_static(filename):
    return bottle.static_file(filename, root='static')

@route("/api/contact")
def api_contact():
    d = {
        'nickname': 'paurullan',
        'name': 'Pau Rul.lan Ferragut',
        'full name': 'Pau Ruŀlan Ferragut',
        'homepage': 'http://paurullan.com',
        'email': 'paurullan@gmail.com',
        'flickr': 'http://flickr.com/photos/paurullan',
        'twitter': 'http://twitter.com/paurullan',
    }
    return d

@error(404)
def error404(error):
    return bottle.template("templates/404.tlp")

if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(reloader=True)
else:
    # arrancar en mode wsgi
    application = bottle.app()
