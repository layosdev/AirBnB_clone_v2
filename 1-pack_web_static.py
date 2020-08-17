#!/usr/bin/python3
import time
from fabric.api import *


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    local("sudo mkdir -p versions")
    date = time.localtime().strftime("%Y%m%d%H%M%S")
    file = ("versions/web_static_{}.tgz").format(date)
    local("sudo tar -cvzf {} web_static".format(file))
    return file
