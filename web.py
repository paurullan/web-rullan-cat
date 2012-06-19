#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import print_function, division

__version__ = "0.0.1"

from bottle import route, error
import bottle

@route("/")
def index():
    return bottle.template("index")

@route("/geo")
def geo():
    return bottle.template("geo")

@route("/static/:filename")
def server_static(filename):
    return bottle.static_file(filename, root='static')

@error(404)
def error404(error):
    return bottle.template("404")

if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(reloader=True)
else:
    # arrancar en mode wsgi
    application = bottle.app()

