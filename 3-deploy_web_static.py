#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
from os.path import exists
env.hosts = ["34.75.140.59", "34.75.62.232"]


def do_pack():
    """ distributes an archive to your web servers """
    local("sudo mkdir -p versions")
    d = datetime.now().strftime("%Y%m%d%H%M%S")
    f = ("versions/web_static_{}.tgz").format(d)
    local("sudo tar -cvzf {} web_static".format(f))
    return f


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if exists(archive_path) is False:
        return False
    else:
        pass
    try:
        put(archive_path, "/tmp/")
        f = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(f)
        run("mkdir {}".format(path))
        run("tar -zxvf /tmp/{}.tgz -C {}/".format(f, path))
        run("sudo rm /tmp/{}".format(archive_path.split("/")[1]))
        run("sudo rm /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(f))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(f, f))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(f))
        return True
    except:
        return False


def deploy():
    """ creates and distributes an archive to your web servers """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
