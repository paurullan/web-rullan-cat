#!/usr/bin/env python
# -*- coding: utf-8 -*-

# www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip
from fabric.api import local, run

__version__ = "0.0.1"

set(
    fab_users='paurullan',
    fab_hosts=['kiwi5.apsl.net'],
    site='web-paurullan',
    )

def deploy():
    local('git pull')
    local('git push')
    run('cd $(site) && git pull')
    run('touch reload/paurullan.reload')
    
