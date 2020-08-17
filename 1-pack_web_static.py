#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    local("sudo mkdir -p versions")
    d = datetime.now().strftime("%Y%m%d%H%M%S")
    f = ("versions/web_static_{}.tgz").format(d)
    local("sudo tar -cvzf {} web_static".format(f))
    return f
